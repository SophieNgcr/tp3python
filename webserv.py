from typing import Optional
from fastapi import fastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello" : "World"}

    