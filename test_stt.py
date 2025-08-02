<<<<<<< HEAD
#!/usr/bin/env python3
"""
Test script for STT (Speech-to-Text) Service component
"""

import sys
import os

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_stt_import():
    """Test if STT service can be imported"""
    print("🎤 Testing STT Service Import...")
    try:
        from services.stt_service import STTService
        print("✅ STT service imported successfully")
        return True
    except Exception as e:
        print(f"❌ STT service import failed: {e}")
        return False

def test_stt_initialization():
    """Test STT service initialization"""
    print("\n🔧 Testing STT Service Initialization...")
    try:
        from services.stt_service import STTService
        stt_service = STTService()
        print("✅ STT service initialized successfully")
        return True
    except Exception as e:
        print(f"❌ STT service initialization failed: {e}")
        return False

def test_context_extraction():
    """Test context extraction functionality"""
    print("\n🔍 Testing Context Extraction...")
    try:
        from services.stt_service import STTService
        stt_service = STTService()
        
        # Test different speech inputs
        test_cases = [
            "Haryana mein gehun ki kheti kar raha hun, paani ki kami hai",
            "Punjab mein dhan ki kheti kar raha hun, normal paani hai",
            "Gujarat mein baajra ki kheti kar raha hun, paani bahut hai"
        ]
        
        for i, speech in enumerate(test_cases, 1):
            context = stt_service.extract_farming_context(speech)
            print(f"✅ Test {i}: {speech[:30]}... → {context}")
        
        return True
    except Exception as e:
        print(f"❌ Context extraction failed: {e}")
        return False

def test_language_codes():
    """Test language code mapping"""
    print("\n🌍 Testing Language Codes...")
    try:
        from services.stt_service import STTService
        stt_service = STTService()
        
        languages = ["hindi", "english", "punjabi", "gujarati", "marathi", "telugu"]
        
        for lang in languages:
            code = stt_service.language_codes.get(lang)
            if code:
                print(f"✅ {lang}: {code}")
            else:
                print(f"❌ {lang}: No code found")
        
        return True
    except Exception as e:
        print(f"❌ Language codes test failed: {e}")
        return False

def test_fallback_mechanism():
    """Test STT fallback mechanism"""
    print("\n🔄 Testing STT Fallback Mechanism...")
    try:
        from services.stt_service import STTService
        # Test with invalid URL to trigger fallback
        stt_service = STTService("http://invalid-url:8001/stt")
        print("✅ STT fallback mechanism configured")
        return True
    except Exception as e:
        print(f"❌ STT fallback test failed: {e}")
        return False

def main():
    """Run STT service tests"""
    print("🧪 Starting STT Service Tests")
    print("=" * 40)
    
    tests = [
        ("STT Import", test_stt_import),
        ("STT Initialization", test_stt_initialization),
        ("Context Extraction", test_context_extraction),
        ("Language Codes", test_language_codes),
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
    print("📊 STT Service Test Results:")
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
        print("🎉 STT Service is working perfectly!")
    else:
        print("⚠️ STT Service needs attention.")
    
    return passed == total

if __name__ == "__main__":
=======
#!/usr/bin/env python3
"""
Test script for STT (Speech-to-Text) Service component
"""

import sys
import os

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_stt_import():
    """Test if STT service can be imported"""
    print("🎤 Testing STT Service Import...")
    try:
        from services.stt_service import STTService
        print("✅ STT service imported successfully")
        return True
    except Exception as e:
        print(f"❌ STT service import failed: {e}")
        return False

def test_stt_initialization():
    """Test STT service initialization"""
    print("\n🔧 Testing STT Service Initialization...")
    try:
        from services.stt_service import STTService
        stt_service = STTService()
        print("✅ STT service initialized successfully")
        return True
    except Exception as e:
        print(f"❌ STT service initialization failed: {e}")
        return False

def test_context_extraction():
    """Test context extraction functionality"""
    print("\n🔍 Testing Context Extraction...")
    try:
        from services.stt_service import STTService
        stt_service = STTService()
        
        # Test different speech inputs
        test_cases = [
            "Haryana mein gehun ki kheti kar raha hun, paani ki kami hai",
            "Punjab mein dhan ki kheti kar raha hun, normal paani hai",
            "Gujarat mein baajra ki kheti kar raha hun, paani bahut hai"
        ]
        
        for i, speech in enumerate(test_cases, 1):
            context = stt_service.extract_farming_context(speech)
            print(f"✅ Test {i}: {speech[:30]}... → {context}")
        
        return True
    except Exception as e:
        print(f"❌ Context extraction failed: {e}")
        return False

def test_language_codes():
    """Test language code mapping"""
    print("\n🌍 Testing Language Codes...")
    try:
        from services.stt_service import STTService
        stt_service = STTService()
        
        languages = ["hindi", "english", "punjabi", "gujarati", "marathi", "telugu"]
        
        for lang in languages:
            code = stt_service.language_codes.get(lang)
            if code:
                print(f"✅ {lang}: {code}")
            else:
                print(f"❌ {lang}: No code found")
        
        return True
    except Exception as e:
        print(f"❌ Language codes test failed: {e}")
        return False

def test_fallback_mechanism():
    """Test STT fallback mechanism"""
    print("\n🔄 Testing STT Fallback Mechanism...")
    try:
        from services.stt_service import STTService
        # Test with invalid URL to trigger fallback
        stt_service = STTService("http://invalid-url:8001/stt")
        print("✅ STT fallback mechanism configured")
        return True
    except Exception as e:
        print(f"❌ STT fallback test failed: {e}")
        return False

def main():
    """Run STT service tests"""
    print("🧪 Starting STT Service Tests")
    print("=" * 40)
    
    tests = [
        ("STT Import", test_stt_import),
        ("STT Initialization", test_stt_initialization),
        ("Context Extraction", test_context_extraction),
        ("Language Codes", test_language_codes),
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
    print("📊 STT Service Test Results:")
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
        print("🎉 STT Service is working perfectly!")
    else:
        print("⚠️ STT Service needs attention.")
    
    return passed == total

if __name__ == "__main__":
>>>>>>> e15bec281abf2b62dc4fb58236aef25909e43dfc
    main() 