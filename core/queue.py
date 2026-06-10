from database.mongo import queue_db

class QueueEngine:
    async def add_to_queue(self, chat_id: int, song_data: dict):
        song_data["chat_id"] = chat_id
        await queue_db.insert_one(song_data)

    async def get_queue(self, chat_id: int):
        return await queue_db.find({"chat_id": chat_id}).sort("timestamp", 1).to_list(length=None)

    async def pop_next(self, chat_id: int):
        next_song = await queue_db.find_one_and_delete({"chat_id": chat_id}, sort=[("timestamp", 1)])
        return next_song

    async def clear_queue(self, chat_id: int):
        await queue_db.delete_many({"chat_id": chat_id})

queue_engine = QueueEngine()
