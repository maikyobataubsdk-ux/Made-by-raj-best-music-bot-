from PIL import Image, ImageDraw, ImageFont, ImageFilter
import aiohttp
import aiofiles
import os
from config import THUMBNAIL_PATH

async def generate_thumbnail(title, duration, requester, thumbnail_url):
    async with aiohttp.ClientSession() as session:
        async with session.get(thumbnail_url) as resp:
            if resp.status == 200:
                f = await aiofiles.open("temp_thumb.jpg", mode="wb")
                await f.write(await resp.read())
                await f.close()
            else:
                # Fallback if URL fails
                Image.new('RGB', (1280, 720), color='black').save("temp_thumb.jpg")

    img = Image.open("temp_thumb.jpg")
    img = img.resize((1280, 720))

    # Create blurred background
    blur_img = img.filter(ImageFilter.GaussianBlur(20))

    # Create dark overlay
    overlay = Image.new('RGBA', (1280, 720), (0, 0, 0, 150))
    blur_img.paste(overlay, (0, 0), overlay)

    draw = ImageDraw.Draw(blur_img)

    # Use default font if custom font not found
    try:
        font_title = ImageFont.truetype("arial.ttf", 60)
        font_info = ImageFont.truetype("arial.ttf", 40)
    except:
        font_title = ImageFont.load_default(size=60)
        font_info = ImageFont.load_default(size=40)

    # Truncate title
    if len(title) > 40:
        title = title[:37] + "..."

    draw.text((50, 450), title, fill="white", font=font_title)
    draw.text((50, 550), f"Duration: {duration}", fill="white", font=font_info)
    draw.text((50, 620), f"Requested by: {requester}", fill="white", font=font_info)

    # Paste original thumbnail in center-top
    small_thumb = img.resize((400, 400))
    blur_img.paste(small_thumb, (440, 30))

    blur_img.convert("RGB").save(THUMBNAIL_PATH)
    return THUMBNAIL_PATH
