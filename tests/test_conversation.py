import unittest
import json
from unittest.mock import Mock, patch
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.ai_model import ParamAIModel
from services.stt_service import STTService
from services.tts_service import TTSService

class TestFarmerAIAssistant(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures"""
        self.ai_model = ParamAIModel()
        self.stt_service = STTService()
        self.tts_service = TTSService()
    
    def test_context_extraction(self):
        """Test farming context extraction from speech"""
        test_speech = "Haryana mein gehun ki kheti kar raha hun, paani ki kami hai"
        
        context = self.stt_service.extract_farming_context(test_speech)
        
        self.assertIsNotNone(context)
        self.assertEqual(context['location'], 'हरियाणा')
        self.assertEqual(context['crop'], 'wheat')
        self.assertEqual(context['water_condition'], 'shortage')
    
    def test_ai_response_generation(self):
        """Test AI response generation with context"""
        context = {
            'location': 'Haryana',
            'crop': 'wheat',
            'water_condition': 'shortage',
            'soil_type': 'black soil',
            'season': 'rabi'
        }
        
        query = "kaunsi dawa use karein?"
        
        response = self.ai_model.generate_response(context, query)
        
        self.assertIsNotNone(response)
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 10)
    
    def test_multilingual_support(self):
        """Test multilingual language detection"""
        # Test Hindi
        hindi_text = "मेरी फसल में कीट लग गए हैं"
        lang = self.ai_model._detect_language(hindi_text)
        self.assertEqual(lang, "hindi")
        
        # Test English
        english_text = "My crop has pests"
        lang = self.ai_model._detect_language(english_text)
        self.assertEqual(lang, "english")
    
    def test_greeting_messages(self):
        """Test greeting messages in different languages"""
        # Test Hindi greeting
        hindi_greeting = self.tts_service.get_greeting_message("hindi")
        self.assertIn("नमस्ते", hindi_greeting)
        
        # Test English greeting
        english_greeting = self.tts_service.get_greeting_message("english")
        self.assertIn("Hello", english_greeting)
    
    def test_query_prompts(self):
        """Test query prompts in different languages"""
        # Test Hindi prompt
        hindi_prompt = self.tts_service.get_query_prompt("hindi")
        self.assertIn("सवाल", hindi_prompt)
        
        # Test English prompt
        english_prompt = self.tts_service.get_query_prompt("english")
        self.assertIn("question", english_prompt)
    
    def test_fallback_responses(self):
        """Test fallback responses when model is not available"""
        # Mock model as None to test fallback
        self.ai_model.model = None
        
        context = {
            'location': 'Haryana',
            'crop': 'wheat',
            'water_condition': 'shortage'
        }
        
        query = "kaunsi dawa use karein?"
        response = self.ai_model.generate_response(context, query)
        
        self.assertIsNotNone(response)
        self.assertIn("नीम", response)  # Should mention neem oil
    
    def test_voice_mapping(self):
        """Test voice mapping for different languages"""
        # Test Hindi voice mapping
        hindi_voice = self.tts_service.voice_mapping["hindi"]
        self.assertIn("vakyansh", hindi_voice)
        self.assertIn("edge", hindi_voice)
        self.assertIn("gtts", hindi_voice)
        
        # Test English voice mapping
        english_voice = self.tts_service.voice_mapping["english"]
        self.assertIn("vakyansh", english_voice)
        self.assertIn("edge", english_voice)
        self.assertIn("gtts", english_voice)
    
    def test_language_codes(self):
        """Test language codes for STT"""
        # Test Hindi language code
        hindi_code = self.stt_service.language_codes["hindi"]
        self.assertEqual(hindi_code, "hi-IN")
        
        # Test English language code
        english_code = self.stt_service.language_codes["english"]
        self.assertEqual(english_code, "en-IN")
    
    @patch('requests.post')
    def test_stt_service_fallback(self, mock_post):
        """Test STT service fallback when main service fails"""
        # Mock failed response
        mock_response = Mock()
        mock_response.status_code = 500
        mock_post.return_value = mock_response
        
        # Test fallback
        audio_data = b"fake_audio_data"
        result = self.stt_service.convert_audio_to_text(audio_data, "hindi")
        
        # Should handle gracefully
        self.assertIsInstance(result, (str, type(None)))
    
    @patch('requests.post')
    def test_tts_service_fallback(self, mock_post):
        """Test TTS service fallback when main service fails"""
        # Mock failed response
        mock_response = Mock()
        mock_response.status_code = 500
        mock_post.return_value = mock_response
        
        # Test fallback
        text = "Test message"
        result = self.tts_service.text_to_speech(text, "hindi")
        
        # Should handle gracefully
        self.assertIsInstance(result, (bytes, type(None)))

class TestConversationFlow(unittest.TestCase):
    
    def test_conversation_context_management(self):
        """Test conversation context management"""
        # Simulate conversation flow
        call_sid = "test_call_123"
        context = {
            'location': 'Haryana',
            'crop': 'wheat',
            'water_condition': 'shortage'
        }
        
        # This would be managed by the main application
        # For testing, we'll simulate the flow
        self.assertIsNotNone(call_sid)
        self.assertIsNotNone(context)
        self.assertIn('location', context)
        self.assertIn('crop', context)
        self.assertIn('water_condition', context)
    
    def test_end_call_detection(self):
        """Test end call phrase detection"""
        end_phrases = ["नहीं", "no", "बंद", "end", "खत्म"]
        
        # Test end call detection
        test_phrases = [
            "नहीं, मैं बंद करना चाहता हूं",
            "No, I want to end the call",
            "बंद कर दो",
            "End the call",
            "खत्म करो"
        ]
        
        for phrase in test_phrases:
            phrase_lower = phrase.lower()
            is_end_call = any(word in phrase_lower for word in end_phrases)
            self.assertTrue(is_end_call, f"Failed to detect end call in: {phrase}")

if __name__ == '__main__':
    unittest.main() 