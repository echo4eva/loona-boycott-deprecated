# backend/app.py
from auth import spotify_client as sp
from utils.playlist import get_user_playlists

print(get_user_playlists())