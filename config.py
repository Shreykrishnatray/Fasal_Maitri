<<<<<<< HEAD
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Twilio Configuration
    TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID", "ACf7af130b09bf922ff53a778a761693d3")
    TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN", "9beeb37b1b08ba34ce08d0326db9a2bb")
    TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER", "+12182199792")
    
    # Exotel Configuration
    EXOTEL_API_KEY = os.getenv("EXOTEL_API_KEY", "")
    EXOTEL_API_SECRET = os.getenv("EXOTEL_API_SECRET", "")
    EXOTEL_SID = os.getenv("EXOTEL_SID", "")
    
    # AI Model Configuration
    PARAM_MODEL_PATH = os.getenv("PARAM_MODEL_PATH", "./models/param-1-2.9b-instruct")
    DEVICE = os.getenv("DEVICE", "cpu")
    
    # STT/TTS Configuration
    VAKYANSH_STT_URL = os.getenv("VAKYANSH_STT_URL", "https://asr-api.open-speech-ekstep.frappe.cloud/v1/inference")
    VAKYANSH_TTS_URL = os.getenv("VAKYANSH_TTS_URL", "https://tts-api.open-speech-ekstep.frappe.cloud/v1/inference")
    
    # Server Configuration
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 8000))
=======
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Twilio Configuration
    TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID", "ACf7af130b09bf922ff53a778a761693d3")
    TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN", "9beeb37b1b08ba34ce08d0326db9a2bb")
    TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER", "+12182199792")
    
    # Exotel Configuration
    EXOTEL_API_KEY = os.getenv("EXOTEL_API_KEY", "")
    EXOTEL_API_SECRET = os.getenv("EXOTEL_API_SECRET", "")
    EXOTEL_SID = os.getenv("EXOTEL_SID", "")
    
    # AI Model Configuration
    PARAM_MODEL_PATH = os.getenv("PARAM_MODEL_PATH", "./models/param-1-2.9b-instruct")
    DEVICE = os.getenv("DEVICE", "cpu")
    
    # STT/TTS Configuration
    VAKYANSH_STT_URL = os.getenv("VAKYANSH_STT_URL", "https://asr-api.open-speech-ekstep.frappe.cloud/v1/inference")
    VAKYANSH_TTS_URL = os.getenv("VAKYANSH_TTS_URL", "https://tts-api.open-speech-ekstep.frappe.cloud/v1/inference")
    
    # Server Configuration
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 8000))
>>>>>>> e15bec281abf2b62dc4fb58236aef25909e43dfc
    DEBUG = os.getenv("DEBUG", "True").lower() == "true" 