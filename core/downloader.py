import asyncio
import os
from yt_dlp import YoutubeDL
from config import COOKIES_PATH, CACHE_DIR

class Downloader:
    def __init__(self):
        self.opts = {
            "format": "bestaudio/best",
            "outtmpl": f"{CACHE_DIR}%(id)s.%(ext)s",
            "cookiefile": COOKIES_PATH if os.path.exists(COOKIES_PATH) else None,
            "quiet": True,
            "no_warnings": True,
            "noprogress": True,
        }

    async def extract_info(self, query: str):
        if not query.startswith(("http://", "https://")):
            query = f"ytsearch:{query}"
        loop = asyncio.get_event_loop()
        with YoutubeDL(self.opts) as ydl:
            return await loop.run_in_executor(None, lambda: ydl.extract_info(query, download=False))

    async def download(self, url: str):
        loop = asyncio.get_event_loop()
        with YoutubeDL(self.opts) as ydl:
            info = await loop.run_in_executor(None, lambda: ydl.extract_info(url, download=True))
            return ydl.prepare_filename(info)

downloader = Downloader()
