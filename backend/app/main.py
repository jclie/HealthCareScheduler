"""
Programmer: Julie Tong
Filename: main.py
Description: Entry point for the hospital scheduling backend API
             Defines the FastAPI application and its endpoints
"""
from fastapi import FastAPI

# create the FASTAPI application
app = FastAPI()

@app.get("/")
def home():
    "health-check endpoint to verify that the backend server is running successfully"
    return {
        "message": "API is running"
    }