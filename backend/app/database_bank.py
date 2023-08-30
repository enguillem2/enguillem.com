from motor.motor_asyncio import AsyncIOMotorClient
from app.models import Movement

from bson import ObjectId

client = AsyncIOMotorClient('mongodb://mymongo')
database = client.bankdatabase
collection = database.movements

async def create_movement(movement):
    new_movement=await collection.insert_one(movement)
    created_movement = await collection.find_one({'_id':new_movement.inserted_id})
    return created_movement