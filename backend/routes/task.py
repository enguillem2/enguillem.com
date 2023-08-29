from fastapi import APIRouter,HTTPException
from app.database import *

from app.models import Task,UpdateTask

task = APIRouter()

@task.get('/api/tasks')
async def get_tasks():
    tasks=await get_all_tasks()
    return tasks

@task.post('/api/tasks',response_model=Task)
async def save_task(task:Task):
    taskFound = await get_one_task(task.title)
    if taskFound:
        raise HTTPException(409,"task alreay exists")

    response = await create_task(task.dict())
    print("response",response)
    if response:
        return response
    raise HTTPException(400,"something went wront")
    

@task.get('/api/tasks/{id}',response_model=Task)
async def get_tasks(id:str):
    task = await get_one_task_id(id)
    if task:
        return task
    raise HTTPException(404,f"task with id {id} not found")

@task.put('/api/tasks/{id}',response_model=Task)
async def put_tasks(id:str,data:UpdateTask):
    updated_task=await update_task(id,data)
    if updated_task:
        return updated_task
    raise HTTPException(404,f"Task witdh id {id} not found")

@task.delete('/api/tasks/{id}')
async def remove_task(id:str):
    response = await delete_task(id)
    if response:
        return {f"task {id} deleted {response}"}
    raise HTTPException(404,f"task with id {id} not found")