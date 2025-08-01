#!/bin/bash

# Farmer AI Assistant Setup Script
echo "🌾 Setting up Farmer AI Assistant..."

# Check if Python 3.9+ is installed
python_version=$(python3 --version 2>&1 | awk '{print $2}' | cut -d. -f1,2)
required_version="3.9"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then
    echo "❌ Python 3.9 or higher is required. Current version: $python_version"
    exit 1
fi

echo "✅ Python version check passed: $python_version"

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Upgrade pip
echo "⬆️ Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "📚 Installing dependencies..."
pip install -r requirements.txt

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p models
mkdir -p logs
mkdir -p data

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "⚙️ Creating .env file..."
    cat > .env << EOF
# Twilio Configuration
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone_number

# AI Model Configuration
PARAM_MODEL_PATH=./models/param-1-2.9b-instruct
DEVICE=cpu

# STT/TTS Configuration
VAKYANSH_STT_URL=http://localhost:8001/stt
VAKYANSH_TTS_URL=http://localhost:8002/tts

# Server Configuration
HOST=0.0.0.0
PORT=8000
DEBUG=True
EOF
    echo "⚠️ Please update .env file with your actual credentials"
fi

# Download model (if available)
echo "🤖 Checking for AI model..."
if [ ! -d "models/param-1-2.9b-instruct" ]; then
    echo "⚠️ AI model not found. Please download Param-1-2.9B-Instruct model and place it in models/param-1-2.9b-instruct/"
    echo "📥 You can get the model from BharatGenAI"
fi

# Create startup script
echo "🚀 Creating startup script..."
cat > start.sh << 'EOF'
#!/bin/bash
source venv/bin/activate
python main.py
EOF
chmod +x start.sh

# Create test script
echo "🧪 Creating test script..."
cat > test.py << 'EOF'
#!/usr/bin/env python3
import requests
import json

def test_health():
    try:
        response = requests.get("http://localhost:8000/health")
        if response.status_code == 200:
            print("✅ Health check passed")
            print(json.dumps(response.json(), indent=2))
        else:
            print("❌ Health check failed")
    except Exception as e:
        print(f"❌ Health check error: {e}")

def test_stats():
    try:
        response = requests.get("http://localhost:8000/stats")
        if response.status_code == 200:
            print("✅ Stats endpoint working")
            print(json.dumps(response.json(), indent=2))
        else:
            print("❌ Stats endpoint failed")
    except Exception as e:
        print(f"❌ Stats error: {e}")

if __name__ == "__main__":
    print("🧪 Testing Farmer AI Assistant...")
    test_health()
    test_stats()
EOF

echo "✅ Setup completed successfully!"
echo ""
echo "📋 Next steps:"
echo "1. Update .env file with your Twilio credentials"
echo "2. Download the Param AI model to models/param-1-2.9b-instruct/"
echo "3. Run: ./start.sh"
echo "4. Test with: python test.py"
echo ""
echo "🌐 For deployment:"
echo "- Railway: Connect your GitHub repo"
echo "- Google Cloud: Use deployment/docker-compose.yml"
echo "- Local testing: Use ngrok for webhook testing"
echo ""
echo "�� Happy farming! 🚜" 