#!/usr/bin/env python3
"""
Test script for Configuration component
"""

import sys
import os

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_config_import():
    """Test if config.py can be imported"""
    print("🔧 Testing Configuration Import...")
    try:
        from config import Config
        print("✅ Config module imported successfully")
        return True
    except Exception as e:
        print(f"❌ Config import failed: {e}")
        return False

def test_config_loading():
    """Test configuration loading"""
    print("\n⚙️ Testing Configuration Loading...")
    try:
        from config import Config
        config = Config()
        
        print("✅ Configuration loaded successfully")
        print(f"✅ Twilio Account SID: {config.TWILIO_ACCOUNT_SID[:10]}...")
        print(f"✅ Twilio Phone Number: {config.TWILIO_PHONE_NUMBER}")
        print(f"✅ AI Model Path: {config.PARAM_MODEL_PATH}")
        print(f"✅ STT URL: {config.VAKYANSH_STT_URL}")
        print(f"✅ TTS URL: {config.VAKYANSH_TTS_URL}")
        print(f"✅ Server Host: {config.HOST}")
        print(f"✅ Server Port: {config.PORT}")
        
        return True
    except Exception as e:
        print(f"❌ Configuration loading failed: {e}")
        return False

def test_twilio_credentials():
    """Test Twilio credentials"""
    print("\n📞 Testing Twilio Credentials...")
    try:
        from config import Config
        config = Config()
        
        # Check if credentials are set
        if config.TWILIO_ACCOUNT_SID and config.TWILIO_AUTH_TOKEN:
            print("✅ Twilio credentials are configured")
            print(f"✅ Account SID: {config.TWILIO_ACCOUNT_SID[:10]}...")
            print(f"✅ Phone Number: {config.TWILIO_PHONE_NUMBER}")
            return True
        else:
            print("❌ Twilio credentials are missing")
            return False
    except Exception as e:
        print(f"❌ Twilio credentials test failed: {e}")
        return False

def main():
    """Run configuration tests"""
    print("🧪 Starting Configuration Tests")
    print("=" * 40)
    
    tests = [
        ("Config Import", test_config_import),
        ("Config Loading", test_config_loading),
        ("Twilio Credentials", test_twilio_credentials),
    ]
    
    results = {}
    
    for test_name, test_func in tests:
        try:
            results[test_name] = test_func()
        except Exception as e:
            print(f"❌ {test_name} failed with exception: {e}")
            results[test_name] = False
    
    print("\n" + "=" * 40)
    print("📊 Configuration Test Results:")
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
        print("🎉 Configuration is working perfectly!")
    else:
        print("⚠️ Configuration needs attention.")
    
    return passed == total

if __name__ == "__main__":
    main() 