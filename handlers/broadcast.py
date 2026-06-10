import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from core.decorators import owner_only
from database.mongo import chats_db

@Client.on_message(filters.command("broadcast") & filters.private)
@owner_only
async def broadcast_handler(client: Client, message: Message):
    if not message.reply_to_message and len(message.command) < 2:
        return await message.reply("Provide a message or reply to one.")

    msg = message.reply_to_message if message.reply_to_message else message.text.split(None, 1)[1]

    chats = await chats_db.find({}, {"chat_id": 1}).to_list(length=None)
    sent = 0
    failed = 0

    for chat in chats:
        try:
            if isinstance(msg, Message):
                await msg.copy(chat["chat_id"])
            else:
                await client.send_message(chat["chat_id"], msg)
            sent += 1
            await asyncio.sleep(0.05) # Flood safety
        except Exception:
            failed += 1

    await message.reply(f"Broadcast complete.\nSent: {sent}\nFailed: {failed}")
