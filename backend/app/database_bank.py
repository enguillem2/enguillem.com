from motor.motor_asyncio import AsyncIOMotorClient
from app.models import Movement

from bson import ObjectId
import csv
import os

client = AsyncIOMotorClient('mongodb://mymongo')
database = client.bankdatabase
collection = database.movements

async def read_csv_bank(file):
    directory = os.getcwd()
    content=os.listdir("app/")
    for f in content:
        print("f: ",f)
    print("reading file",file,directory)
    with open(f"app/{file}",newline='\n') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            # print(', '.join(row))
            print("row",row)

async def get_all_movements():
    movements=[]
    cursor = collection.find({})
    async for document in cursor:
        movements.append(Movement(**document))
    return movements

async def get_one_movement_id(id):
    movement = await collection.find_one({"_id": ObjectId(id)})
    print("que passa amb movemnt",movement)
    return movement

async def get_one_movement(description,amount,date):
    mov = await collection.find_one({'description':description,'amount':amount,'date':date})
    return mov

async def create_movement(movement):
    new_movement=await collection.insert_one(movement)
    created_movement = await collection.find_one({'_id':new_movement.inserted_id})
    return created_movement

async def delete_movement(id:str):
    await collection.delete_one({'_id':ObjectId(id)})
    return True