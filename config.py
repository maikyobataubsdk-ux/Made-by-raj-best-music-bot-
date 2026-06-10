import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH")
MONGO_URI = os.getenv("MONGO_URI")
REDIS_URL = os.getenv("REDIS_URL")
OWNER_ID = int(os.getenv("OWNER_ID", 0))
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", 0))
SUPPORT_CHAT = os.getenv("SUPPORT_CHAT")
DURATION_LIMIT = int(os.getenv("DURATION_LIMIT", 60))
AUTO_LEAVE_DELAY = int(os.getenv("AUTO_LEAVE_DELAY", 300))
CLONE_SUPPORT_CHAT = os.getenv("CLONE_SUPPORT_CHAT")
CLONE_LOG_CHANNEL = int(os.getenv("CLONE_LOG_CHANNEL", 0))
MAX_CLONES_PER_USER = int(os.getenv("MAX_CLONES_PER_USER", 3))

COOKIES_PATH = "cookies.txt"
CACHE_DIR = "/tmp/nexus_cache/"
THUMBNAIL_PATH = "assets/thumbnail.jpg"
