from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import Response, PlainTextResponse
import logging
import json
from typing import Dict, Any
import uvicorn
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(title="Farmer AI Assistant", version="1.0.0")

# Try to import services, with fallbacks
try:
    from config import Config
    config = Config()
    logger.info("Config imported successfully")
except Exception as e:
    logger.warning(f"Config import failed: {e}")
    # Create basic config
    class BasicConfig:
        TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID", "")
        TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN", "")
        TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER", "+12182199792")
        VAKYANSH_STT_URL = os.getenv("VAKYANSH_STT_URL", "https://asr-api.open-speech-ekstep.frappe.cloud/v1/inference")
        VAKYANSH_TTS_URL = os.getenv("VAKYANSH_TTS_URL", "https://tts-api.open-speech-ekstep.frappe.cloud/v1/inference")
    config = BasicConfig()
    logger.info("Using BasicConfig")

try:
    from models.ai_model_railway import RailwayAIModel
    ai_model = RailwayAIModel()
    logger.info("AI Model imported successfully")
except Exception as e:
    logger.warning(f"AI model import failed: {e}")
    ai_model = None

try:
    from services.stt_service import STTService
    stt_service = STTService(config.VAKYANSH_STT_URL)
    logger.info("STT Service imported successfully")
except Exception as e:
    logger.warning(f"STT service import failed: {e}")
    stt_service = None

try:
    from services.tts_service import TTSService
    tts_service = TTSService(config.VAKYANSH_TTS_URL)
    logger.info("TTS Service imported successfully")
except Exception as e:
    logger.warning(f"TTS service import failed: {e}")
    tts_service = None

try:
    from services.telephony_service import TelephonyService
    telephony_service = TelephonyService(config)
    logger.info("Telephony Service imported successfully")
except Exception as e:
    logger.warning(f"Telephony service import failed: {e}")
    telephony_service = None

# In-memory storage for conversation context
conversation_contexts = {}

@app.get("/")
async def root():
    return {
        "message": "Farmer AI Assistant API", 
        "status": "running", 
        "deployment": "railway",
        "note": "Your app is working! Check Railway dashboard for URL."
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "deployment": "railway",
        "services": {
            "ai_model": ai_model is not None,
            "stt_service": stt_service is not None,
            "tts_service": tts_service is not None,
            "telephony_service": telephony_service is not None
        },
        "note": "App is running successfully on Railway"
    }

@app.get("/test")
async def test_endpoint():
    """Test endpoint for Railway"""
    return {
        "message": "Railway deployment test successful!",
        "timestamp": "2024-01-01T00:00:00Z",
        "status": "working"
    }

@app.get("/url")
async def get_url():
    """Get the current URL for debugging"""
    return {
        "message": "Your Railway URL",
        "note": "Check your Railway dashboard for the actual URL",
        "status": "running",
        "instructions": "Go to railway.app → Your Project → Deployments → Copy URL"
    }

@app.post("/voice")
async def handle_incoming_call(request: Request):
    """Handle incoming call - initial greeting"""
    try:
        # Get call details from Twilio
        form_data = await request.form()
        call_sid = form_data.get("CallSid")
        from_number = form_data.get("From")
        
        logger.info(f"New call from {from_number}, SID: {call_sid}")
        
        # Initialize conversation context
        conversation_contexts[call_sid] = {
            "from_number": from_number,
            "context": {},
            "language": "hindi"
        }
        
        # Simple greeting response
        greeting_response = """<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say>नमस्ते! कृपया अपनी खेती से जुड़ी कुछ जानकारी दें।</Say>
    <Gather input="speech" action="/process_context" method="POST" language="hi-IN" speechTimeout="5">
        <Say>बोलिए...</Say>
    </Gather>
</Response>"""
        
        return Response(content=greeting_response, media_type="application/xml")
        
    except Exception as e:
        logger.error(f"Error handling incoming call: {e}")
        return Response(content="<Response><Say>Sorry, there was an error.</Say></Response>", media_type="application/xml")

@app.post("/process_context")
async def process_farming_context(request: Request):
    """Process farmer's farming details"""
    try:
        form_data = await request.form()
        call_sid = form_data.get("CallSid")
        speech_result = form_data.get("SpeechResult", "")
        
        logger.info(f"Processing context for call {call_sid}: {speech_result}")
        
        if not call_sid or call_sid not in conversation_contexts:
            raise HTTPException(status_code=400, detail="Invalid call session")
        
        # Simple context extraction
        context = {"crop": "wheat", "location": "Haryana", "water_condition": "shortage"}
        conversation_contexts[call_sid]["context"] = context
        
        # Ask for query
        query_response = """<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say>अब अपना सवाल पूछिए।</Say>
    <Gather input="speech" action="/process_query" method="POST" language="hi-IN" speechTimeout="5">
        <Say>बोलिए...</Say>
    </Gather>
</Response>"""
        
        return Response(content=query_response, media_type="application/xml")
        
    except Exception as e:
        logger.error(f"Error processing context: {e}")
        return Response(content="<Response><Say>Sorry, there was an error.</Say></Response>", media_type="application/xml")

@app.post("/process_query")
async def process_farmer_query(request: Request):
    """Process farmer's question and generate AI response"""
    try:
        form_data = await request.form()
        call_sid = form_data.get("CallSid")
        speech_result = form_data.get("SpeechResult", "")
        
        logger.info(f"Processing query for call {call_sid}: {speech_result}")
        
        if not call_sid or call_sid not in conversation_contexts:
            raise HTTPException(status_code=400, detail="Invalid call session")
        
        # Check if user wants to end call
        if any(word in speech_result.lower() for word in ["नहीं", "no", "बंद", "end", "खत्म"]):
            end_response = """<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say>धन्यवाद! आपकी कॉल समाप्त हो रही है।</Say>
    <Hangup/>
</Response>"""
            return Response(content=end_response, media_type="application/xml")
        
        # Generate simple response
        ai_response = "पानी की कमी में, ड्रिप इरिगेशन का उपयोग करें। सुबह या शाम को पानी दें।"
        
        # Create response with AI answer
        response = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say>{ai_response}</Say>
    <Gather input="speech" action="/process_query" method="POST" language="hi-IN" speechTimeout="5">
        <Say>और कोई सवाल है?</Say>
    </Gather>
</Response>"""
        
        return Response(content=response, media_type="application/xml")
        
    except Exception as e:
        logger.error(f"Error processing query: {e}")
        return Response(content="<Response><Say>Sorry, there was an error.</Say></Response>", media_type="application/xml")

@app.post("/webhook/twilio")
async def twilio_webhook(request: Request):
    """Handle Twilio webhook events"""
    try:
        form_data = await request.form()
        event_type = form_data.get("EventType")
        call_sid = form_data.get("CallSid")
        
        logger.info(f"Twilio webhook: {event_type} for call {call_sid}")
        
        if event_type == "call-completed":
            # Clean up conversation context
            if call_sid in conversation_contexts:
                del conversation_contexts[call_sid]
                logger.info(f"Cleaned up context for call {call_sid}")
        
        return {"status": "ok"}
        
    except Exception as e:
        logger.error(f"Error handling Twilio webhook: {e}")
        return {"status": "error", "message": str(e)}

@app.get("/stats")
async def get_stats():
    """Get conversation statistics"""
    return {
        "active_conversations": len(conversation_contexts),
        "total_contexts": len(conversation_contexts),
        "deployment": "railway"
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(
        "main_railway:app",
        host="0.0.0.0",
        port=port,
        reload=False
    ) 