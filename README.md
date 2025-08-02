<<<<<<< HEAD
# 🌾 Farmer AI Assistant

A two-way conversational AI system for farmers that allows them to call a number, provide farm details, ask farming-related questions in Hinglish, and receive contextual voice replies — using only a basic phone call (no app required).

## 🎯 Project Goal

Enable farmers to access AI-powered farming advice through simple phone calls, making agricultural technology accessible to everyone, regardless of smartphone or internet availability.

## 🏗️ Architecture

```
Farmer calls → Twilio → FastAPI → STT → AI Model → TTS → Voice Response
```

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Voice Call (Telephony)** | Twilio |
| **STT (Speech-to-Text)** | Vakyansh STT + Google Speech Recognition (fallback) |
| **NLP / AI Reasoning** | Param-1-2.9B-Instruct by BharatGenAI |
| **TTS (Text-to-Speech)** | Vakyansh TTS + Edge TTS + gTTS (fallbacks) |
| **Server / Logic** | FastAPI (Python) |
| **Deployment** | Railway / Replit / Google Cloud Free Tier |

## 🌍 Multilingual Support

- **Hindi** (हिंदी)
- **English**
- **Punjabi** (ਪੰਜਾਬੀ)
- **Gujarati** (ગુજરાતી)
- **Marathi** (मराठी)
- **Telugu** (తెలుగు)
- **Tamil** (தமிழ்)
- **Kannada** (ಕನ್ನಡ)
- **Bengali** (বাংলা)
- **Odia** (ଓଡ଼ିଆ)
- **Assamese** (অসমীয়া)
- **Malayalam** (മലയാളം)

## 🗣️ Conversation Flow

1. **Farmer calls** `+1-218-219-9792`
2. **System greets**: "नमस्ते! कृपया अपनी खेती से जुड़ी कुछ जानकारी दें..."
3. **Farmer provides details**: "Haryana mein gehun ki kheti kar raha hun, paani ki kami hai"
4. **System extracts context**: Location=हरियाणा, Crop=wheat, Water=shortage
5. **System asks for query**: "अब अपना सवाल पूछिए।"
6. **Farmer asks question**: "पानी की कमी में क्या करें?"
7. **AI generates response**: Contextual farming advice
8. **System converts to speech** and plays back to farmer
9. **Repeat** for additional questions

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Git
- Twilio Account (for phone number)

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/farmer-ai-assistant.git
cd farmer-ai-assistant

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your Twilio credentials
```

### Configuration

Create a `.env` file with your credentials:

```env
# Twilio Configuration
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=+12182199792

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
```

### Running the Application

```bash
# Start the FastAPI server
python main.py

# Or using uvicorn
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## 🧪 Testing

### Run All Tests

```bash
# Basic functionality tests
python test_basic.py

# Individual component tests
python test_config.py
python test_stt.py
python test_tts.py
python test_ai_model.py
```

### Test Results

- ✅ **Configuration**: Working perfectly
- ✅ **STT Service**: Working perfectly
- ✅ **TTS Service**: Working perfectly
- ✅ **AI Model**: Working perfectly (with fallback)
- ⏳ **Telephony Service**: Ready for testing
- ⏳ **Main FastAPI App**: Ready for testing

## 📞 Twilio Setup

1. **Get a Twilio Phone Number**
   - Sign up at [Twilio Console](https://console.twilio.com/)
   - Purchase a phone number (US numbers work for international calls)

2. **Configure Webhook**
   - Go to Phone Numbers → Manage → Active numbers
   - Click on your phone number
   - Set Voice Webhook URL to: `https://your-deployed-domain.com/voice`
   - Set HTTP Method to: `POST`

3. **Deploy Your Application**
   - Deploy to Railway, Replit, or Google Cloud
   - Update the webhook URL with your public domain

## 🐳 Docker Deployment

```bash
# Build and run with Docker Compose
docker-compose up -d

# Or build manually
docker build -t farmer-ai-assistant .
docker run -p 8000:8000 farmer-ai-assistant
```

## 📁 Project Structure

```
farmer-ai-assistant/
├── main.py                 # FastAPI application
├── config.py              # Configuration management
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── .gitignore            # Git ignore rules
├── models/
│   └── ai_model.py       # Param AI model integration
├── services/
│   ├── stt_service.py    # Speech-to-Text service
│   ├── tts_service.py    # Text-to-Speech service
│   └── telephony_service.py # Twilio integration
├── deployment/
│   ├── Dockerfile        # Docker configuration
│   └── docker-compose.yml # Docker Compose setup
├── scripts/
│   └── setup.sh          # Automated setup script
└── tests/
    ├── test_basic.py     # Basic functionality tests
    ├── test_config.py    # Configuration tests
    ├── test_stt.py       # STT service tests
    ├── test_tts.py       # TTS service tests
    └── test_ai_model.py  # AI model tests
```

## 🔧 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Health check |
| `/voice` | POST | Handle incoming calls |
| `/process_context` | POST | Process farming context |
| `/process_query` | POST | Process farmer queries |
| `/webhook/twilio` | POST | Twilio webhook handler |
| `/health` | GET | Health status |
| `/stats` | GET | System statistics |

## 🤖 AI Prompt Design

The system uses contextual prompts like:

```
You are an expert agriculture advisor. Please respond in हिंदी.

Farmer Location: हरियाणा
Crop: wheat
Water Condition: shortage
Soil Type: loamy
Season: rabi

Farmer Query: "पानी की कमी में क्या करें?"

Give a clear, short, and practical answer in simple हिंदी that a farmer can easily understand and follow. Focus on:
1. Immediate actionable steps
2. Cost-effective solutions
3. Local availability of resources
4. Safety precautions

Answer:
```

## 🔄 Fallback Mechanisms

The system includes multiple fallback options:

- **STT Fallback**: Vakyansh STT → Google Speech Recognition
- **TTS Fallback**: Vakyansh TTS → Edge TTS → gTTS
- **AI Model Fallback**: Param-1-2.9B-Instruct → Rule-based responses

## 📊 Monitoring

- **Health Check**: `/health` endpoint
- **Statistics**: `/stats` endpoint
- **Logging**: Comprehensive logging throughout the application

## 🚀 Deployment Options

### 1. Railway (Recommended)
```bash
# Install Railway CLI
npm install -g @railway/cli

# Deploy
railway login
railway init
railway up
```

### 2. Replit
- Create new Python project
- Upload your code
- Set environment variables
- Deploy

### 3. Google Cloud Free Tier
- Create VM instance
- Install dependencies
- Deploy application
- Set up domain

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -am 'Add feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **BharatGenAI** for the Param-1-2.9B-Instruct model
- **Vakyansh** for STT/TTS services
- **Twilio** for telephony infrastructure
- **FastAPI** for the web framework

## 📞 Support

- **Phone Number**: `+1-218-219-9792`
- **Email**: support@farmer-ai-assistant.com
- **Issues**: [GitHub Issues](https://github.com/yourusername/farmer-ai-assistant/issues)

## 🌟 Features

- ✅ **Multilingual Support**: 12 Indian languages
- ✅ **Contextual AI**: Farm-specific advice
- ✅ **Fallback Mechanisms**: Multiple backup options
- ✅ **Voice Interface**: No app required
- ✅ **Scalable Architecture**: Ready for production
- ✅ **Comprehensive Testing**: Unit tests for all components
- ✅ **Docker Support**: Easy deployment
- ✅ **Documentation**: Complete setup guide

---

=======
# 🌾 Farmer AI Assistant

A two-way conversational AI system for farmers that allows them to call a number, provide farm details, ask farming-related questions in Hinglish, and receive contextual voice replies — using only a basic phone call (no app required).

## 🎯 Project Goal

Enable farmers to access AI-powered farming advice through simple phone calls, making agricultural technology accessible to everyone, regardless of smartphone or internet availability.

## 🏗️ Architecture

```
Farmer calls → Twilio → FastAPI → STT → AI Model → TTS → Voice Response
```

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Voice Call (Telephony)** | Twilio |
| **STT (Speech-to-Text)** | Vakyansh STT + Google Speech Recognition (fallback) |
| **NLP / AI Reasoning** | Param-1-2.9B-Instruct by BharatGenAI |
| **TTS (Text-to-Speech)** | Vakyansh TTS + Edge TTS + gTTS (fallbacks) |
| **Server / Logic** | FastAPI (Python) |
| **Deployment** | Railway / Replit / Google Cloud Free Tier |

## 🌍 Multilingual Support

- **Hindi** (हिंदी)
- **English**
- **Punjabi** (ਪੰਜਾਬੀ)
- **Gujarati** (ગુજરાતી)
- **Marathi** (मराठी)
- **Telugu** (తెలుగు)
- **Tamil** (தமிழ்)
- **Kannada** (ಕನ್ನಡ)
- **Bengali** (বাংলা)
- **Odia** (ଓଡ଼ିଆ)
- **Assamese** (অসমীয়া)
- **Malayalam** (മലയാളം)

## 🗣️ Conversation Flow

1. **Farmer calls** `+1-218-219-9792`
2. **System greets**: "नमस्ते! कृपया अपनी खेती से जुड़ी कुछ जानकारी दें..."
3. **Farmer provides details**: "Haryana mein gehun ki kheti kar raha hun, paani ki kami hai"
4. **System extracts context**: Location=हरियाणा, Crop=wheat, Water=shortage
5. **System asks for query**: "अब अपना सवाल पूछिए।"
6. **Farmer asks question**: "पानी की कमी में क्या करें?"
7. **AI generates response**: Contextual farming advice
8. **System converts to speech** and plays back to farmer
9. **Repeat** for additional questions

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Git
- Twilio Account (for phone number)

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/farmer-ai-assistant.git
cd farmer-ai-assistant

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your Twilio credentials
```

### Configuration

Create a `.env` file with your credentials:

```env
# Twilio Configuration
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=+12182199792

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
```

### Running the Application

```bash
# Start the FastAPI server
python main.py

# Or using uvicorn
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## 🧪 Testing

### Run All Tests

```bash
# Basic functionality tests
python test_basic.py

# Individual component tests
python test_config.py
python test_stt.py
python test_tts.py
python test_ai_model.py
```

### Test Results

- ✅ **Configuration**: Working perfectly
- ✅ **STT Service**: Working perfectly
- ✅ **TTS Service**: Working perfectly
- ✅ **AI Model**: Working perfectly (with fallback)
- ⏳ **Telephony Service**: Ready for testing
- ⏳ **Main FastAPI App**: Ready for testing

## 📞 Twilio Setup

1. **Get a Twilio Phone Number**
   - Sign up at [Twilio Console](https://console.twilio.com/)
   - Purchase a phone number (US numbers work for international calls)

2. **Configure Webhook**
   - Go to Phone Numbers → Manage → Active numbers
   - Click on your phone number
   - Set Voice Webhook URL to: `https://your-deployed-domain.com/voice`
   - Set HTTP Method to: `POST`

3. **Deploy Your Application**
   - Deploy to Railway, Replit, or Google Cloud
   - Update the webhook URL with your public domain

## 🐳 Docker Deployment

```bash
# Build and run with Docker Compose
docker-compose up -d

# Or build manually
docker build -t farmer-ai-assistant .
docker run -p 8000:8000 farmer-ai-assistant
```

## 📁 Project Structure

```
farmer-ai-assistant/
├── main.py                 # FastAPI application
├── config.py              # Configuration management
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── .gitignore            # Git ignore rules
├── models/
│   └── ai_model.py       # Param AI model integration
├── services/
│   ├── stt_service.py    # Speech-to-Text service
│   ├── tts_service.py    # Text-to-Speech service
│   └── telephony_service.py # Twilio integration
├── deployment/
│   ├── Dockerfile        # Docker configuration
│   └── docker-compose.yml # Docker Compose setup
├── scripts/
│   └── setup.sh          # Automated setup script
└── tests/
    ├── test_basic.py     # Basic functionality tests
    ├── test_config.py    # Configuration tests
    ├── test_stt.py       # STT service tests
    ├── test_tts.py       # TTS service tests
    └── test_ai_model.py  # AI model tests
```

## 🔧 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Health check |
| `/voice` | POST | Handle incoming calls |
| `/process_context` | POST | Process farming context |
| `/process_query` | POST | Process farmer queries |
| `/webhook/twilio` | POST | Twilio webhook handler |
| `/health` | GET | Health status |
| `/stats` | GET | System statistics |

## 🤖 AI Prompt Design

The system uses contextual prompts like:

```
You are an expert agriculture advisor. Please respond in हिंदी.

Farmer Location: हरियाणा
Crop: wheat
Water Condition: shortage
Soil Type: loamy
Season: rabi

Farmer Query: "पानी की कमी में क्या करें?"

Give a clear, short, and practical answer in simple हिंदी that a farmer can easily understand and follow. Focus on:
1. Immediate actionable steps
2. Cost-effective solutions
3. Local availability of resources
4. Safety precautions

Answer:
```

## 🔄 Fallback Mechanisms

The system includes multiple fallback options:

- **STT Fallback**: Vakyansh STT → Google Speech Recognition
- **TTS Fallback**: Vakyansh TTS → Edge TTS → gTTS
- **AI Model Fallback**: Param-1-2.9B-Instruct → Rule-based responses

## 📊 Monitoring

- **Health Check**: `/health` endpoint
- **Statistics**: `/stats` endpoint
- **Logging**: Comprehensive logging throughout the application

## 🚀 Deployment Options

### 1. Railway (Recommended)
```bash
# Install Railway CLI
npm install -g @railway/cli

# Deploy
railway login
railway init
railway up
```

### 2. Replit
- Create new Python project
- Upload your code
- Set environment variables
- Deploy

### 3. Google Cloud Free Tier
- Create VM instance
- Install dependencies
- Deploy application
- Set up domain

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -am 'Add feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **BharatGenAI** for the Param-1-2.9B-Instruct model
- **Vakyansh** for STT/TTS services
- **Twilio** for telephony infrastructure
- **FastAPI** for the web framework

## 📞 Support

- **Phone Number**: `+1-218-219-9792`
- **Email**: support@farmer-ai-assistant.com
- **Issues**: [GitHub Issues](https://github.com/yourusername/farmer-ai-assistant/issues)

## 🌟 Features

- ✅ **Multilingual Support**: 12 Indian languages
- ✅ **Contextual AI**: Farm-specific advice
- ✅ **Fallback Mechanisms**: Multiple backup options
- ✅ **Voice Interface**: No app required
- ✅ **Scalable Architecture**: Ready for production
- ✅ **Comprehensive Testing**: Unit tests for all components
- ✅ **Docker Support**: Easy deployment
- ✅ **Documentation**: Complete setup guide

---

>>>>>>> e15bec281abf2b62dc4fb58236aef25909e43dfc
**Made with ❤️ for Indian Farmers** 