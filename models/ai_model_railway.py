import logging
from typing import Dict, Any
import requests
import json

class RailwayAIModel:
    def __init__(self, model_path: str = None, device: str = "cpu"):
        self.model_path = model_path
        self.device = device
        self.logger = logging.getLogger(__name__)
        
        # Language mapping for multilingual support
        self.language_map = {
            "hindi": "हिंदी",
            "english": "English", 
            "punjabi": "ਪੰਜਾਬੀ",
            "gujarati": "ગુજરાતી",
            "marathi": "मराठी",
            "telugu": "తెలుగు",
            "tamil": "தமிழ்",
            "kannada": "ಕನ್ನಡ",
            "bengali": "বাংলা",
            "odia": "ଓଡ଼ିଆ",
            "assamese": "অসমীয়া",
            "malayalam": "മലയാളം"
        }
        
        self.logger.info("Railway AI Model initialized (using cloud APIs)")
    
    def _detect_language(self, text: str) -> str:
        """Detect the language of the input text"""
        # Simple language detection based on common words
        hindi_words = ["क्या", "कैसे", "कहाँ", "कब", "कौन", "क्यों", "है", "हैं", "था", "थी", "पानी", "फसल", "खेती"]
        english_words = ["what", "how", "where", "when", "who", "why", "is", "are", "was", "were", "water", "crop", "farming"]
        
        text_lower = text.lower()
        hindi_count = sum(1 for word in hindi_words if word in text_lower)
        english_count = sum(1 for word in english_words if word in text_lower)
        
        if hindi_count > english_count:
            return "hindi"
        else:
            return "english"
    
    def generate_response(self, context: Dict[str, Any], query: str) -> str:
        """Generate a farming advice response based on context and query"""
        try:
            # Detect language
            detected_lang = self._detect_language(query)
            
            # Use cloud API or fallback response
            return self._generate_cloud_response(context, query, detected_lang)
            
        except Exception as e:
            self.logger.error(f"Error generating response: {e}")
            return self._generate_fallback_response(context, query, "hindi")
    
    def _generate_cloud_response(self, context: Dict[str, Any], query: str, language: str) -> str:
        """Generate response using cloud API (HuggingFace Inference API)"""
        try:
            # You can use HuggingFace Inference API here
            # For now, we'll use fallback responses
            return self._generate_fallback_response(context, query, language)
            
        except Exception as e:
            self.logger.error(f"Cloud API error: {e}")
            return self._generate_fallback_response(context, query, language)
    
    def _generate_fallback_response(self, context: Dict[str, Any], query: str, language: str) -> str:
        """Generate a fallback response when model is not available"""
        
        # Simple rule-based responses based on common farming queries
        query_lower = query.lower()
        
        if "dawa" in query_lower or "pesticide" in query_lower or "medicine" in query_lower:
            return f"आपकी फसल {context.get('crop', '')} के लिए, पानी की कमी की स्थिति में, आप नीम का तेल या बायोपेस्टिसाइड का उपयोग कर सकते हैं। यह सुरक्षित और प्रभावी है।"
        
        elif "paani" in query_lower or "water" in query_lower or "irrigation" in query_lower:
            return f"पानी की कमी में, ड्रिप इरिगेशन या फरो इरिगेशन का उपयोग करें। सुबह या शाम को पानी दें ताकि वाष्पीकरण कम हो।"
        
        elif "khad" in query_lower or "fertilizer" in query_lower or "manure" in query_lower:
            return f"जैविक खाद जैसे गोबर की खाद या वर्मीकम्पोस्ट का उपयोग करें। यह मिट्टी की गुणवत्ता बेहतर करेगा।"
        
        elif "bima" in query_lower or "insurance" in query_lower:
            return f"फसल बीमा के लिए अपने नजदीकी कृषि कार्यालय में संपर्क करें। यह आपकी फसल को सुरक्षा देगा।"
        
        elif "sukha" in query_lower or "drought" in query_lower:
            return f"सूखे की स्थिति में, मल्चिंग का उपयोग करें और पानी बचाने वाली तकनीक अपनाएं।"
        
        elif "kiraya" in query_lower or "rent" in query_lower:
            return f"किराए पर ट्रैक्टर या मशीनरी लेने के लिए स्थानीय कृषि केंद्र से संपर्क करें।"
        
        else:
            return f"आपकी फसल {context.get('crop', '')} के लिए, स्थानीय कृषि विशेषज्ञ से सलाह लें। वे आपकी स्थानीय स्थिति के अनुसार सटीक सलाह दे सकते हैं।" 