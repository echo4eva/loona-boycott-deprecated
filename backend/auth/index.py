# backend/auth/index.py
import os
import dotenv
import spotipy
import time
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
from flask import session

load_dotenv()

def get_spotify_client():
    client_id = os.getenv('SPOTIPY_CLIENT_ID')
    client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
    redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI')
    scope = "playlist-read-private,playlist-modify-private,playlist-modify-public"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scope=scope
        ))
    
    return sp

def get_spotify_auth():
    client_id = os.getenv('SPOTIPY_CLIENT_ID')
    client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
    redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI')
    scope = "playlist-read-private,playlist-modify-private,playlist-modify-public"

    sp_auth = SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scope=scope
        )
    
    return sp_auth

def refresh_access_token():
    """
    Refreshes the access token using the stored refresh token.
    """
    sp_auth = get_spotify_auth()

    # Retrieve the refresh token from the session
    refresh_token = session.get('TOKEN_INFO', {}).get('refresh_token')

    try:
        # Use the refresh token to get a new access token
        new_token_info = sp_auth.refresh_access_token(refresh_token)

        # Update the token information in the session
        session['TOKEN_INFO'] = new_token_info

        return new_token_info
    except Exception as e:
        # Handle any errors that occur during the token refresh
        print(f"Error refreshing access token: {e}")
        return None
    
def get_token():
    """
    Retrieves the access token from the session, refreshing it if necessary.
    """
    try:
        token_info = session.get('TOKEN_INFO')

        access_token = token_info.get('access_token')
        expires_at = token_info.get('expires_at')

        now = int(time.time())
        # Check if the access token is expired
        if expires_at < now:
            # Access token is expired, refresh it
            new_token_info = refresh_access_token(token_info.get('refresh_token'))

            if new_token_info:
                # Update the token info in the session
                session['TOKEN_INFO'] = new_token_info
                return new_token_info['access_token']
            else:
                # Failed to refresh the access token
                return None
        else:
            # Access token is still valid, return it
            return access_token
    except:
        return None