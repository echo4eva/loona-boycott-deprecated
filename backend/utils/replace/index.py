# backend\utils\replace\index.py
from auth import spotify_client as sp
from ..artist_songs import loona_songs_dict as loona_songs
from ..show_items import loona_episodes_dict as loona_eps
from ..playlist_items import get_user_playlist_items

def replace_songs_with_ep(playlist_id: str):
    to_remove_id = []
    to_add_id = []

    user_songs = get_user_playlist_items(playlist_id)
    # print(user_songs)

    for song, song_ids in user_songs.items():
        if song in loona_songs:
            # print(song, " is here!")
            to_remove_id.extend(song_ids)
            to_add_id.append("spotify:episode:" + loona_eps[song])
    
    # print(to_remove_id)

    # Split in chunks to bypass Spotify API limit on removing and adding
    chunk_size = 100
    for i in range(0, len(to_remove_id), chunk_size):
        chunk = to_remove_id[i:i+chunk_size]
        sp.playlist_remove_all_occurrences_of_items(playlist_id=playlist_id, items=chunk)
    
    for i in range(0, len(to_remove_id), chunk_size):
        chunk = to_add_id[i:i+chunk_size]
        sp.playlist_add_items(playlist_id=playlist_id, items=chunk)