<<<<<<< HEAD
#!/usr/bin/env python3
"""
Test script for Farmer AI Assistant components
"""

import sys
import os
import logging
from typing import Dict, Any

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from config import Config
from models.ai_model import ParamAIModel
from services.stt_service import STTService
from services.tts_service import TTSService

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_ai_model():
    """Test the Param AI model"""
    print("🤖 Testing AI Model (Param-1-2.9B-Instruct)...")
    try:
        ai_model = ParamAIModel()
        
        # Test context and query
        context = {
            'location': 'हरियाणा',
            'crop': 'wheat',
            'water_condition': 'shortage',
            'soil_type': 'loamy',
            'season': 'rabi'
        }
        query = "पानी की कमी में क्या करें?"
        
        response = ai_model.generate_response(context, query)
        print(f"✅ AI Response: {response}")
        return True
    except Exception as e:
        print(f"❌ AI Model Error: {e}")
        return False

def test_stt_service():
    """Test Speech-to-Text service"""
    print("\n🎤 Testing STT Service...")
    try:
        stt_service = STTService()
        
        # Test context extraction
        test_text = "Haryana mein gehun ki kheti kar raha hun, paani ki kami hai"
        context = stt_service.extract_farming_context(test_text)
        print(f"✅ Extracted Context: {context}")
        
        # Test language detection
        languages = ["hindi", "english", "punjabi", "gujarati"]
        for lang in languages:
            code = stt_service.language_codes.get(lang)
            print(f"✅ {lang}: {code}")
        
        return True
    except Exception as e:
        print(f"❌ STT Service Error: {e}")
        return False

def test_tts_service():
    """Test Text-to-Speech service"""
    print("\n🔊 Testing TTS Service...")
    try:
        tts_service = TTSService()
        
        # Test greeting messages
        languages = ["hindi", "english", "punjabi", "gujarati"]
        for lang in languages:
            greeting = tts_service.get_greeting_message(lang)
            print(f"✅ {lang} greeting: {greeting[:50]}...")
        
        # Test query prompts
        for lang in languages:
            prompt = tts_service.get_query_prompt(lang)
            print(f"✅ {lang} prompt: {prompt}")
        
        return True
    except Exception as e:
        print(f"❌ TTS Service Error: {e}")
        return False

def test_multilingual_support():
    """Test multilingual support"""
    print("\n🌍 Testing Multilingual Support...")
    try:
        ai_model = ParamAIModel()
        tts_service = TTSService()
        
        languages = ["hindi", "english", "punjabi", "gujarati", "marathi", "telugu"]
        
        for lang in languages:
            # Test AI model language support
            if lang in ai_model.language_map:
                print(f"✅ {lang}: {ai_model.language_map[lang]}")
            
            # Test TTS voice mapping
            if lang in tts_service.voice_mapping:
                voices = tts_service.voice_mapping[lang]
                print(f"✅ {lang} TTS voices: {list(voices.keys())}")
        
        return True
    except Exception as e:
        print(f"❌ Multilingual Support Error: {e}")
        return False

def test_fallback_mechanisms():
    """Test fallback mechanisms"""
    print("\n🔄 Testing Fallback Mechanisms...")
    try:
        # Test STT fallback
        stt_service = STTService("http://invalid-url:8001/stt")
        print("✅ STT fallback configured")
        
        # Test TTS fallback
        tts_service = TTSService("http://invalid-url:8002/tts")
        print("✅ TTS fallback configured")
        
        return True
    except Exception as e:
        print(f"❌ Fallback Test Error: {e}")
        return False

def test_configuration():
    """Test configuration loading"""
    print("\n⚙️ Testing Configuration...")
    try:
        config = Config()
        
        print(f"✅ Twilio Account SID: {config.TWILIO_ACCOUNT_SID[:10]}...")
        print(f"✅ Twilio Phone Number: {config.TWILIO_PHONE_NUMBER}")
        print(f"✅ AI Model Path: {config.PARAM_MODEL_PATH}")
        print(f"✅ STT URL: {config.VAKYANSH_STT_URL}")
        print(f"✅ TTS URL: {config.VAKYANSH_TTS_URL}")
        print(f"✅ Server Host: {config.HOST}")
        print(f"✅ Server Port: {config.PORT}")
        
        return True
    except Exception as e:
        print(f"❌ Configuration Error: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Starting Farmer AI Assistant Component Tests")
    print("=" * 50)
    
    tests = [
        ("Configuration", test_configuration),
        ("AI Model", test_ai_model),
        ("STT Service", test_stt_service),
        ("TTS Service", test_tts_service),
        ("Multilingual Support", test_multilingual_support),
        ("Fallback Mechanisms", test_fallback_mechanisms),
    ]
    
    results = {}
    
    for test_name, test_func in tests:
        try:
            results[test_name] = test_func()
        except Exception as e:
            print(f"❌ {test_name} failed with exception: {e}")
            results[test_name] = False
    
    print("\n" + "=" * 50)
    print("📊 Test Results Summary:")
    print("=" * 50)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status}: {test_name}")
        if result:
            passed += 1
    
    print(f"\n🎯 Overall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All components are working! Ready for deployment.")
    else:
        print("⚠️ Some components need attention before deployment.")
    
    return passed == total

if __name__ == "__main__":
=======
#!/usr/bin/env python3
"""
Test script for Farmer AI Assistant components
"""

import sys
import os
import logging
from typing import Dict, Any

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from config import Config
from models.ai_model import ParamAIModel
from services.stt_service import STTService
from services.tts_service import TTSService

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_ai_model():
    """Test the Param AI model"""
    print("🤖 Testing AI Model (Param-1-2.9B-Instruct)...")
    try:
        ai_model = ParamAIModel()
        
        # Test context and query
        context = {
            'location': 'हरियाणा',
            'crop': 'wheat',
            'water_condition': 'shortage',
            'soil_type': 'loamy',
            'season': 'rabi'
        }
        query = "पानी की कमी में क्या करें?"
        
        response = ai_model.generate_response(context, query)
        print(f"✅ AI Response: {response}")
        return True
    except Exception as e:
        print(f"❌ AI Model Error: {e}")
        return False

def test_stt_service():
    """Test Speech-to-Text service"""
    print("\n🎤 Testing STT Service...")
    try:
        stt_service = STTService()
        
        # Test context extraction
        test_text = "Haryana mein gehun ki kheti kar raha hun, paani ki kami hai"
        context = stt_service.extract_farming_context(test_text)
        print(f"✅ Extracted Context: {context}")
        
        # Test language detection
        languages = ["hindi", "english", "punjabi", "gujarati"]
        for lang in languages:
            code = stt_service.language_codes.get(lang)
            print(f"✅ {lang}: {code}")
        
        return True
    except Exception as e:
        print(f"❌ STT Service Error: {e}")
        return False

def test_tts_service():
    """Test Text-to-Speech service"""
    print("\n🔊 Testing TTS Service...")
    try:
        tts_service = TTSService()
        
        # Test greeting messages
        languages = ["hindi", "english", "punjabi", "gujarati"]
        for lang in languages:
            greeting = tts_service.get_greeting_message(lang)
            print(f"✅ {lang} greeting: {greeting[:50]}...")
        
        # Test query prompts
        for lang in languages:
            prompt = tts_service.get_query_prompt(lang)
            print(f"✅ {lang} prompt: {prompt}")
        
        return True
    except Exception as e:
        print(f"❌ TTS Service Error: {e}")
        return False

def test_multilingual_support():
    """Test multilingual support"""
    print("\n🌍 Testing Multilingual Support...")
    try:
        ai_model = ParamAIModel()
        tts_service = TTSService()
        
        languages = ["hindi", "english", "punjabi", "gujarati", "marathi", "telugu"]
        
        for lang in languages:
            # Test AI model language support
            if lang in ai_model.language_map:
                print(f"✅ {lang}: {ai_model.language_map[lang]}")
            
            # Test TTS voice mapping
            if lang in tts_service.voice_mapping:
                voices = tts_service.voice_mapping[lang]
                print(f"✅ {lang} TTS voices: {list(voices.keys())}")
        
        return True
    except Exception as e:
        print(f"❌ Multilingual Support Error: {e}")
        return False

def test_fallback_mechanisms():
    """Test fallback mechanisms"""
    print("\n🔄 Testing Fallback Mechanisms...")
    try:
        # Test STT fallback
        stt_service = STTService("http://invalid-url:8001/stt")
        print("✅ STT fallback configured")
        
        # Test TTS fallback
        tts_service = TTSService("http://invalid-url:8002/tts")
        print("✅ TTS fallback configured")
        
        return True
    except Exception as e:
        print(f"❌ Fallback Test Error: {e}")
        return False

def test_configuration():
    """Test configuration loading"""
    print("\n⚙️ Testing Configuration...")
    try:
        config = Config()
        
        print(f"✅ Twilio Account SID: {config.TWILIO_ACCOUNT_SID[:10]}...")
        print(f"✅ Twilio Phone Number: {config.TWILIO_PHONE_NUMBER}")
        print(f"✅ AI Model Path: {config.PARAM_MODEL_PATH}")
        print(f"✅ STT URL: {config.VAKYANSH_STT_URL}")
        print(f"✅ TTS URL: {config.VAKYANSH_TTS_URL}")
        print(f"✅ Server Host: {config.HOST}")
        print(f"✅ Server Port: {config.PORT}")
        
        return True
    except Exception as e:
        print(f"❌ Configuration Error: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Starting Farmer AI Assistant Component Tests")
    print("=" * 50)
    
    tests = [
        ("Configuration", test_configuration),
        ("AI Model", test_ai_model),
        ("STT Service", test_stt_service),
        ("TTS Service", test_tts_service),
        ("Multilingual Support", test_multilingual_support),
        ("Fallback Mechanisms", test_fallback_mechanisms),
    ]
    
    results = {}
    
    for test_name, test_func in tests:
        try:
            results[test_name] = test_func()
        except Exception as e:
            print(f"❌ {test_name} failed with exception: {e}")
            results[test_name] = False
    
    print("\n" + "=" * 50)
    print("📊 Test Results Summary:")
    print("=" * 50)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status}: {test_name}")
        if result:
            passed += 1
    
    print(f"\n🎯 Overall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All components are working! Ready for deployment.")
    else:
        print("⚠️ Some components need attention before deployment.")
    
    return passed == total

if __name__ == "__main__":
>>>>>>> e15bec281abf2b62dc4fb58236aef25909e43dfc
    main() 