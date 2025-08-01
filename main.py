from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import Response, PlainTextResponse
import logging
import json
from typing import Dict, Any
import uvicorn

from config import Config
from models.ai_model import ParamAIModel
from services.stt_service import STTService
from services.tts_service import TTSService
from services.telephony_service import TelephonyService

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(title="Farmer AI Assistant", version="1.0.0")

# Initialize services
config = Config()
ai_model = ParamAIModel(config.PARAM_MODEL_PATH, config.DEVICE)
stt_service = STTService(config.VAKYANSH_STT_URL)
tts_service = TTSService(config.VAKYANSH_TTS_URL)
telephony_service = TelephonyService(config)

# In-memory storage for conversation context (in production, use Redis or database)
conversation_contexts = {}

@app.get("/")
async def root():
    return {"message": "Farmer AI Assistant API", "status": "running"}

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
            "language": "hindi"  # Default language
        }
        
        # Create greeting response
        response = telephony_service.create_greeting_response("hindi")
        
        return Response(content=response, media_type="application/xml")
        
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
        confidence = form_data.get("Confidence", "0")
        
        logger.info(f"Processing context for call {call_sid}: {speech_result}")
        
        if not call_sid or call_sid not in conversation_contexts:
            raise HTTPException(status_code=400, detail="Invalid call session")
        
        # Extract farming context from speech
        context = stt_service.extract_farming_context(speech_result)
        
        # Update conversation context
        conversation_contexts[call_sid]["context"] = context
        
        logger.info(f"Extracted context: {context}")
        
        # Create response asking for query
        response = telephony_service.create_query_response("hindi")
        
        return Response(content=response, media_type="application/xml")
        
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
        confidence = form_data.get("Confidence", "0")
        
        logger.info(f"Processing query for call {call_sid}: {speech_result}")
        
        if not call_sid or call_sid not in conversation_contexts:
            raise HTTPException(status_code=400, detail="Invalid call session")
        
        conversation = conversation_contexts[call_sid]
        context = conversation["context"]
        language = conversation["language"]
        
        # Check if user wants to end call
        if any(word in speech_result.lower() for word in ["नहीं", "no", "बंद", "end", "खत्म"]):
            # End call response
            end_response = """<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say>धन्यवाद! आपकी कॉल समाप्त हो रही है।</Say>
    <Hangup/>
</Response>"""
            return Response(content=end_response, media_type="application/xml")
        
        # Generate AI response
        ai_response = ai_model.generate_response(context, speech_result)
        
        logger.info(f"AI Response: {ai_response}")
        
        # Create response with AI answer
        response = telephony_service.create_ai_response(ai_response, language)
        
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

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "services": {
            "ai_model": ai_model.model is not None,
            "stt_service": True,
            "tts_service": True,
            "telephony_service": telephony_service.twilio_client is not None
        }
    }

@app.get("/stats")
async def get_stats():
    """Get conversation statistics"""
    return {
        "active_conversations": len(conversation_contexts),
        "total_contexts": len(conversation_contexts)
    }

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=config.HOST,
        port=config.PORT,
        reload=config.DEBUG
    ) 