import os
from dotenv import load_dotenv

MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017/")
# Load environment variables from .env file
load_dotenv()

# OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")