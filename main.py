from fastapi import FastAPI, UploadFile, File
from gemini import authenticate, fetch_songs
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.responses import RedirectResponse
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

app = FastAPI()

load_dotenv()
redirect_uri = "http://localhost:8000/callback"  # Replace with your local dev redirect URI
scope = "playlist-read-private"  # Replace with desired scopes
sp_oauth = SpotifyOAuth(client_id=os.getenv('CLIENT_ID'),
                        client_secret=os.getenv('CLIENT_SECRET'),
                        redirect_uri=redirect_uri,
                        scope=scope)

@app.get("/callback")
async def callback(code, state: str = None):
    """Handles redirect callback from Spotify with authorization code."""
    # Verify state token (if used)
    #print(code)
    if code is None:
      # Handle case where code is missing
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing authorization code")
    try:
      # Exchange authorization code for access and refresh tokens
      token_info = sp_oauth.get_access_token(code)
      access_token = token_info['access_token']
      #print("access token", access_token)
      # refresh_token = sp_oauth.refresh_token

      # Redirect back to Streamlit app with success message (using session state)
      # (code omitted for brevity)
      #return {"message": "trying to access authentication token" + access_token}
    except Exception as e:
        # Handle errors during token exchange
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))

@app.post("/parse_image")
async def parse_image(image: UploadFile = File(...)):

    # ... further processing based on your requirements (add your logic here)

  return {"message": "Image parsed successfully!"}

@app.get("/")
async def root():
    authenticate()
    songs = fetch_songs()
    return {"message": songs}
