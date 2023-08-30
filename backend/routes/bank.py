from fastapi import APIRouter,HTTPException
from app.database_bank import *

from app.models import Movement

bank = APIRouter()

@bank.get('/api/movements')
async def get_movements():
    # tasks=await get_all_tasks()
    # return tasks
    return {"Hello": "movments"}

@bank.post('/api/movement',response_model=Movement)
async def save_movement(movement:Movement):
    print("dins post")
    response= await create_movement(movement.dict())
    print("response:",response)
    if response:
        return response
    raise HTTPException(400,"something went wront")

@bank.post('/api/test')
async def test(movement:Movement):
    return {"Hello": "test"}
    
    




