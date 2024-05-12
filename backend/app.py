# backend/app.py
from auth import spotify_client as sp
from utils.playlist_items import get_user_playlist_items
from utils.artist_songs import get_album_songs, get_artists_songs, loona_songs_dict as loona_songs, get_all_loona_songs
from utils.show_items import get_episodes, loona_episodes_dict as loona_episodes
from utils.replace import replace_songs_with_ep

# https://open.spotify.com/playlist/2IHjQHNDmDJgaDO1Zb2Awu?si=bc94f0da58114a05 - loona
# https://open.spotify.com/playlist/563dtXdul1CzsAHmegOxLS?si=4ef14a04fc3749a3 - test small
# https://open.spotify.com/playlist/1f7Zfu4uf5rAlpWoX5R4vA?si=a8820990cd1c4e46 - test 300
# https://open.spotify.com/playlist/3z8RkYc7me0p9jUcBRJshM?si=fd29bbc37d9e4bc0 - weird ones
# https://open.spotify.com/playlist/1VWVekcOvgOQOGrfJueTap?si=45c68523c05b4b04 - all loona clean dupes
def test_get_playlist_songs(playlist_id: str):
    get_user_playlist_items(playlist_id)

# https://open.spotify.com/artist/52zMTJCKluDlFwMQWmccY7?si=0XzdrZHATsO54HCU-gPZLw - loona
# https://open.spotify.com/artist/5KPaeBm0fVfCSZLydp9jdy?si=N2BzaC7FQPaBvyJuBXW2qQ - oec
# https://open.spotify.com/artist/4u9YxYzCjpMjnMcwNu9fzy?si=eiNi8tfaSCuK_qwvFBkk6g - 1/3
# https://open.spotify.com/artist/5JPKwLsHGaPIlxqHiF29e4?si=urieC31XSRmyKhOF8AYqWA - yyxy
def test_get_artist_songs(artist_id: str):
    print(get_artists_songs(artist_id))
    pass

# https://open.spotify.com/album/747FhjbZXy5H8frCZ90eDv?si=j2ZqpeNIRDa0Vc0wvUGiIg
def get_songs_from_album(album_id: str):
    get_album_songs(album_id)

# https://open.spotify.com/show/1pjU1f2PfoIf4NS3eYT925?si=dfc309fa91004d69
def test_get_episodes_from_show(show_id: str):
    print(get_episodes(show_id))

# https://open.spotify.com/playlist/62Fi7ebGvquiSEY2jtHOBX?si=8d311be48b6947c4
# https://open.spotify.com/playlist/62Fi7ebGvquiSEY2jtHOBX?si=b19c5aba597a422b
# https://open.spotify.com/playlist/05LoDrNr2K5hBI6pacgDQq?si=410a7c84d06543da
# https://open.spotify.com/playlist/05LoDrNr2K5hBI6pacgDQq?si=a271eecfd9ed4003
# https://open.spotify.com/playlist/6cMxeISW5ozHanN7g9vKOQ?si=298d8c9ce57c4098
# https://open.spotify.com/playlist/3BmL33mEM1wZSo6VdFqwuq?si=eca6bb8efbd94358 - test3
# https://open.spotify.com/playlist/603yyqn7eHkHC5ivgM0QPY?si=5501fd870dcb403a - final test
# https://open.spotify.com/playlist/6iJbS24vIDwaXlJj8FF4sd?si=2d19ba1b0cfd4f50 -  all loona test 1
# https://open.spotify.com/playlist/69Gah7Afxla1eHtAtZzukQ?si=b1744cdd48314353 - myne
def test_replace(playlist_id: str):
    replace_songs_with_ep(playlist_id)
    
def main():
    # test_get_playlist_songs("1VWVekcOvgOQOGrfJueTap")
    # test_get_playlist_songs("3z8RkYc7me0p9jUcBRJshM")
    # test_get_episodes_from_show("1pjU1f2PfoIf4NS3eYT925")
    test_replace("69Gah7Afxla1eHtAtZzukQ")

main()