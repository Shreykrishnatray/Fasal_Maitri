import requests
import logging
from typing import Dict, Any, Optional
from twilio.rest import Client
from twilio.twiml import VoiceResponse

class TelephonyService:
    def __init__(self, config):
        self.config = config
        self.logger = logging.getLogger(__name__)
        
        # Initialize Twilio client
        if config.TWILIO_ACCOUNT_SID and config.TWILIO_AUTH_TOKEN:
            self.twilio_client = Client(config.TWILIO_ACCOUNT_SID, config.TWILIO_AUTH_TOKEN)
        else:
            self.twilio_client = None
            self.logger.warning("Twilio credentials not configured")
    
    def create_greeting_response(self, language: str = "hindi") -> str:
        """Create TwiML response for initial greeting"""
        response = VoiceResponse()
        
        greeting_text = self._get_greeting_text(language)
        response.say(greeting_text, language=language)
        
        # Gather speech input
        gather = response.gather(
            input='speech',
            action='/process_context',
            method='POST',
            speech_timeout='auto',
            language=language
        )
        gather.say("कृपया बोलें", language=language)
        
        return str(response)
    
    def create_query_response(self, language: str = "hindi") -> str:
        """Create TwiML response for asking query"""
        response = VoiceResponse()
        
        query_text = self._get_query_text(language)
        response.say(query_text, language=language)
        
        # Gather speech input
        gather = response.gather(
            input='speech',
            action='/process_query',
            method='POST',
            speech_timeout='auto',
            language=language
        )
        gather.say("अपना सवाल पूछें", language=language)
        
        return str(response)
    
    def create_ai_response(self, ai_text: str, language: str = "hindi") -> str:
        """Create TwiML response with AI answer"""
        response = VoiceResponse()
        
        response.say(ai_text, language=language)
        
        # Ask if they want to ask another question
        response.say("क्या आप कोई और सवाल पूछना चाहते हैं?", language=language)
        
        # Gather for another question
        gather = response.gather(
            input='speech',
            action='/process_query',
            method='POST',
            speech_timeout='auto',
            language=language
        )
        gather.say("हाँ या नहीं बोलें", language=language)
        
        return str(response)
    
    def _get_greeting_text(self, language: str) -> str:
        """Get greeting text in specified language"""
        greetings = {
            "hindi": "नमस्ते! कृपया अपनी खेती से जुड़ी कुछ जानकारी दें जैसे लोकेशन, फसल, पानी की स्थिति...",
            "english": "Hello! Please provide some information about your farming like location, crop, water condition...",
            "punjabi": "ਸਤ ਸ੍ਰੀ ਅਕਾਲ! ਕਿਰਪਾ ਕਰਕੇ ਆਪਣੀ ਖੇਤੀ ਬਾਰੇ ਕੁਝ ਜਾਣਕਾਰੀ ਦਿਓ ਜਿਵੇਂ ਟਿਕਾਣਾ, ਫਸਲ, ਪਾਣੀ ਦੀ ਸਥਿਤੀ..."
        }
        return greetings.get(language, greetings["hindi"])
    
    def _get_query_text(self, language: str) -> str:
        """Get query prompt text in specified language"""
        prompts = {
            "hindi": "अब अपना सवाल पूछिए।",
            "english": "Now ask your question.",
            "punjabi": "ਹੁਣ ਆਪਣਾ ਸਵਾਲ ਪੁੱਛੋ।"
        }
        return prompts.get(language, prompts["hindi"])
    
    def make_call(self, to_number: str, from_number: str = None) -> Optional[str]:
        """Make an outbound call using Twilio"""
        if not self.twilio_client:
            self.logger.error("Twilio client not initialized")
            return None
        
        try:
            from_number = from_number or self.config.TWILIO_PHONE_NUMBER
            
            call = self.twilio_client.calls.create(
                to=to_number,
                from_=from_number,
                url='https://your-domain.com/voice',  # Webhook URL
                method='POST'
            )
            
            self.logger.info(f"Call initiated: {call.sid}")
            return call.sid
            
        except Exception as e:
            self.logger.error(f"Error making call: {e}")
            return None 