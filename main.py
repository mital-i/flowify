from fastapi import FastAPI
from gemini import authenticate, fetch_songs

app = FastAPI()

@app.get("/")
async def root():
    authenticate()
    songs = fetch_songs()
    return {"message": songs}