from fastapi import FastAPI,HTTPException
from routes.task import task
from routes.bank import bank
from fastapi.middleware.cors import CORSMiddleware
from decouple import config

app = FastAPI()

origins=[
    config('FRONTED_URL'),
    config('FRONTED_URL2'),
    config('FRONTED_URL3')

]

print("origins:",origins)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "Worldaa"}



app.include_router(task)
app.include_router(bank)

