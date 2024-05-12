# backend/utils/playlist/index.py
from auth import spotify_client as sp
import json

def get_user_playlist_items(playlist_id: str):
    songs = dict()

    results = sp.playlist_items(playlist_id=playlist_id, additional_types=["track", "episode"])
    items = results['items']

    # Check if there are more items to retrieve
    while results['next']:
        results = sp.next(results)
        items.extend(results['items'])
    
    # print(items)
    
    for item in items:
        # print(item)
        track_name = item['track']['name']
        track_id = item['track']['id']
        if track_name in songs:
            songs[track_name].append(track_id)
        else:
            songs[track_name] = [track_id]
    
    # json_string = json.dumps(songs, indent=4, ensure_ascii=False)
    # print(json_string.encode('utf-8').decode('utf-8'))

    return songs