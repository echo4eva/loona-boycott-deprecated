# backend\main.py
from flask import Flask, redirect, request, jsonify, session
from flask_cors import CORS
from auth import get_spotify_auth, get_token
from dotenv import load_dotenv
from utils.replace import replace_songs_with_ep
load_dotenv()
import os
import spotipy

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')
CORS(app, resources={r"/*": {"origins": ["http://localhost:3000"]}}, supports_credentials=True)

@app.route("/")
def read_root():
    return "<p>Hello, World</p>"

@app.route("/login")
def login():
    sp_auth = get_spotify_auth()
    auth_url = sp_auth.get_authorize_url()

    return jsonify({'auth_url': auth_url})

@app.route("/callback")
def call_back():
    code = request.args.get('code')
    sp_auth = get_spotify_auth()
    token_info = sp_auth.get_access_token(code)
    session['TOKEN_INFO'] = token_info

    frontend_redirect_url = f'http://localhost:3000/'
    return redirect(frontend_redirect_url)

    # for debugging
    # return session['TOKEN_INFO']

@app.route('/me')
def test_token():
    access_token = get_token()
    if access_token:
        sp = spotipy.Spotify(auth=access_token)
        user_info = sp.me()
        return jsonify(user_info), 200
    else:
        return jsonify({'error' : 'failed to get access token'}), 401
    
@app.route('/boycott', methods=['POST'])
def boycott_playlist():
    access_token = get_token()
    if access_token:
        playlist_id = request.form.get('playlist_id')
        print(playlist_id)
        if playlist_id:
            try:
                replace_songs_with_ep(playlist_id)
                return jsonify({'message': 'Playlist updated successfully'}), 200
            except Exception as e:
                return jsonify({'error': str(e)}), 500
        else:
            return jsonify({'error': 'Playlist ID is required'}), 400
    else:
        return jsonify({'error': 'Failed to retrieve access token'}), 401



if __name__ == "__main__":
    app.run(debug=True)