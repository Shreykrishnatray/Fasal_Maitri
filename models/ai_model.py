import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import logging
from typing import Dict, Any
import os

class ParamAIModel:
    def __init__(self, model_path: str = "./models/param-1-2.9b-instruct", device: str = "cpu"):
        self.model_path = model_path
        self.device = device
        self.tokenizer = None
        self.model = None
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
        
        self._load_model()
    
    def _load_model(self):
        """Load the Param model and tokenizer"""
        try:
            self.logger.info(f"Loading Param model from {self.model_path}")
            
            # Check if model exists locally
            if not os.path.exists(self.model_path):
                self.logger.warning(f"Model not found at {self.model_path}. Using default model.")
                # You can specify the HuggingFace model name here
                model_name = "BharatGenAI/Param-1-2.9B-Instruct"
            else:
                model_name = self.model_path
            
            self.tokenizer = AutoTokenizer.from_pretrained(model_name)
            self.model = AutoModelForCausalLM.from_pretrained(
                model_name,
                torch_dtype=torch.float16 if self.device == "cuda" else torch.float32,
                device_map="auto" if self.device == "cuda" else None,
                trust_remote_code=True
            )
            
            if self.device == "cpu":
                self.model = self.model.to("cpu")
            
            self.logger.info("Param model loaded successfully")
            
        except Exception as e:
            self.logger.error(f"Error loading model: {e}")
            # Fallback to a simpler model or mock response
            self._load_fallback_model()
    
    def _load_fallback_model(self):
        """Load a fallback model or create mock responses"""
        self.logger.info("Loading fallback model")
        # For now, we'll use mock responses
        self.model = None
        self.tokenizer = None
    
    def _detect_language(self, text: str) -> str:
        """Detect the language of the input text"""
        # Simple language detection based on common words
        hindi_words = ["क्या", "कैसे", "कहाँ", "कब", "कौन", "क्यों", "है", "हैं", "था", "थी"]
        english_words = ["what", "how", "where", "when", "who", "why", "is", "are", "was", "were"]
        
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
            
            # Build the prompt
            prompt = self._build_prompt(context, query, detected_lang)
            
            if self.model is None:
                # Fallback response
                return self._generate_fallback_response(context, query, detected_lang)
            
            # Generate response using the model
            inputs = self.tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
            
            with torch.no_grad():
                outputs = self.model.generate(
                    inputs.input_ids,
                    max_length=512,
                    temperature=0.7,
                    do_sample=True,
                    pad_token_id=self.tokenizer.eos_token_id
                )
            
            response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            
            # Extract only the generated part
            response = response[len(prompt):].strip()
            
            return response
            
        except Exception as e:
            self.logger.error(f"Error generating response: {e}")
            return self._generate_fallback_response(context, query, "hindi")
    
    def _build_prompt(self, context: Dict[str, Any], query: str, language: str) -> str:
        """Build a multilingual prompt for the AI model"""
        
        # Get language name in native script
        lang_name = self.language_map.get(language, "हिंदी")
        
        prompt = f"""You are an expert agriculture advisor. Please respond in {lang_name}.

Farmer Location: {context.get('location', 'Unknown')}
Crop: {context.get('crop', 'Unknown')}
Water Condition: {context.get('water_condition', 'Unknown')}
Soil Type: {context.get('soil_type', 'Unknown')}
Season: {context.get('season', 'Unknown')}

Farmer Query: "{query}"

Give a clear, short, and practical answer in simple {lang_name} that a farmer can easily understand and follow. Focus on:
1. Immediate actionable steps
2. Cost-effective solutions
3. Local availability of resources
4. Safety precautions

Answer:"""

        return prompt
    
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
        
        else:
            return f"आपकी फसल {context.get('crop', '')} के लिए, स्थानीय कृषि विशेषज्ञ से सलाह लें। वे आपकी स्थानीय स्थिति के अनुसार सटीक सलाह दे सकते हैं।" 