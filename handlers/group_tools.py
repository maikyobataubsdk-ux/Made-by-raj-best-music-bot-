from pyrogram import Client, filters
from pyrogram.types import Message
from core.decorators import admin_only
from database.mongo import notes_db, filters_db

@Client.on_message(filters.command("ban") & filters.group)
@admin_only
async def ban_user(client: Client, message: Message):
    user_id = message.reply_to_message.from_user.id if message.reply_to_message else (message.command[1] if len(message.command) > 1 else None)
    if not user_id: return await message.reply("Specify a user.")
    await client.ban_chat_member(message.chat.id, user_id)
    await message.reply(f"Banned {user_id}")

@Client.on_message(filters.command("unban") & filters.group)
@admin_only
async def unban_user(client: Client, message: Message):
    user_id = message.reply_to_message.from_user.id if message.reply_to_message else (message.command[1] if len(message.command) > 1 else None)
    if not user_id: return await message.reply("Specify a user.")
    await client.unban_chat_member(message.chat.id, user_id)
    await message.reply(f"Unbanned {user_id}")

@Client.on_message(filters.command("mute") & filters.group)
@admin_only
async def mute_user(client: Client, message: Message):
    user_id = message.reply_to_message.from_user.id if message.reply_to_message else (message.command[1] if len(message.command) > 1 else None)
    if not user_id: return await message.reply("Specify a user.")
    from pyrogram.types import ChatPermissions
    await client.restrict_chat_member(message.chat.id, user_id, ChatPermissions())
    await message.reply(f"Muted {user_id}")

@Client.on_message(filters.command("unmute") & filters.group)
@admin_only
async def unmute_user(client: Client, message: Message):
    user_id = message.reply_to_message.from_user.id if message.reply_to_message else (message.command[1] if len(message.command) > 1 else None)
    if not user_id: return await message.reply("Specify a user.")
    from pyrogram.types import ChatPermissions
    await client.restrict_chat_member(message.chat.id, user_id, ChatPermissions(can_send_messages=True, can_send_media_messages=True))
    await message.reply(f"Unmuted {user_id}")

# Notes logic
@Client.on_message(filters.command("note") & filters.group)
@admin_only
async def save_note(client: Client, message: Message):
    if len(message.command) < 2 or not message.reply_to_message:
        return await message.reply("Usage: /note [name] (reply to message)")
    name = message.command[1]
    content = message.reply_to_message.text or message.reply_to_message.caption
    await notes_db.update_one({"chat_id": message.chat.id, "name": name}, {"$set": {"content": content}}, upsert=True)
    await message.reply(f"Note '{name}' saved.")

@Client.on_message(filters.command("notes") & filters.group)
async def list_notes(client: Client, message: Message):
    notes = await notes_db.find({"chat_id": message.chat.id}).to_list(length=None)
    if not notes: return await message.reply("No notes found.")
    await message.reply("Notes: " + ", ".join([n["name"] for n in notes]))

# Filter logic
@Client.on_message(filters.command("filter") & filters.group)
@admin_only
async def add_filter(client: Client, message: Message):
    if len(message.command) < 3: return await message.reply("Usage: /filter [trigger] [text]")
    trigger = message.command[1]
    text = message.text.split(None, 2)[2]
    await filters_db.update_one({"chat_id": message.chat.id, "trigger": trigger}, {"$set": {"text": text}}, upsert=True)
    await message.reply(f"Filter for '{trigger}' added.")

# Trigger auto-reply
@Client.on_message(filters.group & ~filters.bot & filters.text, group=1)
async def auto_reply(client: Client, message: Message):
    chat_id = message.chat.id
    text = message.text.lower()

    # Check filters
    f = await filters_db.find_one({"chat_id": chat_id, "trigger": text})
    if f: return await message.reply(f["text"])

    # Check notes
    if text.startswith("#"):
        name = text[1:]
        n = await notes_db.find_one({"chat_id": chat_id, "name": name})
        if n: return await message.reply(n["content"])
