import spotipy
from spotipy.oauth2 import SpotifyOAuth

def initialize_spotify(client_id, client_secret, redirect_uri):
    return spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                     client_secret=client_secret,
                                                     redirect_uri=redirect_uri,
                                                     scope="user-library-read user-modify-playback-state"))
