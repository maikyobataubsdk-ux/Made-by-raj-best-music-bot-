import asyncio
from pyrogram import Client, idle
from config import BOT_TOKEN, API_ID, API_HASH
from utils.startup_check import run_checks
from utils.logger import get_logger
from core.call import call_manager

logger = get_logger("NexusBot")

async def main():
    try:
        run_checks()

        bot = Client(
            "NexusMusicBot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins=dict(root="handlers")
        )

        await bot.start()

        # Accessing 'me' to verify connection and log bot info
        logger.info(f"Main bot started as @{bot.me.username} (ID: {bot.me.id})")

        # NTgCalls doesn't have a start() method like PyTgCalls
        logger.info("NTgCalls ready.")

        await idle()

        await bot.stop()
        logger.info("Bot stopped.")
    except Exception as e:
        logger.error(f"Error in main loop: {e}", exc_info=True)

if __name__ == "__main__":
    asyncio.run(main())
