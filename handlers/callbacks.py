from pyrogram import Client
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from database.models import get_chat, update_chat_settings

@Client.on_callback_query()
async def callback_handler(client: Client, query: CallbackQuery):
    data = query.data
    chat_id = query.message.chat.id

    if data == "settings_music":
        chat = await get_chat(chat_id)
        autoplay = chat["settings"].get("autoplay", False)
        text = "Music Settings"
        buttons = [
            [InlineKeyboardButton(f"Autoplay: {'ON' if autoplay else 'OFF'}", callback_data="toggle_autoplay")],
            [InlineKeyboardButton("Back", callback_data="settings_main")]
        ]
        await query.message.edit(text, reply_markup=InlineKeyboardMarkup(buttons))

    elif data == "toggle_autoplay":
        chat = await get_chat(chat_id)
        chat["settings"]["autoplay"] = not chat["settings"].get("autoplay", False)
        await update_chat_settings(chat_id, chat["settings"])
        await callback_handler(client, query) # Refresh

    elif data == "settings_main":
        from handlers.settings import settings_cmd # Avoid circular
        await query.message.edit("Chat Settings", reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Music Settings", callback_data="settings_music")],
            [InlineKeyboardButton("Protection Settings", callback_data="settings_protection")],
            [InlineKeyboardButton("Welcome Settings", callback_data="settings_welcome")]
        ]))

    else:
        await query.answer("Button clicked!")
