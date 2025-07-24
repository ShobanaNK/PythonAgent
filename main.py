from fastapi import FastAPI
from fastapi.responses import FileResponse
from models.query import Query
from LLMAgent import AgentService
import uvicorn
import os
from dotenv import load_dotenv

# Option 1: Use an environment variable (recommended)
env_mode = os.getenv("ENV_MODE", "dev")  # fallback to 'dev' if not set

# Build the filename
env_file = f".env.{env_mode}"

# Load the appropriate file
load_dotenv(dotenv_path=env_file)

app = FastAPI()

@app.get("/")
async def root_msg():
    return {"message": "Hello World to Appointment Agent"}

@app.post("/chat")
async def chat(query: Query):
    print("Received chat message " + query.usermessage)
    agentService = AgentService()
    llm = agentService.get_chat_model()
    prompt = agentService.get_prompt(query.usermessage)
    response = llm.invoke(prompt)
    return response.content


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("static/favicon.png")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        port=8088
    )