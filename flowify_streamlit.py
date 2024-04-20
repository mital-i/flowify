import streamlit as st
import pandas as pd
import requests
import spotipy_api

 
st.write("""
# flowify
upload a picture and generate a custom playlist based on the vibe!
""") 

def main():
  uploaded_file = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])
  # ... rest of your app logic using the uploaded_file object
  if uploaded_file is not None:
    filename = uploaded_file.name
    file_type = uploaded_file.type
    file_size = uploaded_file.size
    st.write(f"Filename: {filename}")
    st.write(f"File type: {file_type}")
    st.write(f"File size: {file_size} bytes")

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

    #display playlist information
    playlist_id = "37i9dQZF1DXcBWIGoYBM5M"
    spotipy_api.display_playlist(playlist_id)
  
if __name__ == "__main__":
  main()
