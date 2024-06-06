# backend\main.py
from flask import Flask, redirect, request, jsonify, session
from flask_cors import CORS
from flask_session import Session
from auth import get_spotify_auth, get_token
from utils.replace import replace_songs_with_ep
import spotipy
from config import ApplicationConfig

app = Flask(__name__)
app.config.from_object(ApplicationConfig)
server_session = Session(app)
# CORS(app, resources={r"/*": {"origins": ["http://localhost:3000"]}}, supports_credentials=True)
cors = CORS(app, supports_credentials=True)

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

    frontend_redirect_url = f'http://127.0.0.1:3000'
    return redirect(frontend_redirect_url)

    # for debugging
    # return jsonify(session['TOKEN_INFO'])

@app.route('/me')
def test_token():
    access_token = get_token()
    if access_token:
        sp = spotipy.Spotify(auth=access_token)
        user_info = sp.me()
        response = jsonify(user_info), 200
        return response
    else:
        response = jsonify({'error' : 'failed to get access token'}), 401
        return response
    
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