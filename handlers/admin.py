from pyrogram import Client, filters
from pyrogram.types import Message
from core.decorators import owner_only
import sys
import os

@Client.on_message(filters.command("restart") & filters.private)
@owner_only
async def restart_bot(client: Client, message: Message):
    await message.reply("Restarting...")
    os.execl(sys.executable, sys.executable, *sys.argv)

@Client.on_message(filters.command("stats") & filters.private)
@owner_only
async def stats_cmd(client: Client, message: Message):
    # Simplified stats
    await message.reply("Bot Stats: TBD")
