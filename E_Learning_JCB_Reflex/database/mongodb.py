"""MongoDB database connection configuration."""

import os
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# MongoDB URI from environment
MONGODB_URI = os.getenv("MONGODB_URI")

if not MONGODB_URI:
    raise ValueError("MONGODB_URI environment variable is not set")


class MongoDB:
    """MongoDB connection manager."""

    client: AsyncIOMotorClient = None
    db = None

    @classmethod
    async def connect(cls):
        """Connect to MongoDB."""
        if cls.client is None:
            cls.client = AsyncIOMotorClient(MONGODB_URI)
            # Extract database name from URI or use default
            cls.db = cls.client.get_default_database()
            print(f"Connected to MongoDB: {cls.db.name}")

    @classmethod
    async def disconnect(cls):
        """Disconnect from MongoDB."""
        if cls.client:
            cls.client.close()
            cls.client = None
            cls.db = None
            print("Disconnected from MongoDB")

    @classmethod
    def get_db(cls):
        """Get database instance."""
        if cls.db is None:
            raise RuntimeError("Database not connected. Call connect() first.")
        return cls.db


# Synchronous client for initial setup/testing
def get_sync_client():
    """Get synchronous MongoDB client."""
    return MongoClient(MONGODB_URI)
