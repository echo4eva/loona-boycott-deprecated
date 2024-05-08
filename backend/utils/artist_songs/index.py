# backend\utils\artist_songs\index.py
from auth import spotify_client as sp

def get_album_songs(album_id: str):
    """
    Get individual songs from an album

    - items: is a list of songs
    """
    album_songs = dict()
    
    # Get the first page of tracks
    results = sp.album_tracks(album_id=album_id)
    items = results["items"]
    
    # Check if there are more pages of tracks
    while results['next']:
        results = sp.next(results)
        items.extend(results['items'])

    for item in items:
        track_name = item["name"]
        track_id = item["id"]
        album_songs[track_id] = track_name

    return album_songs

def get_artists_songs(artist_id: str):
    """
    Gets all songs from an artist
    """
    artist_songs = dict()

    results = sp.artist_albums(artist_id=artist_id, album_type='album,single')
    albums = results['items']

    while results['next']:
        results = sp.next(results)
        albums.extend(results['items'])
        print("there is a next")

    # for every album, get their tracks
    for album in albums:
        album_id = album["id"]
        album_songs = get_album_songs(album_id)
        artist_songs.update(album_songs)
    
    return artist_songs

def get_all_loona_songs():
    """
    Hardcoded function to get a dictionary to hardcode
    so I don't have to call API everytime to get all songs from artist
    """
    loona_songs = dict()

    loona_id = "52zMTJCKluDlFwMQWmccY7"
    oec_id = "5KPaeBm0fVfCSZLydp9jdy"
    one_third_id = "4u9YxYzCjpMjnMcwNu9fzy"
    yyxy_id = "5JPKwLsHGaPIlxqHiF29e4"

    loona = get_artists_songs(loona_id)
    oec = get_artists_songs(oec_id)
    one_third = get_artists_songs(one_third_id)
    yyxy = get_artists_songs(yyxy_id)

    loona_songs.update(loona)
    loona_songs.update(oec)
    loona_songs.update(one_third)
    loona_songs.update(yyxy)

    print(loona_songs)

"""
HARDCODED DICTIONARY OF ALL SONGS
dictionary = {id: song name, ...}
"""
loona_songs_dict = {'4vRttrdGNoznz3dLAyhXmN': '12:00', '6gDWKVUuk9P01YTNow2kiP': 'Why Not?', '2JBJ2S5O6gpxMjHXbGbUlv': 'Voice', '3sw7CX1khKHUlFDPQP434V': 'Fall Again', '4yJSvxnj0wCPIG4VwU2XBJ': 'Universe', '13nnrv6b5V2vm0aARqEQgn': 'Hide & Seek', '7uHlXp4BaaVcoYcslvuGI2': 'OOPS!', '5ShU1AEd2oIGkTocr2zaWn': 'Star', '2iU7an5xjHihPBgMFXZjhR': 'X X', '6wNKKoUQfLPmch7cqSFytV': 'Butterfly', '7nbKBoLQ8ZiQ5Ge8vMPcgF': 'Satellite', '0dGoEd5azO9g3tKdONfBRZ': 'Curiosity', '5udzPjfCFLvrKvdu5TyGn6': 'Colors', '06uHelfNbaIX9rkJ4ggc51': 'Where you at', '37VXRNG3JmXOfWEB1liLjl': 'Stylish', '67eY6596UEynyZXoHZrnsj': 'Perfect Love', '18ZiN7QJZZHBjrgMRmZ9Ss': '열기(9)', '0YAHBaodj1YIoK0htcE6k6': 'favOriTe', '4EMAaWwu2zXTkXIA6YPKkt': 'Hi High', '6dXWpb09RGrZwfxVr9KGcT': '+ +', '55z4CHK595oo1sXngKXdGN': 'LUMINOUS', '6jF2XcaFFFiEZQS8E2ToEV': 'SICK LOVE', '3MZFdBPYCFCn1YQLV0s7Vl': 'Hi High - Japanese Ver.', '4h2fIodPmm0JCSp7VI8JGJ': 'SICK LOVE', '4hy2mxKZbnlQgfQaxHJV21': 'The Journey', '7cHXwaBnIBFUPuP376z07E': 'Flip That', '4V7sAUqroJrjmfrbANLGra': 'Need U', '2BdGXQ4MjeYCZ9JNte85Q4': 'POSE', '65Q3dBSnGq6rRGh7szSWYm': 'Pale Blue Dot', '6m81zUhuw7mVp37OummGgw': 'Playback', '70HOn7S07x4fvvrt8lKRbT': 'Don`t Go - Queendom2 Version', '2YVzshKzFglQLBXPYNpGI8': 'HULA HOOP', '7IgkCiHFhpm8KwTgDa2eO3': 'StarSeed 〜カクセイ〜', '0cdDgFpP63lWj0C29zJ15s': 'PTT（Paint The Town） - Japanese Ver.', '0nwgVSZaSkxUUjy8mYwVq8': 'HULA HOOP - City Pop Ver.', '4eEI7fEoKgZyoUgq48tsjd': '&', '5awNIWVrh2ISfvPd5IUZNh': 'PTT (Paint The Town)', '4ZsSeCSgARNHlLa69ejGzz': 'WOW', '7733b9hgMqNkq4DBfU8cz6': 'Be Honest', '7jVQ1WS5RqUxRaKQVRaokc': 'Dance On My Own', '676qfSjSg2f0Qo98tl1CpR': 'A Different Night', '4iFf7g2UuvdzKjbPqUR5uI': 'U R', '2WAYPejv44bmgl7qQVPVW6': 'PTT（Paint The Town） - Japanese Ver.', '0g4EXf2GxjePFGl6EXnGFZ': '#', '1ry2mTVmAJHbNLzl5qww5v': 'So What', '1W9fuK1bUimZRvyckkQR05': 'Number 1', '5l8Vpgx92aqAuniKsSKbyZ': 'Oh (Yes I Am)', '5wXl54GxirvUdS9ne70mC7': 'Ding Ding Dong', '2qqDqqdnSQPR9lOTUs3YUi': '365', '1FJPXCXDD9yt9naw8R5bfs': '365', '2h4zPgT1Den4BZKWMX6tmU': '+ +', '3gKTvPS563VgdTL4oDHQ2Z': 'Hi High', '04xRuLRx53ROPx6GaBj5k6': 'favOriTe', '3Hwg1j58X82pgKvptLwDFG': '열기', '6GoDM3iFXPZQITvwOUz1yS': 'Perfect Love', '2IKsQTB52Wex5eFyNFHJKN': 'Stylish', '57CWpEu3MKVrobqeHl0zZf': 'favOriTe', '5UUeEljsNQroCUNId8DIV6': 'Egoist (Olivia Hye)', '6cfacimNXWogsp6DtJflyL': 'Rosy (고원, Olivia Hye)', '1DzpZ8HBR0MgGkZDhAdd7f': 'One & Only (Go Won)', '1tLmp8dEhaHvU0jm2aG6sS': 'See Saw (Chuu, Go Won)', '6Ul4x5pyNZqi4OvTjEtH8V': 'Heart Attack (츄)', '0wGSyd97w2CU2AvGZ4MgdS': "Girl's Talk (이브, 츄)", '5gkbQEgYlXajuf8CcYpojE': 'The Carol 2.0 (ViVi, Choerry, Yves)', '7eUtsnBNOWfWDObBZyU4F4': 'new', '4ddaY4PJxvq47qIps1KQ6Q': 'D-1', '0JnwBhEJOwvtHxbCplWwGz': 'Love Cherry Motion', '05giLqSQDArF3euc2EhNjw': 'Puzzle', '1uNTfm5WZVGdig95SAXajH': 'Singing in the Rain', '3GAKRdjL6Snq9C7u5tMC01': 'Love Letter', '3DGKXLtVjawKFweymvHn84': '키스는 다음에', '7vgLNwdUzUQelOr9aacuxA': 'My Sunday', '6f1PlxNaKfbbBosoRXmoAF': 'My Melody', '1gHIOHn4plsaFam4lTS96Q': '키스는 다음에', '1IEGeQZD2By2YKow9pgqDU': 'My Sunday', '4jfrzP6MkChOkHDpPptKS8': 'My Melody', '2jvTBj2oSJi3fij1WH1AJR': 'The Carol', '0KsPxLQtEvfb04Sx1pmUsL': '소년, 소녀', '64bAqsPFa6xDWQ7t24ZSSp': "I'll Be There", '7FRZUHPUHLgAFHVUk5ryqz': '다녀가요', '2YKbeTKBCPBFypzJ8I6XbP': 'ViViD', '6Zx8b5jkkPgUWYNwmsdZUq': 'ViViD - Acoustic Mix Version', '0BLHmjFCZsiWQfeRFj6Pc2': 'ADD', '0vP1o3CY4I8EnMQChYPgHu': 'Sweet Crazy Love', '5MwA1bgPR2rGGRDqCuXYaI': 'Uncover', '08gpF9fiPvxfjQCwnQdzgS': 'Girl Front', '1mTdL5A5cF3gJqwK0SXOQ2': 'LOONATIC', '3tzvNHyKc75uFRw98sBcMi': 'Chaotic', '6Jfr8kDlEx6LnKnp4Xd3yT': 'Starlight', '7cSbCH6UlmdTTYqtb92MlH': 'ODD Front', '1Fh66I6X7Me2HWqSXwYvZh': 'LOONATIC - Eng. Ver.', '3GRwM20EPVWjKoVsNsHjrj': 'ODD', '6hDCBYBnbr4lfRj5H7bkC4': 'Girl Front', '7h9wP4yMYuFdiciHMsdxWU': 'LOONATIC', '1s8ZMgjthh2IGvYKWdgO2B': 'Chaotic', '0DRvlkPs5FKt6Rh9q4B6Nh': 'Starlight', '5DLOuYYn9QiwjYHYaxVVmx': 'Love & Evil', '41jbCSLDcNYRrB2QdmRGZ7': 'Sonatine', '6LTGZpSy9qs2YlWoaGZgiX': 'Rain 51db', '4TocMZ25EO24fdxxOKMRHQ': 'Love & Live', '6XkQh3wi7VD5XziRGUFuGs': 'You and Me Together', '6UFwnR81gaEIrwILz5lyHm': 'Fairy Tale', '4tE7Hk4xfeaLbYeelkKkOI': 'Valentine Girl', '1vFgGSZOjdomaUakHJi3oB': 'Into the New Heart', '1qOLmP7sv0JgMsyrtM5abd': 'Love & Live', '60CamYLx3dnpHjG8KGDzyq': 'You and Me Together', '0znW2d5md1KOiZg8Wfu2XU': 'Fairy Tale', '08JjmBX616ab0JvtrulPfQ': 'Valentine Girl', '2GkF0nk8gmLYru7UZcZA9K': 'dal segno', '4rKEmhNA19JezqVsSQS4yo': 'love4eva (feat. Grimes)', '5zNzvVBEuk8EEQslNTe42B': 'frozen', '0ZoFCxoLfn2uKunJbm4ERr': 'one way', '3jueKDWC9DmTfnU2jMxE8U': 'rendezvous 18.6y'}