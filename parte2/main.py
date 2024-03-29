from typing import Optional
import uvicorn
from fastapi import FastAPI

app =  FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

if __name__=='__main__':
    uvicorn.run(app)