from fastapi import FastAPI
from fastapi.responses import FileResponse
from models.query import Query
import uvicorn

app = FastAPI()

@app.get("/")
async def root_msg():
    return {"message": "Hello World to Appointment Agent"}

@app.post("/chat")
async def chat(query: Query):
    print("Received chat message " + query.usermessage)
    return "We received your message. Will reach out to you shortly. Thank you!."


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("static/favicon.png")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        port=8088
    )