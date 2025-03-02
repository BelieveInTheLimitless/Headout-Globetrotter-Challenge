from motor.motor_asyncio import AsyncIOMotorClient
from ..config.settings import settings
import json
import os

client = AsyncIOMotorClient(settings.MONGO_URI)
db = client[settings.DATABASE_NAME]

destinations_collection = db.destinations
users_collection = db.users
challenges_collection = db.challenges

async def init_db():
    count = await destinations_collection.count_documents({})
    if count == 0:
        json_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "destinations.json")
        if os.path.exists(json_path):
            with open(json_path, "r") as f:
                destinations = json.load(f)
                if destinations:
                    await destinations_collection.insert_many(destinations)
                    print(f"Imported {len(destinations)} destinations")
        else:
            print(f"Warning: destinations.json not found at {json_path}")