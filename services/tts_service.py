import requests
import logging
import tempfile
import os
from typing import Optional, Tuple
from gtts import gTTS
import edge_tts
import asyncio
import io

class TTSService:
    def __init__(self, tts_url: str = "http://localhost:8002/tts"):
        self.tts_url = tts_url
        self.logger = logging.getLogger(__name__)
        
        # Voice mapping for different languages
        self.voice_mapping = {
            "hindi": {
                "vakyansh": "hi-IN-MadhurNeural",
                "edge": "hi-IN-MadhurNeural",
                "gtts": "hi"
            },
            "english": {
                "vakyansh": "en-IN-NeerjaNeural", 
                "edge": "en-IN-NeerjaNeural",
                "gtts": "en"
            },
            "punjabi": {
                "vakyansh": "pa-IN-GurpreetNeural",
                "edge": "pa-IN-GurpreetNeural", 
                "gtts": "pa"
            },
            "gujarati": {
                "vakyansh": "gu-IN-DhwaniNeural",
                "edge": "gu-IN-DhwaniNeural",
                "gtts": "gu"
            },
            "marathi": {
                "vakyansh": "mr-IN-AarohiNeural", 
                "edge": "mr-IN-AarohiNeural",
                "gtts": "mr"
            },
            "telugu": {
                "vakyansh": "te-IN-ShrutiNeural",
                "edge": "te-IN-ShrutiNeural",
                "gtts": "te"
            },
            "tamil": {
                "vakyansh": "ta-IN-PallaviNeural",
                "edge": "ta-IN-PallaviNeural", 
                "gtts": "ta"
            },
            "kannada": {
                "vakyansh": "kn-IN-SapnaNeural",
                "edge": "kn-IN-SapnaNeural",
                "gtts": "kn"
            },
            "bengali": {
                "vakyansh": "bn-IN-TanishaaNeural",
                "edge": "bn-IN-TanishaaNeural",
                "gtts": "bn"
            },
            "odia": {
                "vakyansh": "or-IN-JyotiNeural",
                "edge": "or-IN-JyotiNeural",
                "gtts": "or"
            },
            "assamese": {
                "vakyansh": "as-IN-JoyeeNeural",
                "edge": "as-IN-JoyeeNeural",
                "gtts": "as"
            },
            "malayalam": {
                "vakyansh": "ml-IN-SobhanaNeural",
                "edge": "ml-IN-SobhanaNeural",
                "gtts": "ml"
            }
        }
    
    def text_to_speech(self, text: str, language: str = "hindi") -> Optional[bytes]:
        """Convert text to speech using Vakyansh TTS"""
        try:
            # Get voice configuration
            voice_config = self.voice_mapping.get(language.lower(), self.voice_mapping["hindi"])
            
            # Prepare the request
            data = {
                'text': text,
                'voice': voice_config["vakyansh"],
                'language': language.lower()
            }
            
            # Make request to Vakyansh TTS
            response = requests.post(
                self.tts_url,
                json=data,
                timeout=30
            )
            
            if response.status_code == 200:
                return response.content
            else:
                self.logger.error(f"TTS API error: {response.status_code}")
                return self._fallback_tts(text, language)
                
        except Exception as e:
            self.logger.error(f"Error in TTS conversion: {e}")
            return self._fallback_tts(text, language)
    
    def _fallback_tts(self, text: str, language: str) -> Optional[bytes]:
        """Fallback TTS using alternative methods"""
        try:
            # Try Edge TTS first as it's better for Indian languages
            return self._edge_tts_fallback(text, language)
        except Exception as e:
            self.logger.error(f"Edge TTS fallback failed: {e}")
            try:
                # Try gTTS as second fallback
                return self._gtts_fallback(text, language)
            except Exception as e2:
                self.logger.error(f"gTTS fallback failed: {e2}")
                return None
    
    def _edge_tts_fallback(self, text: str, language: str) -> Optional[bytes]:
        """Edge TTS fallback"""
        try:
            voice_config = self.voice_mapping.get(language.lower(), self.voice_mapping["hindi"])
            voice = voice_config["edge"]
            
            # Create temporary file
            with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_file:
                temp_path = temp_file.name
            
            # Use edge-tts
            asyncio.run(self._generate_edge_audio(text, voice, temp_path))
            
            # Read the generated audio
            with open(temp_path, 'rb') as f:
                audio_data = f.read()
            
            # Clean up
            os.unlink(temp_path)
            
            return audio_data
            
        except Exception as e:
            self.logger.error(f"Edge TTS error: {e}")
            return None
    
    async def _generate_edge_audio(self, text: str, voice: str, output_path: str):
        """Generate audio using Edge TTS"""
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(output_path)
    
    def _gtts_fallback(self, text: str, language: str) -> Optional[bytes]:
        """Google TTS fallback"""
        try:
            voice_config = self.voice_mapping.get(language.lower(), self.voice_mapping["hindi"])
            lang_code = voice_config["gtts"]
            
            # Create temporary file
            with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_file:
                temp_path = temp_file.name
            
            # Generate speech
            tts = gTTS(text=text, lang=lang_code, slow=False)
            tts.save(temp_path)
            
            # Read the generated audio
            with open(temp_path, 'rb') as f:
                audio_data = f.read()
            
            # Clean up
            os.unlink(temp_path)
            
            return audio_data
            
        except Exception as e:
            self.logger.error(f"gTTS error: {e}")
            return None
    
    def create_twiml_response(self, text: str, language: str = "hindi") -> str:
        """Create TwiML response for Twilio"""
        try:
            # Generate audio
            audio_data = self.text_to_speech(text, language)
            
            if audio_data:
                # Save audio to temporary file and get URL
                audio_url = self._save_audio_for_twilio(audio_data)
                
                # Create TwiML
                twiml = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Play>{audio_url}</Play>
    <Gather input="speech" action="/process_speech" method="POST" speechTimeout="auto" language="{language}">
        <Say>Please speak your question now.</Say>
    </Gather>
</Response>"""
                
                return twiml
            else:
                # Fallback to text-to-speech
                return f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say language="{language}">{text}</Say>
    <Gather input="speech" action="/process_speech" method="POST" speechTimeout="auto" language="{language}">
        <Say>Please speak your question now.</Say>
    </Gather>
</Response>"""
                
        except Exception as e:
            self.logger.error(f"Error creating TwiML: {e}")
            return f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say language="{language}">{text}</Say>
    <Gather input="speech" action="/process_speech" method="POST" speechTimeout="auto" language="{language}">
        <Say>Please speak your question now.</Say>
    </Gather>
</Response>"""
    
    def _save_audio_for_twilio(self, audio_data: bytes) -> str:
        """Save audio file and return public URL for Twilio"""
        # This would typically save to a cloud storage service
        # For now, we'll return a placeholder
        # In production, you'd save to S3, Google Cloud Storage, etc.
        return "https://your-audio-storage-url.com/audio.mp3"
    
    def get_greeting_message(self, language: str = "hindi") -> str:
        """Get greeting message in specified language"""
        greetings = {
            "hindi": "नमस्ते! कृपया अपनी खेती से जुड़ी कुछ जानकारी दें जैसे लोकेशन, फसल, पानी की स्थिति...",
            "english": "Hello! Please provide some information about your farming like location, crop, water condition...",
            "punjabi": "ਸਤ ਸ੍ਰੀ ਅਕਾਲ! ਕਿਰਪਾ ਕਰਕੇ ਆਪਣੀ ਖੇਤੀ ਬਾਰੇ ਕੁਝ ਜਾਣਕਾਰੀ ਦਿਓ ਜਿਵੇਂ ਟਿਕਾਣਾ, ਫਸਲ, ਪਾਣੀ ਦੀ ਸਥਿਤੀ...",
            "gujarati": "નમસ્તે! કૃપા કરીને તમારી ખેતી વિશે કેટલીક માહિતી આપો જેમ કે સ્થાન, પાક, પાણીની સ્થિતિ...",
            "marathi": "नमस्कार! कृपया तुमच्या शेतीबद्दल काही माहिती द्या जसे स्थान, पीक, पाण्याची स्थिती...",
            "telugu": "నమస్కారం! దయచేసి మీ వ్యవసాయం గురించి కొంత సమాచారం ఇవ్వండి వంటి స్థానం, పంట, నీటి పరిస్థితి...",
            "tamil": "வணக்கம்! தயவுசெய்து உங்கள் விவசாயத்தைப் பற்றி சில தகவல்களை வழங்கவும் போன்ற இடம், பயிர், நீர் நிலை...",
            "kannada": "ನಮಸ್ಕಾರ! ದಯವಿಟ್ಟು ನಿಮ್ಮ ಕೃಷಿಯ ಬಗ್ಗೆ ಕೆಲವು ಮಾಹಿತಿಯನ್ನು ನೀಡಿ ಉದಾಹರಣೆಗೆ ಸ್ಥಳ, ಬೆಳೆ, ನೀರಿನ ಸ್ಥಿತಿ...",
            "bengali": "নমস্কার! অনুগ্রহ করে আপনার কৃষিকাজ সম্পর্কে কিছু তথ্য দিন যেমন অবস্থান, ফসল, জলের অবস্থা...",
            "odia": "ନମସ୍କାର! ଦୟାକରି ଆପଣଙ୍କ କୃଷି ବିଷୟରେ କିଛି ସୂଚନା ଦିଅନ୍ତୁ ଯେପରି ସ୍ଥାନ, ଫସଲ, ଜଳର ସ୍ଥିତି...",
            "assamese": "নমস্কাৰ! অনুগ্ৰহ কৰি আপোনাৰ কৃষি সম্পৰ্কে কিছু তথ্য দিয়ক যেনে স্থান, শস্য, পানীৰ অৱস্থা...",
            "malayalam": "നമസ്കാരം! ദയവായി നിങ്ങളുടെ കൃഷിയെക്കുറിച്ച് ചില വിവരങ്ങൾ നൽകുക പോലെ സ്ഥാനം, വിള, വെള്ളത്തിന്റെ അവസ്ഥ..."
        }
        
        return greetings.get(language.lower(), greetings["hindi"])
    
    def get_query_prompt(self, language: str = "hindi") -> str:
        """Get query prompt in specified language"""
        prompts = {
            "hindi": "अब अपना सवाल पूछिए।",
            "english": "Now ask your question.",
            "punjabi": "ਹੁਣ ਆਪਣਾ ਸਵਾਲ ਪੁੱਛੋ।",
            "gujarati": "હવે તમારો પ્રશ્ન પૂછો।",
            "marathi": "आता तुमचा प्रश्न विचारा।",
            "telugu": "ఇప్పుడు మీ ప్రశ్న అడగండి.",
            "tamil": "இப்போது உங்கள் கேள்வியைக் கேள்வி.",
            "kannada": "ಈಗ ನಿಮ್ಮ ಪ್ರಶ್ನೆಯನ್ನು ಕೇಳಿ.",
            "bengali": "এখন আপনার প্রশ্ন জিজ্ঞাসা করুন।",
            "odia": "ବର୍ତ୍ତମାନ ଆପଣଙ୍କ ପ୍ରଶ୍ନ ପଚାରନ୍ତୁ।",
            "assamese": "এতিয়া আপোনাৰ প্ৰশ্ন সুধক।",
            "malayalam": "ഇപ്പോൾ നിങ്ങളുടെ ചോദ്യം ചോദിക്കുക."
        }
        
        return prompts.get(language.lower(), prompts["hindi"]) 