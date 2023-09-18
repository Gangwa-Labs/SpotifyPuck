import os
import pygame
from hyperpixel2r import Touch
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID = '3e64a448ffda4cb6ad51e8f0da677680'
SPOTIPY_CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']
SPOTIPY_REDIRECT_URI = 'https://localhost:8080'
if not SPOTIPY_CLIENT_SECRET:
    raise ValueError("SPOTIPY_CLIENT_SECRET is not set in the environment variables.")

# Initialize Spotify API
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope="app-remote-control,user-modify-playback-state"))

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((480, 480))
pygame.display.set_caption('Spotify Play/Pause')

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Button dimensions
button_x = 160
button_y = 210
button_width = 160
button_height = 60

# Main loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the play/pause button
    pygame.draw.rect(screen, GREEN if sp.current_playback()['is_playing'] else RED,
                     (button_x, button_y, button_width, button_height))

    touch = Touch()


    @touch.on_touch
    def handle_touch(touch_id, x, y, state):
        if state and button_x <= x <= button_x + button_width and button_y <= y <= button_y + button_height:
            if sp.current_playback()['is_playing']:
                sp.pause_playback()
            else:
                sp.start_playback()


    pygame.display.flip()

pygame.quit()
