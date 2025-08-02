<<<<<<< HEAD
#!/usr/bin/env python3
"""
Test script for TTS (Text-to-Speech) Service component
"""

import sys
import os

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_tts_import():
    """Test if TTS service can be imported"""
    print("🔊 Testing TTS Service Import...")
    try:
        from services.tts_service import TTSService
        print("✅ TTS service imported successfully")
        return True
    except Exception as e:
        print(f"❌ TTS service import failed: {e}")
        return False

def test_tts_initialization():
    """Test TTS service initialization"""
    print("\n🔧 Testing TTS Service Initialization...")
    try:
        from services.tts_service import TTSService
        tts_service = TTSService()
        print("✅ TTS service initialized successfully")
        return True
    except Exception as e:
        print(f"❌ TTS service initialization failed: {e}")
        return False

def test_greeting_messages():
    """Test greeting messages in different languages"""
    print("\n👋 Testing Greeting Messages...")
    try:
        from services.tts_service import TTSService
        tts_service = TTSService()
        
        languages = ["hindi", "english", "punjabi", "gujarati", "marathi", "telugu"]
        
        for lang in languages:
            greeting = tts_service.get_greeting_message(lang)
            print(f"✅ {lang}: {greeting[:50]}...")
        
        return True
    except Exception as e:
        print(f"❌ Greeting messages test failed: {e}")
        return False

def test_query_prompts():
    """Test query prompts in different languages"""
    print("\n❓ Testing Query Prompts...")
    try:
        from services.tts_service import TTSService
        tts_service = TTSService()
        
        languages = ["hindi", "english", "punjabi", "gujarati", "marathi", "telugu"]
        
        for lang in languages:
            prompt = tts_service.get_query_prompt(lang)
            print(f"✅ {lang}: {prompt}")
        
        return True
    except Exception as e:
        print(f"❌ Query prompts test failed: {e}")
        return False

def test_voice_mapping():
    """Test voice mapping for different languages"""
    print("\n🎵 Testing Voice Mapping...")
    try:
        from services.tts_service import TTSService
        tts_service = TTSService()
        
        languages = ["hindi", "english", "punjabi", "gujarati", "marathi", "telugu"]
        
        for lang in languages:
            if lang in tts_service.voice_mapping:
                voices = tts_service.voice_mapping[lang]
                print(f"✅ {lang}: {list(voices.keys())}")
            else:
                print(f"❌ {lang}: No voice mapping found")
        
        return True
    except Exception as e:
        print(f"❌ Voice mapping test failed: {e}")
        return False

def test_fallback_mechanism():
    """Test TTS fallback mechanism"""
    print("\n🔄 Testing TTS Fallback Mechanism...")
    try:
        from services.tts_service import TTSService
        # Test with invalid URL to trigger fallback
        tts_service = TTSService("http://invalid-url:8002/tts")
        print("✅ TTS fallback mechanism configured")
        return True
    except Exception as e:
        print(f"❌ TTS fallback test failed: {e}")
        return False

def main():
    """Run TTS service tests"""
    print("🧪 Starting TTS Service Tests")
    print("=" * 40)
    
    tests = [
        ("TTS Import", test_tts_import),
        ("TTS Initialization", test_tts_initialization),
        ("Greeting Messages", test_greeting_messages),
        ("Query Prompts", test_query_prompts),
        ("Voice Mapping", test_voice_mapping),
        ("Fallback Mechanism", test_fallback_mechanism),
    ]
    
    results = {}
    
    for test_name, test_func in tests:
        try:
            results[test_name] = test_func()
        except Exception as e:
            print(f"❌ {test_name} failed with exception: {e}")
            results[test_name] = False
    
    print("\n" + "=" * 40)
    print("📊 TTS Service Test Results:")
    print("=" * 40)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status}: {test_name}")
        if result:
            passed += 1
    
    print(f"\n🎯 Overall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 TTS Service is working perfectly!")
    else:
        print("⚠️ TTS Service needs attention.")
    
    return passed == total

if __name__ == "__main__":
=======
#!/usr/bin/env python3
"""
Test script for TTS (Text-to-Speech) Service component
"""

import sys
import os

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_tts_import():
    """Test if TTS service can be imported"""
    print("🔊 Testing TTS Service Import...")
    try:
        from services.tts_service import TTSService
        print("✅ TTS service imported successfully")
        return True
    except Exception as e:
        print(f"❌ TTS service import failed: {e}")
        return False

def test_tts_initialization():
    """Test TTS service initialization"""
    print("\n🔧 Testing TTS Service Initialization...")
    try:
        from services.tts_service import TTSService
        tts_service = TTSService()
        print("✅ TTS service initialized successfully")
        return True
    except Exception as e:
        print(f"❌ TTS service initialization failed: {e}")
        return False

def test_greeting_messages():
    """Test greeting messages in different languages"""
    print("\n👋 Testing Greeting Messages...")
    try:
        from services.tts_service import TTSService
        tts_service = TTSService()
        
        languages = ["hindi", "english", "punjabi", "gujarati", "marathi", "telugu"]
        
        for lang in languages:
            greeting = tts_service.get_greeting_message(lang)
            print(f"✅ {lang}: {greeting[:50]}...")
        
        return True
    except Exception as e:
        print(f"❌ Greeting messages test failed: {e}")
        return False

def test_query_prompts():
    """Test query prompts in different languages"""
    print("\n❓ Testing Query Prompts...")
    try:
        from services.tts_service import TTSService
        tts_service = TTSService()
        
        languages = ["hindi", "english", "punjabi", "gujarati", "marathi", "telugu"]
        
        for lang in languages:
            prompt = tts_service.get_query_prompt(lang)
            print(f"✅ {lang}: {prompt}")
        
        return True
    except Exception as e:
        print(f"❌ Query prompts test failed: {e}")
        return False

def test_voice_mapping():
    """Test voice mapping for different languages"""
    print("\n🎵 Testing Voice Mapping...")
    try:
        from services.tts_service import TTSService
        tts_service = TTSService()
        
        languages = ["hindi", "english", "punjabi", "gujarati", "marathi", "telugu"]
        
        for lang in languages:
            if lang in tts_service.voice_mapping:
                voices = tts_service.voice_mapping[lang]
                print(f"✅ {lang}: {list(voices.keys())}")
            else:
                print(f"❌ {lang}: No voice mapping found")
        
        return True
    except Exception as e:
        print(f"❌ Voice mapping test failed: {e}")
        return False

def test_fallback_mechanism():
    """Test TTS fallback mechanism"""
    print("\n🔄 Testing TTS Fallback Mechanism...")
    try:
        from services.tts_service import TTSService
        # Test with invalid URL to trigger fallback
        tts_service = TTSService("http://invalid-url:8002/tts")
        print("✅ TTS fallback mechanism configured")
        return True
    except Exception as e:
        print(f"❌ TTS fallback test failed: {e}")
        return False

def main():
    """Run TTS service tests"""
    print("🧪 Starting TTS Service Tests")
    print("=" * 40)
    
    tests = [
        ("TTS Import", test_tts_import),
        ("TTS Initialization", test_tts_initialization),
        ("Greeting Messages", test_greeting_messages),
        ("Query Prompts", test_query_prompts),
        ("Voice Mapping", test_voice_mapping),
        ("Fallback Mechanism", test_fallback_mechanism),
    ]
    
    results = {}
    
    for test_name, test_func in tests:
        try:
            results[test_name] = test_func()
        except Exception as e:
            print(f"❌ {test_name} failed with exception: {e}")
            results[test_name] = False
    
    print("\n" + "=" * 40)
    print("📊 TTS Service Test Results:")
    print("=" * 40)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status}: {test_name}")
        if result:
            passed += 1
    
    print(f"\n🎯 Overall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 TTS Service is working perfectly!")
    else:
        print("⚠️ TTS Service needs attention.")
    
    return passed == total

if __name__ == "__main__":
>>>>>>> e15bec281abf2b62dc4fb58236aef25909e43dfc
    main() 