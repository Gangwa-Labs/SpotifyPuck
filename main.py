import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
import os

# Set your client ID, client secret, and redirect URI
SPOTIPY_CLIENT_ID = '3e64a448ffda4cb6ad51e8f0da677680'
SPOTIPY_CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']
SPOTIPY_REDIRECT_URI = 'https://localhost:8080'
if not SPOTIPY_CLIENT_SECRET:
    raise ValueError("SPOTIPY_CLIENT_SECRET is not set in the environment variables.")

# Create a Spotify object with Authorization Code Flow
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope="app-remote-control user-modify-playback-state",
                                               open_browser=False))
print("Press 'a' to pause the song and 's' to resume it. Press 'q' to quit.")

while True:
    command = input("Enter your command: ")

    if command == 'a':
        sp.pause_playback()
        print("Song paused.")
    elif command == 's':
        sp.start_playback()
        print("Song resumed.")
    elif command == 'q':
        print("Exiting...")
        break
    else:
        print("Invalid command. Press 'a' to pause, 's' to resume, or 'q' to quit.")