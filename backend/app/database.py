from motor.motor_asyncio import AsyncIOMotorClient
from app.models import Task,UpdateTask

from bson import ObjectId

client = AsyncIOMotorClient('mongodb://mymongo')
database = client.taskdatabase
collection = database.tasks

async def get_one_task_id(id):
    task = await collection.find_one({"_id": ObjectId(id)})
    return task

async def get_one_task(title):
    task = await collection.find_one({'title':title})
    return task

async def get_all_tasks():
    tasks=[]
    cursor = collection.find({})
    async for document in cursor:
        tasks.append(Task(**document))
    return tasks



async def create_task(task):
    new_task=await collection.insert_one(task)
    created_task = await collection.find_one({'_id':new_task.inserted_id})
    return created_task

async def update_task(id:str,data:UpdateTask):
    task = {k: v for k, v in data.dict().items() if v is not None}
    await collection.update_one({"_id": ObjectId(id)}, {"$set": task})
    document = await collection.find_one({"_id": ObjectId(id)})
    print("DOCUMENT",document)
    return document
    # await collection.update_one({'_id':id},{'set':task})
    # updated_task = await collection.find_one({'_id':id})

async def delete_task(id:str):
    await collection.delete_one({'_id':ObjectId(id)})
    return True