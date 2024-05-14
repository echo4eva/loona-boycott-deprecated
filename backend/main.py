# backend\main.py
from fastapi import FastAPI, Request, responses
from auth import get_spotify_client, get_spotify_auth

# uvicorn main:app --reload
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/login")
async def login():
    sp_auth = get_spotify_auth()
    auth_url = sp_auth.get_authorize_url()

    return responses.RedirectResponse(auth_url)

@app.get("/callback")
async def call_back(code: str):
    sp_auth = get_spotify_auth()
    token_info = sp_auth.get_access_token(code)
    access_token = token_info['access_token']
    
    return {"access token": access_token}

@app.get("/me")
def get_user_profile():
    pass

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}