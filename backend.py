from fastapi import FastAPI, UploadFile, File
from frontend import upload_file
from gemini import authenticate, fetch_songs
from fastapi import FastAPI, HTTPException, Depends, status
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
from spotify_client import SpotifyClient

app = FastAPI()

load_dotenv()
redirect_uri = "http://localhost:8000/callback"  
scope = "playlist-read-private playlist-modify-private"  
sp_oauth = SpotifyOAuth(client_id=os.getenv('CLIENT_ID'),
                        client_secret=os.getenv('CLIENT_SECRET'),
                        redirect_uri=redirect_uri,
                        scope=scope)
spotify_client = SpotifyClient()

@app.get("/callback")
async def callback(code, state: str = None):
    """Handles redirect callback from Spotify with authorization code."""

    # Verify state token (if used)
    #print(code)
    if code is None:
      # Handle case where code is missing
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing authorization code")
    try:
        upload_file()
        # Exchange authorization code for access and refresh tokens
        token_info = sp_oauth.get_access_token(code)
        access_token = token_info['access_token']
        #print("access token", access_token)
        # refresh_token = sp_oauth.refresh_token

        spotify_client.create_playlist()

        # Redirect back to Streamlit app with success message (using session state)
        return {"message": "id"}
    except Exception as e:
        # Handle errors during token exchange
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))

@app.post("/parse_image")
async def parse_image(image: UploadFile = File(...)):
    # authenticate()
    # song_to_artists = fetch_songs()

    # spotify_client.add_songs_to_playlist(song_to_artists)
  
    return {"message": "Image parsed successfully!"}

@app.get("/")
async def root():
    
    return {"message": "success"}
