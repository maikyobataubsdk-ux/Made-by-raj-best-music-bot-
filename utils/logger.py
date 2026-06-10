import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler("bot.log", maxBytes=10*1024*1024, backupCount=7),
        logging.StreamHandler()
    ]
)

logging.getLogger("pyrogram").setLevel(logging.INFO)
logging.getLogger("ntgcalls").setLevel(logging.INFO)

def get_logger(name):
    return logging.getLogger(name)
