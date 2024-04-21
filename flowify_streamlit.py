import streamlit as st
import pandas as pd
import requests
import spotipy_api
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from gemini import authenticate, fetch_songs

st.write("""
# flowify <3
upload a picture and generate a custom playlist based on the vibe!
""") 

def upload_file(): 
  uploaded_file = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])
  # ... rest of your app logic using the uploaded_file object
  if uploaded_file is not None:
    filename = uploaded_file.name
    file_type = uploaded_file.type
    file_size = uploaded_file.size

    data = {"image": uploaded_file}  # You can use a different format if needed

    # Send a POST request with the image data to the FastAPI endpoint
    response = requests.post("http://localhost:8000/parse_image", files=data)
    if response.status_code == 200:
      data = response.json()
      st.success(data["message"])
      # Display any additional parsing results from the backend (if available)
      # For example: st.write(f"Image format: {data['format']}")
    else:
      st.error("Error sending request to backend")

def main():
  upload_file()

  # authenticate()
  # songs = fetch_songs()
  # print('SONGS:::_____')
  # print(songs)
  # print('END-------')
  
  #display playlist information
  
  #playlist_id = "37i9dQZF1DXcBWIGoYBM5M"
  #spotipy_api.display_playlist(playlist_id)
  
  #display auth button 
  spotipy_api.spotify_oauth()
  spotipy_api.test()
  
if __name__ == "__main__":
  main()
