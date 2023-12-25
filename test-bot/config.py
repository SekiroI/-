import os
from dotenv import load_dotenv

env = None
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    env = load_dotenv(dotenv_path)

API_TOKEN = os.environ.get("API_TOKEN")
ADMIN_ID = os.environ.get("ADMIN_ID")
