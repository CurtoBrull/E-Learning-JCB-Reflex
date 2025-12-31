"""Test MongoDB connection with current credentials"""
import os
import asyncio
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
print(f"Testing connection...")
print(f"URI: {MONGODB_URI[:50]}...{MONGODB_URI[-50:]}")

async def test_connection():
    try:
        client = AsyncIOMotorClient(MONGODB_URI)
        db = client.get_default_database()
        print(f"✓ Database name: {db.name}")

        await client.admin.command('ping')
        print("✓ Successfully connected to MongoDB!")

        collections = await db.list_collection_names()
        print(f"✓ Collections: {collections}")

        client.close()
        return True

    except Exception as e:
        print(f"✗ Connection failed: {str(e)}")
        return False

if __name__ == "__main__":
    success = asyncio.run(test_connection())
    exit(0 if success else 1)
