import spotipy
from spotipy.oauth2 import SpotifyOAuth


def get_token(client_id, client_secret, redirect_uri):
    """Retrieve a new token or get the cached one."""
    auth_manager = SpotifyOAuth(client_id=client_id,
                                client_secret=client_secret,
                                redirect_uri=redirect_uri,
                                scope="user-library-read user-modify-playback-state")

    token_info = auth_manager.get_cached_token()

    if not token_info:
        # This will open a web page for the user to log in.
        # After logging in, Spotipy will automatically cache the token.
        token_info = auth_manager.get_access_token()

    return token_info


def refresh_token(client_id, client_secret, refresh_token):
    """Refresh the access token using the refresh token."""
    auth_manager = SpotifyOAuth(client_id=client_id,
                                client_secret=client_secret)

    new_token = auth_manager.refresh_access_token(refresh_token)
    return new_token
