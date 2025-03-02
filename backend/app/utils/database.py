from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import UpdateOne
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
    
    json_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "destinations.json")
    
    if os.path.exists(json_path):
        with open(json_path, "r") as f:
            destinations = json.load(f)
        
        if destinations:
            if count == 0:
                await destinations_collection.insert_many(destinations)
                print(f"Imported {len(destinations)} destinations")
            else:
                bulk_operations = []
                for destination in destinations:
                    bulk_operations.append(
                        UpdateOne(
                            {"name": destination["name"]},
                            {"$set": destination},
                            upsert=True
                        )
                    )
                
                if bulk_operations:
                    result = await destinations_collection.bulk_write(bulk_operations)
                    print(f"Updated {result.modified_count} destinations")
                    print(f"Inserted {result.upserted_count} new destinations")
    else:
        print(f"Warning: destinations.json not found at {json_path}")