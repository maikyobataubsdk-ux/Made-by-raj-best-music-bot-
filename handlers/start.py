from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import SUPPORT_CHAT

@Client.on_message(filters.command("start") & filters.private)
async def start_private(client: Client, message: Message):
    caption = f"Welcome {message.from_user.mention} to Nexus Music Bot!"
    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("Help", callback_data="help_main"),
         InlineKeyboardButton("Support", url=f"https://t.me/{SUPPORT_CHAT}")],
        [InlineKeyboardButton("Add to Group", url=f"https://t.me/{client.me.username}?startgroup=true")]
    ])
    try:
        await message.reply_photo(
            photo="https://telegra.ph/file/default_thumb.jpg",
            caption=caption,
            reply_markup=reply_markup
        )
    except Exception:
        await message.reply_text(
            text=caption,
            reply_markup=reply_markup
        )

@Client.on_message(filters.command("start") & filters.group)
async def start_group(client: Client, message: Message):
    await message.reply("I'm alive! Use /help to see available commands.")
