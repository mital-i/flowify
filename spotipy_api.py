import spotipy
import streamlit as st

def display_playlist(playlist_id): 
    # ... (Authorization and Spotipy client creation)
    playlist_url = f"https://open.spotify.com/embed/playlist/{playlist_id}"

    playlist_data = sp.playlist(playlist_id)

    # Extract and display playlist details
    playlist_name = playlist_data["name"]
    playlist_description = playlist_data["description"]
    playlist_owner = playlist_data["owner"]["display_name"]
    tracks = playlist_data["tracks"]["items"]  # List of track dictionaries

    # Use Streamlit to display playlist details
    st.title(playlist_name)
    st.write(f"Description: {playlist_description}")
    st.write(f"Owner: {playlist_owner}")

    # Display track information (optional)
    for track in tracks:
        track_name = track["track"]["name"]
        artist_name = track["track"]["artists"][0]["name"]
        st.write(f"- {track_name} by {artist_name}")
