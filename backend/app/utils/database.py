from motor.motor_asyncio import AsyncIOMotorClient
from ..config.settings import settings
import json
import os
import logging

# Configure logging
logger = logging.getLogger(__name__)

# Initialize MongoDB connection
try:
    client = AsyncIOMotorClient(settings.MONGO_URI)
    db = client[settings.DATABASE_NAME]
    
    destinations_collection = db.destinations
    users_collection = db.users
    challenges_collection = db.challenges
except Exception as e:
    logger.error(f"Failed to initialize MongoDB connection: {str(e)}")
    raise

async def init_db():
    """
    Initialize database by dropping and recreating all collections from JSON files.
    This ensures the database perfectly matches the source files on each deployment.
    """
    try:
        # Base directory for data files
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        
        # Reset and initialize destinations collection
        await reset_collection(
            collection=destinations_collection,
            json_path=os.path.join(base_dir, "destinations.json"),
            collection_name="destinations"
        )
        
        # Reset and initialize users collection (if users.json exists)
        await reset_collection(
            collection=users_collection,
            json_path=os.path.join(base_dir, "users.json"),
            collection_name="users"
        )
        
        # Reset and initialize challenges collection (if challenges.json exists)
        await reset_collection(
            collection=challenges_collection,
            json_path=os.path.join(base_dir, "challenges.json"),
            collection_name="challenges"
        )
        
        logger.info("Database initialization completed successfully")
        
    except Exception as e:
        logger.error(f"Unexpected error in init_db: {str(e)}")
        # Log the error but don't crash the application
        logger.warning("Continuing application startup despite database initialization failure")

async def reset_collection(collection, json_path, collection_name):
    """
    Drop and recreate a collection from a JSON file.
    If the JSON file doesn't exist, just drop and create an empty collection.
    
    Args:
        collection: The MongoDB collection object
        json_path: Path to the JSON file with data
        collection_name: Name of the collection (for logging)
    """
    try:
        # Drop the collection
        logger.info(f"Dropping {collection_name} collection")
        await collection.drop()
        
        # Check if JSON file exists and load data
        if os.path.exists(json_path):
            try:
                with open(json_path, "r") as f:
                    items = json.load(f)
                
                if items and isinstance(items, list):
                    logger.info(f"Loaded {len(items)} {collection_name} from JSON file")
                    
                    # Insert data into the empty collection
                    await collection.insert_many(items)
                    logger.info(f"Inserted {len(items)} {collection_name}")
                else:
                    logger.warning(f"No {collection_name} found in JSON file or invalid format")
            except json.JSONDecodeError as e:
                logger.error(f"Invalid JSON in {json_path}: {str(e)}")
            except Exception as e:
                logger.error(f"Failed to insert {collection_name}: {str(e)}")
        else:
            logger.info(f"{collection_name}.json not found at {json_path}, created empty collection")
            
    except Exception as e:
        logger.error(f"Failed to reset {collection_name} collection: {str(e)}")
        # Don't re-raise, allow other collections to be processed