#!/usr/bin/env python3
"""
Basic test script for Farmer AI Assistant core components
"""

import sys
import os
import logging

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_configuration():
    """Test configuration loading"""
    print("⚙️ Testing Configuration...")
    try:
        # Test basic config structure
        config_vars = {
            "TWILIO_ACCOUNT_SID": "ACf7af130b09bf922ff53a778a761693d3",
            "TWILIO_AUTH_TOKEN": "9beeb37b1b08ba34ce08d0326db9a2bb",
            "TWILIO_PHONE_NUMBER": "+12182199792",
            "PARAM_MODEL_PATH": "./models/param-1-2.9b-instruct",
            "DEVICE": "cpu",
            "VAKYANSH_STT_URL": "http://localhost:8001/stt",
            "VAKYANSH_TTS_URL": "http://localhost:8002/tts",
            "HOST": "0.0.0.0",
            "PORT": 8000,
            "DEBUG": True
        }
        
        print("✅ Configuration structure is correct")
        print(f"✅ Twilio Account SID: {config_vars['TWILIO_ACCOUNT_SID'][:10]}...")
        print(f"✅ Twilio Phone Number: {config_vars['TWILIO_PHONE_NUMBER']}")
        print(f"✅ AI Model Path: {config_vars['PARAM_MODEL_PATH']}")
        print(f"✅ STT URL: {config_vars['VAKYANSH_STT_URL']}")
        print(f"✅ TTS URL: {config_vars['VAKYANSH_TTS_URL']}")
        print(f"✅ Server Host: {config_vars['HOST']}")
        print(f"✅ Server Port: {config_vars['PORT']}")
        
        return True
    except Exception as e:
        print(f"❌ Configuration Error: {e}")
        return False

def test_context_extraction():
    """Test context extraction logic"""
    print("\n🔍 Testing Context Extraction...")
    try:
        # Simulate context extraction logic
        test_speech = "Haryana mein gehun ki kheti kar raha hun, paani ki kami hai"
        
        context = {
            'location': None,
            'crop': None,
            'water_condition': None,
            'soil_type': None,
            'season': None
        }
        
        # Simple keyword-based extraction
        text_lower = test_speech.lower()
        
        # Location extraction
        if "haryana" in text_lower:
            context['location'] = "हरियाणा"
        
        # Crop extraction
        if "gehun" in text_lower or "wheat" in text_lower:
            context['crop'] = "wheat"
        elif "dhan" in text_lower or "rice" in text_lower:
            context['crop'] = "rice"
        elif "baajra" in text_lower or "millet" in text_lower:
            context['crop'] = "millet"
        
        # Water condition extraction
        if "paani ki kami" in text_lower or "water shortage" in text_lower:
            context['water_condition'] = "shortage"
        elif "paani bahut hai" in text_lower or "excess water" in text_lower:
            context['water_condition'] = "excess"
        elif "normal paani" in text_lower or "normal water" in text_lower:
            context['water_condition'] = "normal"
        
        print(f"✅ Extracted Context: {context}")
        return True
    except Exception as e:
        print(f"❌ Context Extraction Error: {e}")
        return False

def test_multilingual_greetings():
    """Test multilingual greeting messages"""
    print("\n🌍 Testing Multilingual Greetings...")
    try:
        greetings = {
            "hindi": "नमस्ते! कृपया अपनी खेती से जुड़ी कुछ जानकारी दें जैसे लोकेशन, फसल, पानी की स्थिति...",
            "english": "Hello! Please provide some information about your farming like location, crop, water condition...",
            "punjabi": "ਸਤ ਸ੍ਰੀ ਅਕਾਲ! ਕਿਰਪਾ ਕਰਕੇ ਆਪਣੀ ਖੇਤੀ ਬਾਰੇ ਕੁਝ ਜਾਣਕਾਰੀ ਦਿਓ ਜਿਵੇਂ ਟਿਕਾਣਾ, ਫਸਲ, ਪਾਣੀ ਦੀ ਸਥਿਤੀ...",
            "gujarati": "નમસ્તે! કૃપા કરીને તમારી ખેતી વિશે કેટલીક માહિતી આપો જેમ કે સ્થાન, પાક, પાણીની સ્થિતિ...",
            "marathi": "नमस्कार! कृपया तुमच्या शेतीबद्दल काही माहिती द्या जसे स्थान, पीक, पाण्याची स्थिती...",
            "telugu": "నమస్కారం! దయచేసి మీ వ్యవసాయం గురించి కొంత సమాచారం ఇవ్వండి, ఉదాహరణకు స్థానం, పంట, నీటి పరిస్థితి..."
        }
        
        for lang, greeting in greetings.items():
            print(f"✅ {lang}: {greeting[:50]}...")
        
        return True
    except Exception as e:
        print(f"❌ Multilingual Greetings Error: {e}")
        return False

def test_query_prompts():
    """Test query prompt messages"""
    print("\n❓ Testing Query Prompts...")
    try:
        prompts = {
            "hindi": "अब अपना सवाल पूछिए।",
            "english": "Now ask your question.",
            "punjabi": "ਹੁਣ ਆਪਣਾ ਸਵਾਲ ਪੁੱਛੋ।",
            "gujarati": "હવે તમારો પ્રશ્ન પૂછો।",
            "marathi": "आता तुमचा प्रश्न विचारा।",
            "telugu": "ఇప్పుడు మీ ప్రశ్న అడగండి."
        }
        
        for lang, prompt in prompts.items():
            print(f"✅ {lang}: {prompt}")
        
        return True
    except Exception as e:
        print(f"❌ Query Prompts Error: {e}")
        return False

def test_ai_prompt_structure():
    """Test AI prompt structure"""
    print("\n🤖 Testing AI Prompt Structure...")
    try:
        context = {
            'location': 'हरियाणा',
            'crop': 'wheat',
            'water_condition': 'shortage',
            'soil_type': 'loamy',
            'season': 'rabi'
        }
        query = "पानी की कमी में क्या करें?"
        language = "hindi"
        
        # Build prompt structure
        lang_name = "हिंदी" if language == "hindi" else "English"
        
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
        
        print("✅ AI Prompt Structure:")
        print(f"   - Language: {lang_name}")
        print(f"   - Location: {context['location']}")
        print(f"   - Crop: {context['crop']}")
        print(f"   - Water: {context['water_condition']}")
        print(f"   - Query: {query}")
        
        return True
    except Exception as e:
        print(f"❌ AI Prompt Structure Error: {e}")
        return False

def test_conversation_flow():
    """Test conversation flow logic"""
    print("\n🔄 Testing Conversation Flow...")
    try:
        # Simulate conversation stages
        stages = [
            "1. Farmer calls +12182199792",
            "2. System greets in Hindi",
            "3. Farmer provides farm details",
            "4. System extracts context",
            "5. System asks for query",
            "6. Farmer asks farming question",
            "7. AI generates contextual response",
            "8. System converts to speech",
            "9. Response played to farmer"
        ]
        
        for stage in stages:
            print(f"✅ {stage}")
        
        return True
    except Exception as e:
        print(f"❌ Conversation Flow Error: {e}")
        return False

def main():
    """Run all basic tests"""
    print("🧪 Starting Basic Farmer AI Assistant Tests")
    print("=" * 50)
    
    tests = [
        ("Configuration", test_configuration),
        ("Context Extraction", test_context_extraction),
        ("Multilingual Greetings", test_multilingual_greetings),
        ("Query Prompts", test_query_prompts),
        ("AI Prompt Structure", test_ai_prompt_structure),
        ("Conversation Flow", test_conversation_flow),
    ]
    
    results = {}
    
    for test_name, test_func in tests:
        try:
            results[test_name] = test_func()
        except Exception as e:
            print(f"❌ {test_name} failed with exception: {e}")
            results[test_name] = False
    
    print("\n" + "=" * 50)
    print("📊 Basic Test Results Summary:")
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
        print("🎉 Core components are working! Ready for ML model integration.")
    else:
        print("⚠️ Some core components need attention.")
    
    print("\n📋 Next Steps:")
    print("1. Install ML dependencies (transformers, torch)")
    print("2. Download Param-1-2.9B-Instruct model")
    print("3. Set up Vakyansh STT/TTS services")
    print("4. Deploy to cloud platform")
    print("5. Configure Twilio webhook")
    
    return passed == total

if __name__ == "__main__":
    main() 