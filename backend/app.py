# backend/app.py
from auth import spotify_client as sp
from utils.playlist_items import get_user_playlist_items
from utils.artist_songs import get_album_songs, get_artists_songs
from utils.show_items import get_episodes

# https://open.spotify.com/playlist/2IHjQHNDmDJgaDO1Zb2Awu?si=bc94f0da58114a05 - loona
# https://open.spotify.com/playlist/563dtXdul1CzsAHmegOxLS?si=4ef14a04fc3749a3 - test small
# https://open.spotify.com/playlist/1f7Zfu4uf5rAlpWoX5R4vA?si=a8820990cd1c4e46 - test 300
def test_get_playlist_songs(playlist_id: str):
    print(get_user_playlist_items(playlist_id))

# https://open.spotify.com/artist/52zMTJCKluDlFwMQWmccY7?si=0XzdrZHATsO54HCU-gPZLw - loona
# https://open.spotify.com/artist/5KPaeBm0fVfCSZLydp9jdy?si=N2BzaC7FQPaBvyJuBXW2qQ - oec
# https://open.spotify.com/artist/4u9YxYzCjpMjnMcwNu9fzy?si=eiNi8tfaSCuK_qwvFBkk6g - 1/3
# https://open.spotify.com/artist/5JPKwLsHGaPIlxqHiF29e4?si=urieC31XSRmyKhOF8AYqWA - yyxy
def test_get_artist_songs(artist_id: str):
    print(len(get_artists_songs(artist_id)))
    pass

# https://open.spotify.com/album/747FhjbZXy5H8frCZ90eDv?si=j2ZqpeNIRDa0Vc0wvUGiIg
def get_songs_from_album(album_id: str):
    get_album_songs(album_id)

# https://open.spotify.com/show/1pjU1f2PfoIf4NS3eYT925?si=dfc309fa91004d69
def test_get_episodes_from_show(show_id: str):
    get_episodes(show_id)
    
def main():
    # test_get_playlist_songs("1pjU1f2PfoIf4NS3eYT925")
    test_get_episodes_from_show("1pjU1f2PfoIf4NS3eYT925")

main()