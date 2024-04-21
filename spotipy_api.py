import webbrowser
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import streamlit as st
from dotenv import load_dotenv
import os


load_dotenv()

redirect_uri = "http://localhost:8000/callback"
client_id=os.getenv('CLIENT_ID')
client_secret=os.getenv('CLIENT_SECRET')
#change scope during merge
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# ... (Implement user authorization flow to obtain an access token)

def display_playlist(playlist_id):
    playlist_data = sp.playlist(playlist_id)
    playlist_url = f"https://open.spotify.com/embed/playlist/{playlist_id}"
    st.button("Open in Spotify", on_click=lambda: webbrowser.open(playlist_url))


    # Extract and display playlist details using Streamlit
    st.title(playlist_data["name"])
    st.write(f"Description: {playlist_data['description']}")
    st.write(f"Owner: {playlist_data['owner']['display_name']}")

    # (Optional) Display track information
    tracks = playlist_data["tracks"]["items"]
    for track in tracks:
        track_name = track["track"]["name"]
        artist_name = track["track"]["artists"][0]["name"]
        st.write(f"- {track_name} by {artist_name}")

#display button for users to authenticate log in 
def spotify_oauth():
    if not st.session_state.get("auth_token"):
        st.info("Authorize with Spotify to access your data.")
        if st.button("Authorize"):
            sp_oauth = SpotifyOAuth(client_id=client_id,
                            client_secret=client_secret,
                            redirect_uri=redirect_uri,
                            scope="playlist-read-private")   # Replace with your scopes
            auth_url = sp_oauth.get_authorize_url()
            st.session_state["auth_url"] = auth_url
            st.write("Click the button below to authorize:")
            st.write(auth_url)

            webbrowser.open(auth_url)
            if st.session_state.get("access_token"):
                # Access token found in session state, indicate successful authorization
                st.success("Authorization successful! You can now access Spotify data.")
            else:
                # Access token not found, handle potential errors
                error_msg = st.session_state.get("error_msg")
                if error_msg:
                    st.error(f"Authorization error: {error_msg}")
                else:
                    # No error message available, display generic message
                    st.warning("Authorization status unknown. Please try again.")


        