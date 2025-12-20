import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Application settings
    DEBUG = True
    PORT = 5000
    
    # Mode selection: 'demo' or 'live'
    # Change this to 'live' when you have API keys
    APP_MODE = os.getenv('APP_MODE', 'demo')
    
    # API Keys (will be loaded from .env file)
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')
    ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY', '')
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY', '')
    HUGGINGFACE_API_KEY = os.getenv('HUGGINGFACE_API_KEY', '')
    NEWS_API_KEY = os.getenv("NEWS_API_KEY")
    NEWS_API_URL = "https://newsapi.org/v2/everything"
    NEWS_SOURCES = "techcrunch,wired,the-verge,engadget,ars-technica"
    # Model configurations
    MODELS_CONFIG = {
        "GPT-4": {
            "enabled": bool(OPENAI_API_KEY),
            "api_key": OPENAI_API_KEY,
            "endpoint": "https://api.openai.com/v1/chat/completions",
            "model_id": "gpt-4"
        },
        "Claude-3": {
            "enabled": bool(ANTHROPIC_API_KEY),
            "api_key": ANTHROPIC_API_KEY,
            "endpoint": "https://api.anthropic.com/v1/messages",
            "model_id": "claude-3-sonnet-20240229"
        },
        "Gemini Pro": {
            "enabled": bool(GOOGLE_API_KEY),
            "api_key": GOOGLE_API_KEY,
            "endpoint": "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent",
            "model_id": "gemini-pro"
        },
        "Llama-3-70B": {
            "enabled": bool(HUGGINGFACE_API_KEY),
            "api_key": HUGGINGFACE_API_KEY,
            "endpoint": "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-70B-Instruct",
            "model_id": "meta-llama/Meta-Llama-3-70B-Instruct"
        },
        "Mistral-7B": {
            "enabled": bool(HUGGINGFACE_API_KEY),
            "api_key": HUGGINGFACE_API_KEY,
            "endpoint": "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2",
            "model_id": "mistralai/Mistral-7B-Instruct-v0.2"
        },
        "Phi-3": {
            "enabled": bool(HUGGINGFACE_API_KEY),
            "api_key": HUGGINGFACE_API_KEY,
            "endpoint": "https://api-inference.huggingface.co/models/microsoft/Phi-3-mini-4k-instruct",
            "model_id": "microsoft/Phi-3-mini-4k-instruct"
        }
    }