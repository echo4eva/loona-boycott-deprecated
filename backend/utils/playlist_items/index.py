# backend/utils/playlist/index.py
from auth import spotify_client as sp

def get_user_playlist_items(playlist_id: str):
    songs = dict()
    # fields_list = ["items.track.name", "items.track.id"]
    # fields_list = ["items"]
    # fields = ",".join(fields_list)

    results = sp.playlist_items(playlist_id=playlist_id)
    items = results['items']

    # Check if there are more items to retrieve
    while results['next']:
        results = sp.next(results)
        items.extend(results['items'])
    
    for item in items:
        track_name = item["track"]["name"]
        track_id = item["track"]["id"]
        songs[track_name] = track_id

    return songs