from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root_msg():
    return {"message": "Hello World to Appointment Agent"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        port=8088
    )