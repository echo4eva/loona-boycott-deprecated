# backend/auth/__init__.py
from .index import get_spotify_client, get_spotify_auth, get_token

spotify_client = get_spotify_client()
spotify_auth = get_spotify_auth()