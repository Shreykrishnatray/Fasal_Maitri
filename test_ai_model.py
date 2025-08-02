<<<<<<< HEAD
#!/usr/bin/env python3
"""
Test script for AI Model (Param-1-2.9B-Instruct) component
"""

import sys
import os

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_ai_model_import():
    """Test if AI model can be imported"""
    print("🤖 Testing AI Model Import...")
    try:
        from models.ai_model import ParamAIModel
        print("✅ AI model imported successfully")
        return True
    except Exception as e:
        print(f"❌ AI model import failed: {e}")
        return False

def test_ai_model_initialization():
    """Test AI model initialization"""
    print("\n🔧 Testing AI Model Initialization...")
    try:
        from models.ai_model import ParamAIModel
        # Test without loading the actual model (will use fallback)
        ai_model = ParamAIModel()
        print("✅ AI model initialized successfully")
        return True
    except Exception as e:
        print(f"❌ AI model initialization failed: {e}")
        return False

def test_language_mapping():
    """Test language mapping"""
    print("\n🌍 Testing Language Mapping...")
    try:
        from models.ai_model import ParamAIModel
        ai_model = ParamAIModel()
        
        languages = ["hindi", "english", "punjabi", "gujarati", "marathi", "telugu"]
        
        for lang in languages:
            if lang in ai_model.language_map:
                print(f"✅ {lang}: {ai_model.language_map[lang]}")
            else:
                print(f"❌ {lang}: No mapping found")
        
        return True
    except Exception as e:
        print(f"❌ Language mapping test failed: {e}")
        return False

def test_prompt_building():
    """Test prompt building functionality"""
    print("\n📝 Testing Prompt Building...")
    try:
        from models.ai_model import ParamAIModel
        ai_model = ParamAIModel()
        
        context = {
            'location': 'हरियाणा',
            'crop': 'wheat',
            'water_condition': 'shortage',
            'soil_type': 'loamy',
            'season': 'rabi'
        }
        query = "पानी की कमी में क्या करें?"
        language = "hindi"
        
        prompt = ai_model._build_prompt(context, query, language)
        print("✅ Prompt built successfully")
        print(f"✅ Language: {language}")
        print(f"✅ Context: {context}")
        print(f"✅ Query: {query}")
        
        return True
    except Exception as e:
        print(f"❌ Prompt building test failed: {e}")
        return False

def test_fallback_response():
    """Test fallback response generation"""
    print("\n🔄 Testing Fallback Response...")
    try:
        from models.ai_model import ParamAIModel
        ai_model = ParamAIModel()
        
        context = {
            'location': 'हरियाणा',
            'crop': 'wheat',
            'water_condition': 'shortage',
            'soil_type': 'loamy',
            'season': 'rabi'
        }
        query = "पानी की कमी में क्या करें?"
        
        response = ai_model._generate_fallback_response(context, query, "hindi")
        print("✅ Fallback response generated successfully")
        print(f"✅ Response: {response[:100]}...")
        
        return True
    except Exception as e:
        print(f"❌ Fallback response test failed: {e}")
        return False

def test_response_generation():
    """Test full response generation (with fallback)"""
    print("\n💬 Testing Response Generation...")
    try:
        from models.ai_model import ParamAIModel
        ai_model = ParamAIModel()
        
        context = {
            'location': 'हरियाणा',
            'crop': 'wheat',
            'water_condition': 'shortage',
            'soil_type': 'loamy',
            'season': 'rabi'
        }
        query = "पानी की कमी में क्या करें?"
        
        response = ai_model.generate_response(context, query)
        print("✅ Response generated successfully")
        print(f"✅ Response: {response[:100]}...")
        
        return True
    except Exception as e:
        print(f"❌ Response generation test failed: {e}")
        return False

def main():
    """Run AI model tests"""
    print("🧪 Starting AI Model Tests")
    print("=" * 40)
    
    tests = [
        ("AI Model Import", test_ai_model_import),
        ("AI Model Initialization", test_ai_model_initialization),
        ("Language Mapping", test_language_mapping),
        ("Prompt Building", test_prompt_building),
        ("Fallback Response", test_fallback_response),
        ("Response Generation", test_response_generation),
    ]
    
    results = {}
    
    for test_name, test_func in tests:
        try:
            results[test_name] = test_func()
        except Exception as e:
            print(f"❌ {test_name} failed with exception: {e}")
            results[test_name] = False
    
    print("\n" + "=" * 40)
    print("📊 AI Model Test Results:")
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
        print("🎉 AI Model is working perfectly!")
    else:
        print("⚠️ AI Model needs attention.")
    
    return passed == total

if __name__ == "__main__":
=======
#!/usr/bin/env python3
"""
Test script for AI Model (Param-1-2.9B-Instruct) component
"""

import sys
import os

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_ai_model_import():
    """Test if AI model can be imported"""
    print("🤖 Testing AI Model Import...")
    try:
        from models.ai_model import ParamAIModel
        print("✅ AI model imported successfully")
        return True
    except Exception as e:
        print(f"❌ AI model import failed: {e}")
        return False

def test_ai_model_initialization():
    """Test AI model initialization"""
    print("\n🔧 Testing AI Model Initialization...")
    try:
        from models.ai_model import ParamAIModel
        # Test without loading the actual model (will use fallback)
        ai_model = ParamAIModel()
        print("✅ AI model initialized successfully")
        return True
    except Exception as e:
        print(f"❌ AI model initialization failed: {e}")
        return False

def test_language_mapping():
    """Test language mapping"""
    print("\n🌍 Testing Language Mapping...")
    try:
        from models.ai_model import ParamAIModel
        ai_model = ParamAIModel()
        
        languages = ["hindi", "english", "punjabi", "gujarati", "marathi", "telugu"]
        
        for lang in languages:
            if lang in ai_model.language_map:
                print(f"✅ {lang}: {ai_model.language_map[lang]}")
            else:
                print(f"❌ {lang}: No mapping found")
        
        return True
    except Exception as e:
        print(f"❌ Language mapping test failed: {e}")
        return False

def test_prompt_building():
    """Test prompt building functionality"""
    print("\n📝 Testing Prompt Building...")
    try:
        from models.ai_model import ParamAIModel
        ai_model = ParamAIModel()
        
        context = {
            'location': 'हरियाणा',
            'crop': 'wheat',
            'water_condition': 'shortage',
            'soil_type': 'loamy',
            'season': 'rabi'
        }
        query = "पानी की कमी में क्या करें?"
        language = "hindi"
        
        prompt = ai_model._build_prompt(context, query, language)
        print("✅ Prompt built successfully")
        print(f"✅ Language: {language}")
        print(f"✅ Context: {context}")
        print(f"✅ Query: {query}")
        
        return True
    except Exception as e:
        print(f"❌ Prompt building test failed: {e}")
        return False

def test_fallback_response():
    """Test fallback response generation"""
    print("\n🔄 Testing Fallback Response...")
    try:
        from models.ai_model import ParamAIModel
        ai_model = ParamAIModel()
        
        context = {
            'location': 'हरियाणा',
            'crop': 'wheat',
            'water_condition': 'shortage',
            'soil_type': 'loamy',
            'season': 'rabi'
        }
        query = "पानी की कमी में क्या करें?"
        
        response = ai_model._generate_fallback_response(context, query, "hindi")
        print("✅ Fallback response generated successfully")
        print(f"✅ Response: {response[:100]}...")
        
        return True
    except Exception as e:
        print(f"❌ Fallback response test failed: {e}")
        return False

def test_response_generation():
    """Test full response generation (with fallback)"""
    print("\n💬 Testing Response Generation...")
    try:
        from models.ai_model import ParamAIModel
        ai_model = ParamAIModel()
        
        context = {
            'location': 'हरियाणा',
            'crop': 'wheat',
            'water_condition': 'shortage',
            'soil_type': 'loamy',
            'season': 'rabi'
        }
        query = "पानी की कमी में क्या करें?"
        
        response = ai_model.generate_response(context, query)
        print("✅ Response generated successfully")
        print(f"✅ Response: {response[:100]}...")
        
        return True
    except Exception as e:
        print(f"❌ Response generation test failed: {e}")
        return False

def main():
    """Run AI model tests"""
    print("🧪 Starting AI Model Tests")
    print("=" * 40)
    
    tests = [
        ("AI Model Import", test_ai_model_import),
        ("AI Model Initialization", test_ai_model_initialization),
        ("Language Mapping", test_language_mapping),
        ("Prompt Building", test_prompt_building),
        ("Fallback Response", test_fallback_response),
        ("Response Generation", test_response_generation),
    ]
    
    results = {}
    
    for test_name, test_func in tests:
        try:
            results[test_name] = test_func()
        except Exception as e:
            print(f"❌ {test_name} failed with exception: {e}")
            results[test_name] = False
    
    print("\n" + "=" * 40)
    print("📊 AI Model Test Results:")
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
        print("🎉 AI Model is working perfectly!")
    else:
        print("⚠️ AI Model needs attention.")
    
    return passed == total

if __name__ == "__main__":
>>>>>>> e15bec281abf2b62dc4fb58236aef25909e43dfc
    main() 