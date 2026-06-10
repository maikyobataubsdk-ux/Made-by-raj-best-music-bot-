from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import SUPPORT_CHAT

@Client.on_message(filters.command("start") & filters.private)
async def start_private(client: Client, message: Message):
    text = (
        "Nexus Music Bot\n\n"
        "Professional Telegram Voice Chat music system with high quality audio streaming.\n\n"
        "Use the buttons below to explore my features or add me to your group."
    )
    reply_markup = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Help", callback_data="help_main"),
            InlineKeyboardButton("Support", url=f"https://t.me/{SUPPORT_CHAT}")
        ],
        [
            InlineKeyboardButton("Add to Group", url=f"https://t.me/{client.me.username}?startgroup=true")
        ]
    ])
    await message.reply_text(
        text=text,
        reply_markup=reply_markup
    )

@Client.on_message(filters.command("start") & filters.group)
async def start_group(client: Client, message: Message):
    text = "Nexus Music Bot is active in this chat.\n\nUse /play followed by a song name or link to start streaming."
    reply_markup = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Support", url=f"https://t.me/{SUPPORT_CHAT}")
        ]
    ])
    await message.reply_text(
        text=text,
        reply_markup=reply_markup
    )
