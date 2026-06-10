from pyrogram import Client, filters
from pyrogram.types import Message
from core.queue import queue_engine

@Client.on_message(filters.command("queue") & filters.group)
async def queue_handler(client: Client, message: Message):
    queue = await queue_engine.get_queue(message.chat.id)
    if not queue:
        return await message.reply("Queue is empty.")

    text = "Current Queue:\n"
    for i, song in enumerate(queue, 1):
        text += f"{i}. {song['title']}\n"
    await message.reply(text)

@Client.on_message(filters.command("clearqueue") & filters.group)
async def clear_queue_handler(client: Client, message: Message):
    await queue_engine.clear_queue(message.chat.id)
    await message.reply("Queue cleared.")
