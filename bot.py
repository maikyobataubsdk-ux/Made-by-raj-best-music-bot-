import asyncio
from pyrogram import Client, idle
from config import BOT_TOKEN, API_ID, API_HASH
from utils.startup_check import run_checks
from utils.logger import get_logger
from core.call import call_manager

logger = get_logger("NexusBot")

async def main():
    run_checks()

    bot = Client(
        "NexusMusicBot",
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN,
        plugins=dict(root="handlers")
    )

    await bot.start()
    logger.info("Main bot started.")

    # NTgCalls doesn't have a start() method like PyTgCalls
    logger.info("NTgCalls ready.")

    await idle()

    await bot.stop()
    logger.info("Bot stopped.")

if __name__ == "__main__":
    asyncio.run(main())
