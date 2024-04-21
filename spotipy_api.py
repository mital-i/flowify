import webbrowser
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import streamlit as st


# ... (Replace with your credentials)
client_id = "b6d5d4c9193347ec86496ebec8ccb7cf"
client_secret = "6c748a90b2ae41869a0f689122be1d35"
redirect_uri = "http://localhost:8501/"

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
            webbrowser.open(auth_url)
            st.write("Authentication successful!!")

            