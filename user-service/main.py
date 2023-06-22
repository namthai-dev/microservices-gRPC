# user-service/main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
async def get_users():
    return {"users": []}
