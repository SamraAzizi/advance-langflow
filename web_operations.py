from dotenv import load_dotenv
import os
import requests
from urllib.parse import quote_plus

load_dotenv()

def _make_api_request(url, **kwargs):
    api_key = os.getenv("BRIGHTDATA_API_KEY")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }