from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

class MongoManager:
    _client = None
    _database = None

    @classmethod
    def connect(cls):
        if cls._client is None:
            cls._client = AsyncIOMotorClient(os.getenv("MONGO_URI"))
            cls._database = cls._client[os.getenv("DB_NAME")]
            print(f"Connected to MongoDB database: {os.getenv('DB_NAME')}")
    
    @classmethod
    def get_database(cls):
        return cls._database
    
    @classmethod
    def disconnect(cls):
        if cls._client:
            cls._client.close()
            cls._client = None
            cls._database = None
            print("MongoDB connection closed")