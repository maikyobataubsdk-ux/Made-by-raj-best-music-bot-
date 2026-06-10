import os
import sys
from config import BOT_TOKEN, API_ID, API_HASH, MONGO_URI
from utils.logger import get_logger

logger = get_logger("StartupCheck")

def check_env():
    if not BOT_TOKEN or not API_ID or not API_HASH or not MONGO_URI:
        logger.error("Missing required environment variables!")
        sys.exit(1)
    logger.info("Environment variables checked.")

def check_cookies():
    if not os.path.exists("cookies.txt"):
        logger.warning("cookies.txt not found. YouTube may throttle downloads.")
    else:
        logger.info("cookies.txt found.")

def run_checks():
    check_env()
    check_cookies()
