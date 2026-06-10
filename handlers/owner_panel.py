from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from core.decorators import owner_only

@Client.on_message(filters.command(["owner", "panel"]) & filters.private)
@owner_only
async def owner_panel(client: Client, message: Message):
    await message.reply(
        "Master Owner Panel",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Bot Management", callback_data="owner_bot")],
            [InlineKeyboardButton("User Management", callback_data="owner_user")],
            [InlineKeyboardButton("Clone Management", callback_data="owner_clone")]
        ])
    )
