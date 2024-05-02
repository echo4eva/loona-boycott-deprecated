# backend/utils/playlist/index.py
from auth import spotify_client as sp

def get_user_playlists():
    playlists = sp.current_user_playlists(limit=50)
    print(playlists)