# user-service/main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/orders")
async def get_orders():
    return {"orders": []}
