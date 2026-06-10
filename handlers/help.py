from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("help"))
async def help_cmd(client: Client, message: Message):
    await message.reply(
        "Nexus Music Bot Help Menu",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Music", callback_data="help_music"),
             InlineKeyboardButton("Group Tools", callback_data="help_tools")],
            [InlineKeyboardButton("Settings", callback_data="help_settings"),
             InlineKeyboardButton("Clones", callback_data="help_clones")]
        ])
    )
