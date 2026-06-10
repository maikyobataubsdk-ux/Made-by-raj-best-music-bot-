from pyrogram import Client, filters
from pyrogram.types import Message
from core.downloader import downloader
from core.call import call_manager
from core.queue import queue_engine
import time

@Client.on_message(filters.command(["play", "vplay"]) & filters.group)
async def play_handler(client: Client, message: Message):
    query = " ".join(message.command[1:])
    if not query:
        return await message.reply("Please provide a song name or URL.")

    m = await message.reply("Searching...")
    try:
        info = await downloader.extract_info(query)
        if not info:
            return await m.edit("No results found.")

        if "entries" in info:
            if not info["entries"]:
                return await m.edit("No results found.")
            info = info["entries"][0]

        song_data = {
            "title": info.get("title", "Unknown"),
            "duration": info.get("duration", 0),
            "url": info.get("url") or info.get("webpage_url"),
            "thumbnail": info.get("thumbnail"),
            "requested_by": message.from_user.id,
            "timestamp": time.time()
        }

        if not song_data["url"]:
            return await m.edit("Failed to get audio URL.")

        # In a real bot we'd check if bot is already in VC.
        # For now, we attempt to play.
        await call_manager.play(client, message.chat.id, song_data["url"])
        await m.edit(f"Playing: {song_data['title']}")

    except Exception as e:
        await m.edit(f"Error: {str(e)}")
