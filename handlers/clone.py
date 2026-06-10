from pyrogram import Client, filters
from pyrogram.types import Message
from database.models import add_clone, get_clones
import subprocess
import sys
import os

@Client.on_message(filters.command("getclone") & filters.private)
async def get_clone_handler(client: Client, message: Message):
    await message.reply("Please send your bot token from @BotFather.")

@Client.on_message(filters.text & filters.private)
async def process_token(client: Client, message: Message):
    if ":" in message.text and len(message.text) > 30:
        token = message.text
        # Normally validate here

        clone_data = {
            "bot_token": token,
            "owner_id": message.from_user.id,
            "status": "running"
        }
        await add_clone(clone_data)

        # Start clone process
        # We use environmental variables to pass config to clone
        env = os.environ.copy()
        env["BOT_TOKEN"] = token

        subprocess.Popen([sys.executable, "bot.py"], env=env)

        await message.reply("Clone deployed successfully!")
