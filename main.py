from fastapi import FastAPI, UploadFile, File
from gemini import authenticate, fetch_songs

app = FastAPI()

@app.post("/parse_image")
async def parse_image(image: UploadFile = File(...)):

    # ... further processing based on your requirements (add your logic here)

  return {"message": "Image parsed successfully!"}

@app.get("/")
async def root():
    authenticate()
    songs = fetch_songs()

    print('SONGS:::_____')
    print(songs)
    print('END-------')
    
    return {"message": songs}
