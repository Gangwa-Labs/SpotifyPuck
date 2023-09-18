def get_current_song_info(spotify_client):
    track_info = spotify_client.current_playback()
    song_name = track_info['item']['name']
    artist_name = track_info['item']['artists'][0]['name']
    album_cover_url = track_info['item']['album']['images'][0]['url']
    return song_name, artist_name, album_cover_url

def play_pause(spotify_client):
    playback = spotify_client.current_playback()
    if playback['is_playing']:
        spotify_client.pause_playback()
    else:
        spotify_client.start_playback()

def skip_forward(spotify_client):
    spotify_client.next_track()

def skip_backward(spotify_client):
    spotify_client.previous_track()

def set_volume(spotify_client, volume_percent):
    spotify_client.volume(volume_percent)
