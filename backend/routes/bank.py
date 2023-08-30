from fastapi import APIRouter,HTTPException
from app.database_bank import *

from app.models import Movement

bank = APIRouter()

@bank.get('/api/movements')
async def get_movements():
    movements=await get_all_movements()
    return movements

@bank.get('/api/movements/{id}',response_model=Movement)
async def get_movements(id:str):
    movement = await get_one_movement_id(id)
    if movement:
        return movement
    raise HTTPException(404,f"movement with id {id} not found")

@bank.post('/api/movement',response_model=Movement)
async def save_movement(movement:Movement):
    print("dins post")
    movementFound=await get_one_movement(movement.description,movement.amount,movement.date)
    if movementFound:
        raise HTTPException(409,"movement alreay exists")

    response= await create_movement(movement.dict())
    print("response:",response)
    if response:
        return response
    raise HTTPException(400,"something went wront")



@bank.delete('/api/movements/{id}')
async def remove_movement(id:str):
    print("la IDDDD",id)
    response = await delete_movement(id)
    if response:
        return {f"task {id} deleted {response}"}
    raise HTTPException(404,f"movment with id {id} not found")
    
    




