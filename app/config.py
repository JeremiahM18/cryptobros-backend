# app/config.py
import os
from dotenv import load_dotenv

# Load .env when running locally
load_dotenv()

COINGECKO_API_KEY = os.getenv("COINGECKO_API_KEY")
COINGECKO_BASE_URL = os.getenv("COINGECKO_BASE_URL", "https://api.coingecko.com/api/v3")

if COINGECKO_API_KEY is None:
    raise RuntimeError("COINGECKO_API_KEY is not set. Check your .env or environment vars.")