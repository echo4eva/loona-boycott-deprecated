from auth import spotify_client as sp
from ..artist_songs import loona_songs_dict as loona_songs
from ..show_items import loona_episodes_dict as loona_eps
from ..playlist_items import get_user_playlist_items

def replace_songs_with_ep(playlist_id: str):
    to_remove_id = []
    to_add_id = []

    user_songs = get_user_playlist_items(playlist_id)
    # print(user_songs)

    for song in user_songs:
        user_song_id = user_songs[song]
        print(song)
        if user_song_id in loona_songs:
            print(song, " is herege!")
            to_remove_id.append(user_song_id)
            to_add_id.append("spotify:episode:" + loona_eps[song])

    print(to_remove_id)
    print(to_add_id)

    sp.playlist_remove_all_occurrences_of_items(playlist_id=playlist_id, items=to_remove_id)
    sp.playlist_add_items(playlist_id=playlist_id, items=to_add_id)

