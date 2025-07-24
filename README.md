# PythonAgent
LLM powered python based web application for appointment scheduling using Langchain and FastAPI.
Appointment scheduling will be using FHIR appointment APIs.

# SetUp

## Run this Agent

fhir\Scripts\activate
copy .env file as .env.dev and update the api_key in .env.dev
python main.py

application starts at http://127.0.0.1:8088

## Bring up FHIR service on local
Ref - https://medium.com/impelsys/running-and-interacting-with-your-own-hapi-fhir-server-in-local-0f12c0cbbfdd

My server runs at localhost:8086.

## Python Env setup 

python -m venv fhir
fhir\Scripts\activate
pip install fastapi uvicorn langchain openai

