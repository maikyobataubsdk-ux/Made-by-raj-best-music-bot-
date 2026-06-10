from pyrogram import Client, filters
from pyrogram.types import Message
from core.call import call_manager
from core.decorators import admin_only

@Client.on_message(filters.command("pause") & filters.group)
@admin_only
async def pause_handler(client: Client, message: Message):
    call = call_manager.get_call(client)
    call.pause(message.chat.id)
    await message.reply("Stream paused.")

@Client.on_message(filters.command("resume") & filters.group)
@admin_only
async def resume_handler(client: Client, message: Message):
    call = call_manager.get_call(client)
    call.resume(message.chat.id)
    await message.reply("Stream resumed.")

@Client.on_message(filters.command("stop") & filters.group)
@admin_only
async def stop_handler(client: Client, message: Message):
    call = call_manager.get_call(client)
    call.stop(message.chat.id)
    await message.reply("Stream stopped.")

@Client.on_message(filters.command("mute") & filters.group)
@admin_only
async def mute_handler(client: Client, message: Message):
    call = call_manager.get_call(client)
    call.mute(message.chat.id)
    await message.reply("Bot muted in VC.")

@Client.on_message(filters.command("unmute") & filters.group)
@admin_only
async def unmute_handler(client: Client, message: Message):
    call = call_manager.get_call(client)
    call.unmute(message.chat.id)
    await message.reply("Bot unmuted in VC.")
