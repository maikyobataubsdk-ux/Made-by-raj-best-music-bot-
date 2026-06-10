import ntgcalls
from pyrogram import Client
from config import BOT_TOKEN

class CallManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CallManager, cls).__new__(cls)
            cls._instance.calls = {} # bot_token -> NTgCalls
        return cls._instance

    def get_call(self, client: Client):
        bot_token = client.bot_token if hasattr(client, "bot_token") else BOT_TOKEN
        if bot_token not in self.calls:
            self.calls[bot_token] = ntgcalls.NTgCalls(client)
        return self.calls[bot_token]

    async def play(self, client: Client, chat_id: int, file_path: str):
        call = self.get_call(client)

        # Check if already connected
        try:
            state = call.get_state(chat_id)
        except:
            call.create_call(chat_id)

        audio_desc = ntgcalls.AudioDescription(
            media_source=ntgcalls.MediaSource.FFMPEG,
            sample_rate=48000,
            channel_count=2,
            input=file_path
        )
        media_desc = ntgcalls.MediaDescription(microphone=audio_desc)
        # Using PLAYBACK mode for stream direction as per ntgcalls logic
        call.set_stream_sources(chat_id, ntgcalls.StreamMode.PLAYBACK, media_desc)

call_manager = CallManager()
