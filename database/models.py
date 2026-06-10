from database.mongo import chats_db, users_db, clones_db

async def get_chat(chat_id: int):
    chat = await chats_db.find_one({"chat_id": chat_id})
    if not chat:
        chat = {
            "chat_id": chat_id,
            "settings": {
                "song_request": "everyone",
                "queue_limit": 0,
                "duration_limit": 0,
                "autoplay": False,
                "loop_mode": "off",
                "volume": 100,
                "video": False,
                "dj_role": [],
                "welcome": True,
                "welcome_text": "Welcome {mention} to {chat}!",
                "welcome_media": None,
                "goodbye": False,
                "goodbye_text": "Goodbye {name}!",
                "language": "EN",
                "prefix": "/",
                "del_cmds": True,
                "antiflood": False,
                "antispam": False,
                "antibot": False,
                "link_filter": False,
                "caps_filter": False,
                "bad_words": False
            }
        }
        await chats_db.insert_one(chat)
    return chat

async def update_chat_settings(chat_id: int, settings: dict):
    await chats_db.update_one({"chat_id": chat_id}, {"$set": {"settings": settings}})

async def get_user(user_id: int):
    user = await users_db.find_one({"user_id": user_id})
    if not user:
        user = {
            "user_id": user_id,
            "is_banned": False,
            "is_admin": False,
            "clones": []
        }
        await users_db.insert_one(user)
    return user

async def add_clone(clone_data: dict):
    await clones_db.insert_one(clone_data)

async def get_clones(owner_id: int):
    return await clones_db.find({"owner_id": owner_id}).to_list(length=None)
