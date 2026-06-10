from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI

client = AsyncIOMotorClient(MONGO_URI)
db = client.NexusBot

chats_db = db.chats
users_db = db.users
clones_db = db.clones
broadcast_db = db.broadcast_log
notes_db = db.notes
filters_db = db.filters
queue_db = db.queue
