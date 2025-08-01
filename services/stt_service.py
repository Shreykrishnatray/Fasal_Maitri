import requests
import logging
import os
from typing import Optional
import wave
import numpy as np
from pydub import AudioSegment
import tempfile

class STTService:
    def __init__(self, stt_url: str = "http://localhost:8001/stt"):
        self.stt_url = stt_url
        self.logger = logging.getLogger(__name__)
        
        # Language codes for Vakyansh STT
        self.language_codes = {
            "hindi": "hi-IN",
            "english": "en-IN", 
            "punjabi": "pa-IN",
            "gujarati": "gu-IN",
            "marathi": "mr-IN",
            "telugu": "te-IN",
            "tamil": "ta-IN",
            "kannada": "kn-IN",
            "bengali": "bn-IN",
            "odia": "or-IN",
            "assamese": "as-IN",
            "malayalam": "ml-IN"
        }
    
    def convert_audio_to_text(self, audio_data: bytes, language: str = "hindi") -> Optional[str]:
        """Convert audio to text using Vakyansh STT"""
        try:
            # Get language code
            lang_code = self.language_codes.get(language.lower(), "hi-IN")
            
            # Prepare the request
            files = {
                'audio': ('audio.wav', audio_data, 'audio/wav'),
                'language': (None, lang_code)
            }
            
            # Make request to Vakyansh STT
            response = requests.post(
                self.stt_url,
                files=files,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                return result.get('text', '')
            else:
                self.logger.error(f"STT API error: {response.status_code}")
                return self._fallback_stt(audio_data, language)
                
        except Exception as e:
            self.logger.error(f"Error in STT conversion: {e}")
            return self._fallback_stt(audio_data, language)
    
    def _fallback_stt(self, audio_data: bytes, language: str) -> Optional[str]:
        """Fallback STT using alternative methods"""
        try:
            # Try using Google Speech Recognition as fallback
            return self._google_stt_fallback(audio_data, language)
        except Exception as e:
            self.logger.error(f"Fallback STT failed: {e}")
            return None
    
    def _google_stt_fallback(self, audio_data: bytes, language: str) -> Optional[str]:
        """Google Speech Recognition fallback"""
        try:
            import speech_recognition as sr
            
            # Save audio to temporary file
            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_file:
                temp_file.write(audio_data)
                temp_file_path = temp_file.name
            
            # Use speech recognition
            recognizer = sr.Recognizer()
            
            with sr.AudioFile(temp_file_path) as source:
                audio = recognizer.record(source)
                
                # Get language code for Google
                lang_code = self.language_codes.get(language.lower(), "hi-IN")
                
                text = recognizer.recognize_google(
                    audio, 
                    language=lang_code
                )
                
                # Clean up
                os.unlink(temp_file_path)
                
                return text
                
        except ImportError:
            self.logger.warning("speech_recognition not available")
            return None
        except Exception as e:
            self.logger.error(f"Google STT fallback failed: {e}")
            return None
    
    def process_twilio_audio(self, audio_url: str, account_sid: str, auth_token: str) -> Optional[str]:
        """Process audio from Twilio call"""
        try:
            # Download audio from Twilio
            response = requests.get(
                audio_url,
                auth=(account_sid, auth_token),
                timeout=30
            )
            
            if response.status_code == 200:
                audio_data = response.content
                return self.convert_audio_to_text(audio_data)
            else:
                self.logger.error(f"Failed to download audio: {response.status_code}")
                return None
                
        except Exception as e:
            self.logger.error(f"Error processing Twilio audio: {e}")
            return None
    
    def extract_farming_context(self, text: str) -> dict:
        """Extract farming-related context from transcribed text"""
        context = {
            'location': None,
            'crop': None,
            'water_condition': None,
            'soil_type': None,
            'season': None
        }
        
        text_lower = text.lower()
        
        # Extract location
        location_keywords = {
            'haryana': 'हरियाणा',
            'punjab': 'पंजाब', 
            'gujarat': 'गुजरात',
            'maharashtra': 'महाराष्ट्र',
            'karnataka': 'कर्नाटक',
            'tamil nadu': 'तमिलनाडु'
        }
        
        for english_loc, hindi_loc in location_keywords.items():
            if english_loc in text_lower:
                context['location'] = hindi_loc
                break
        
        # Extract crop
        crop_keywords = {
            'gehun': 'wheat',
            'chawal': 'rice', 
            'makka': 'maize',
            'bajra': 'pearl millet',
            'jowar': 'sorghum',
            'cotton': 'cotton',
            'sugarcane': 'sugarcane',
            'potato': 'potato',
            'tomato': 'tomato',
            'onion': 'onion'
        }
        
        for hindi_crop, english_crop in crop_keywords.items():
            if hindi_crop in text_lower or english_crop in text_lower:
                context['crop'] = english_crop
                break
        
        # Extract water condition
        if 'paani' in text_lower or 'water' in text_lower:
            if 'kami' in text_lower or 'shortage' in text_lower or 'less' in text_lower:
                context['water_condition'] = 'shortage'
            elif 'bharpur' in text_lower or 'excess' in text_lower or 'more' in text_lower:
                context['water_condition'] = 'excess'
            else:
                context['water_condition'] = 'normal'
        
        # Extract soil type
        soil_keywords = {
            'kali': 'black soil',
            'lal': 'red soil',
            'peeli': 'yellow soil',
            'balu': 'sandy soil',
            'chikni': 'clay soil'
        }
        
        for hindi_soil, english_soil in soil_keywords.items():
            if hindi_soil in text_lower or english_soil in text_lower:
                context['soil_type'] = english_soil
                break
        
        # Extract season
        season_keywords = {
            'rabi': 'rabi',
            'kharif': 'kharif',
            'zaid': 'zaid',
            'summer': 'summer',
            'winter': 'winter',
            'monsoon': 'monsoon'
        }
        
        for season in season_keywords:
            if season in text_lower:
                context['season'] = season
                break
        
        return context 