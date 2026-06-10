from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from core.decorators import admin_only
from database.models import get_chat

@Client.on_message(filters.command("settings") & filters.group)
@admin_only
async def settings_cmd(client: Client, message: Message):
    await message.reply(
        "Chat Settings",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Music Settings", callback_data="settings_music")],
            [InlineKeyboardButton("Protection Settings", callback_data="settings_protection")],
            [InlineKeyboardButton("Welcome Settings", callback_data="settings_welcome")]
        ])
    )
