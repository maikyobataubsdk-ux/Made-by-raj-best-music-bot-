import asyncio
import os
from pyrogram import Client
from dotenv import load_dotenv

async def verify_bot():
    load_dotenv()

    bot_token = os.getenv("BOT_TOKEN")
    api_id = os.getenv("API_ID")
    api_hash = os.getenv("API_HASH")

    if not all([bot_token, api_id, api_hash]):
        print("❌ Missing environment variables (BOT_TOKEN, API_ID, or API_HASH)")
        return

    print("Attempting to connect to Telegram...")
    try:
        bot = Client(
            "VerifyBot",
            api_id=int(api_id),
            api_hash=api_hash,
            bot_token=bot_token,
            in_memory=True
        )
        async with bot:
            print(f"✅ Successfully connected to Telegram as @{bot.me.username} (ID: {bot.me.id})")
    except Exception as e:
        print(f"❌ Failed to connect: {e}")

if __name__ == "__main__":
    asyncio.run(verify_bot())
