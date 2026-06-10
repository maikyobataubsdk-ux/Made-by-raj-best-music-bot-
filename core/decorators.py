from pyrogram.types import Message
from config import OWNER_ID
from database.models import get_chat

def admin_only(func):
    async def wrapper(client, message: Message):
        if message.from_user.id == OWNER_ID:
            return await func(client, message)

        chat_id = message.chat.id
        member = await client.get_chat_member(chat_id, message.from_user.id)
        if member.privileges:
            return await func(client, message)

        return await message.reply("You must be an admin to use this command.")
    return wrapper

def owner_only(func):
    async def wrapper(client, message: Message):
        if message.from_user.id == OWNER_ID:
            return await func(client, message)
        return await message.reply("This command is restricted to the bot owner.")
    return wrapper
