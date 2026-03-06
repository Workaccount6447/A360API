import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Telegram Configuration
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
TELE_ID = os.getenv("TELE_ID")
TELE_HASH = os.getenv("TELE_HASH")

# AI API Keys
IMGAI_API_KEY = os.getenv("IMGAI_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Services & Database
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
BASE_URL = os.getenv("BASE_URL")
MONGO_URL = os.getenv("MONGO_URL")

# Example usage:
# print(f"Bot Token loaded: {BOT_TOKEN[:5]}***")
