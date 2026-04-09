from fastapi import FastAPI
import uvicorn

app = FastAPI()

# Changed from .post to .get file 
@app.get("/")
async def hello():
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)