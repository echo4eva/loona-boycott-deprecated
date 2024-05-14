# backend\main.py
from flask import Flask, redirect, request, jsonify, session
from auth import get_spotify_auth
from dotenv import load_dotenv

load_dotenv()
import os

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')

@app.route("/")
def read_root():
    return "<p>Hello, World</p>"

@app.route("/login")
def login():
    sp_auth = get_spotify_auth()
    auth_url = sp_auth.get_authorize_url()

    return redirect(auth_url)

@app.route("/callback")
def call_back():
    code = request.args.get('code')
    sp_auth = get_spotify_auth()
    token_info = sp_auth.get_access_token(code)
    
    session['TOKEN_INFO'] = token_info
    
    return session['TOKEN_INFO']

if __name__ == "__main__":
    app.run(debug=True)