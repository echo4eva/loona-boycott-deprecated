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
        if track_name in album_songs:
            album_songs[track_name].append(track_id)
        else:
            album_songs[track_name] = [track_id]

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

should be {name : id}
"""
# loona_songs_dict = {'ViViD (Acoustic Ver.)': '0Egf0suvZSOB3bet2rLWGX', 'I’ll be There': '2cCj7bIY0jrdGn20lq88ae', 'Around You': '2Tf6La0o3Jqu7HfKwkWqjJ', 'Let Me In': '3Ir6BUnlnAGTMZBMIHlgSu', 'Kiss Later': '4TeqecANyRsllKmXNw641W', 'Everyday I Love You (feat. HaSeul)': '5e6Tii9571q3uKOC6wn8XU', 'Everyday I Need You (feat. JinSoul)': '6y0g4cJTSABiaaKECOISiI', 'Into the New Heart (Guitar by JungMo)': '7EG2HkWMW1mM7PIMznLyhW', 'Eclipse (Prod. By Daniel Obi Klein)': '6k3sl3Hs6bNN497d672gpR', 'Eclipse': '3y3gnrkETEr90Zpe6fNuOt', 'Twilight (Prod. By Cha Cha Malone)': '0Eh58SEH7NMUS5r6saQ7W7', 'Twilight': '1twEuszaJqYVaUhXgkUtEZ', 'Singing in the Rain': '6ZCugHZvchMlF6DqMDYIW1', 'Love Letter': '3t7m1KLkT2aPvqyzVRnTBy', 'Butterfly': '5jhYykolbcG1T9wZSyvhp5', 'PTT (Paint The Town)': '5awNIWVrh2ISfvPd5IUZNh', 'Not Friends (ALAWN REMIX)': '4JMSZR1HhsOyMm8JwXdYPX', 'Not Friends (TIDO REMIX)': '2GH8QibZN3lChxaIYjPdSw', 'Not Friends (ORBIT REMIX)': '3nSd7w3aOfhAoGxVZuUY7X', 'Not Friends ORIGINAL MIX': '0T6MBcbl5Y6stcLWorNQQ2', 'SHAKE IT': '1ezubi9SlRqI3fHoGXjuP7', 'Tell me now': '2kIYgg1tOBTjs7XLZNwuSs', 'POSE': '6L22JhubMtyZNBEFuzeZKB', '12:00': '4vRttrdGNoznz3dLAyhXmN', 'Why Not?': '6gDWKVUuk9P01YTNow2kiP', 'Voice': '2JBJ2S5O6gpxMjHXbGbUlv', 'Fall Again': '3sw7CX1khKHUlFDPQP434V', 'Universe': '4yJSvxnj0wCPIG4VwU2XBJ', 'Hide & Seek': '13nnrv6b5V2vm0aARqEQgn', 'OOPS!': '7uHlXp4BaaVcoYcslvuGI2', 'Star': '5ShU1AEd2oIGkTocr2zaWn', 'X X': '2iU7an5xjHihPBgMFXZjhR', 'Satellite': '7nbKBoLQ8ZiQ5Ge8vMPcgF', 'Curiosity': '0dGoEd5azO9g3tKdONfBRZ', 'Colors': '5udzPjfCFLvrKvdu5TyGn6', 'Where you at': '06uHelfNbaIX9rkJ4ggc51', 'Stylish': '2IKsQTB52Wex5eFyNFHJKN', 'Perfect Love': '6GoDM3iFXPZQITvwOUz1yS', '열기(9)': '18ZiN7QJZZHBjrgMRmZ9Ss', 'favOriTe': '57CWpEu3MKVrobqeHl0zZf', 'Hi High': '3gKTvPS563VgdTL4oDHQ2Z', '+ +': '2h4zPgT1Den4BZKWMX6tmU', 'You and Me Together': '60CamYLx3dnpHjG8KGDzyq', 'LUMINOUS': '55z4CHK595oo1sXngKXdGN', 'SICK LOVE': '4h2fIodPmm0JCSp7VI8JGJ', 'Hi High - Japanese Ver.': '3MZFdBPYCFCn1YQLV0s7Vl', 'The Journey': '4hy2mxKZbnlQgfQaxHJV21', 'Flip That': '7cHXwaBnIBFUPuP376z07E', 'Need U': '4V7sAUqroJrjmfrbANLGra', 'Pale Blue Dot': '65Q3dBSnGq6rRGh7szSWYm', 'Playback': '6m81zUhuw7mVp37OummGgw', 'Don`t Go - Queendom2 Version': '70HOn7S07x4fvvrt8lKRbT', 'HULA HOOP': '2YVzshKzFglQLBXPYNpGI8', 'StarSeed 〜カクセイ〜': '7IgkCiHFhpm8KwTgDa2eO3', 'PTT（Paint The Town） - Japanese Ver.': '2WAYPejv44bmgl7qQVPVW6', 'HULA HOOP - City Pop Ver.': '0nwgVSZaSkxUUjy8mYwVq8', '&': '4eEI7fEoKgZyoUgq48tsjd', 'WOW': '4ZsSeCSgARNHlLa69ejGzz', 'Be Honest': '7733b9hgMqNkq4DBfU8cz6', 'Dance On My Own': '7jVQ1WS5RqUxRaKQVRaokc', 'A Different Night': '676qfSjSg2f0Qo98tl1CpR', 'U R': '4iFf7g2UuvdzKjbPqUR5uI', '#': '0g4EXf2GxjePFGl6EXnGFZ', 'So What': '1ry2mTVmAJHbNLzl5qww5v', 'Number 1': '1W9fuK1bUimZRvyckkQR05', 'Oh (Yes I Am)': '5l8Vpgx92aqAuniKsSKbyZ', 'Ding Ding Dong': '5wXl54GxirvUdS9ne70mC7', '365': '1FJPXCXDD9yt9naw8R5bfs', '열기': '3Hwg1j58X82pgKvptLwDFG', 'Egoist (Olivia Hye)': '5UUeEljsNQroCUNId8DIV6', 'Rosy (고원, Olivia Hye)': '6cfacimNXWogsp6DtJflyL', 'One & Only (Go Won)': '1DzpZ8HBR0MgGkZDhAdd7f', 'See Saw (Chuu, Go Won)': '1tLmp8dEhaHvU0jm2aG6sS', 'Heart Attack (츄)': '6Ul4x5pyNZqi4OvTjEtH8V', "Girl's Talk (이브, 츄)": '0wGSyd97w2CU2AvGZ4MgdS', 'The Carol 2.0 (ViVi, Choerry, Yves)': '5gkbQEgYlXajuf8CcYpojE', 'new': '7eUtsnBNOWfWDObBZyU4F4', 'D-1': '4ddaY4PJxvq47qIps1KQ6Q', 'Love Cherry Motion': '0JnwBhEJOwvtHxbCplWwGz', 'Puzzle': '05giLqSQDArF3euc2EhNjw', 'Everyday I Love You': '2z81SECbY31aro8nTm53w2', 'Everyday I Need You': '7f4qrgfoJYyriW4dq46sg8', '키스는 다음에': '1gHIOHn4plsaFam4lTS96Q', 'My Sunday': '1IEGeQZD2By2YKow9pgqDU', 'My Melody': '4jfrzP6MkChOkHDpPptKS8', 'The Carol': '2jvTBj2oSJi3fij1WH1AJR', '소년, 소녀': '0KsPxLQtEvfb04Sx1pmUsL', "I'll Be There": '64bAqsPFa6xDWQ7t24ZSSp', "I'll be There": '', '다녀가요': '7FRZUHPUHLgAFHVUk5ryqz', 'ViViD': '2YKbeTKBCPBFypzJ8I6XbP', 'ViViD - Acoustic Mix Version': '6Zx8b5jkkPgUWYNwmsdZUq', 'ViViD (Acoustic Ver.)': '0Egf0suvZSOB3bet2rLWGX', 'ADD': '0BLHmjFCZsiWQfeRFj6Pc2', 'Sweet Crazy Love': '0vP1o3CY4I8EnMQChYPgHu', 'Uncover': '5MwA1bgPR2rGGRDqCuXYaI', 'Girl Front': '6hDCBYBnbr4lfRj5H7bkC4', 'LOONATIC': '7h9wP4yMYuFdiciHMsdxWU', 'Chaotic': '1s8ZMgjthh2IGvYKWdgO2B', 'Starlight': '0DRvlkPs5FKt6Rh9q4B6Nh', 'ODD Front': '7cSbCH6UlmdTTYqtb92MlH', 'LOONATIC - Eng. Ver.': '1Fh66I6X7Me2HWqSXwYvZh', 'ODD': '3GRwM20EPVWjKoVsNsHjrj', 'Love & Evil': '5DLOuYYn9QiwjYHYaxVVmx', 'Sonatine': '41jbCSLDcNYRrB2QdmRGZ7', 'Rain 51db': '6LTGZpSy9qs2YlWoaGZgiX', 'Love & Live': '1qOLmP7sv0JgMsyrtM5abd', 'Fairy Tale': '0znW2d5md1KOiZg8Wfu2XU', 'Valentine Girl': '08JjmBX616ab0JvtrulPfQ', 'Into the New Heart': '1vFgGSZOjdomaUakHJi3oB', 'dal segno': '2GkF0nk8gmLYru7UZcZA9K', 'love4eva (feat. Grimes)': '4rKEmhNA19JezqVsSQS4yo', 'frozen': '5zNzvVBEuk8EEQslNTe42B', 'one way': '0ZoFCxoLfn2uKunJbm4ERr', 'rendezvous 18.6y': '3jueKDWC9DmTfnU2jMxE8U'}
loona_songs_dict = {'ViViD': ['4STsLimXfiydKp7WwJYoFh', '2YKbeTKBCPBFypzJ8I6XbP', '1P2oYaTIBRB4pYL28Ps5Mv', '5UcKA3kFDFze29N8qrV804'], 'ViViD (Acoustic Ver.)': ['0Y8wd59ekQxkcSN9lyMG7A', '0Egf0suvZSOB3bet2rLWGX'], 'I’ll Be There (HeeJin, HyunJin)': ['38s2E3OM2UJY6EO8siwz81'], 'Around You': ['5hKU02nIlA7m5G0tHFZueF', '2Tf6La0o3Jqu7HfKwkWqjJ'], 'The Carol (LOONA‚ HaSeul)': ['3lLoJVI9eif5kAsL4rk8um'], 'Let Me In (HaSeul)': ['0vziFOaBxXNZaVG9pLXfQq'], 'Kiss Later (YeoJin)': ['6WLfBd2KFL8iuU57qy9HqI'], 'My Sunday (HeeJin‚ HyunJin)': ['0ij8esbxdXCUIUfcKwfzJu'], 'My Melody (HaSeul‚YeoJin)': ['5jfEwcinJx9m2tQlYwL644'], 'Love & Evil': ['3307jEqptKGpAa3THFheVu', '0HT726L1FN7csp0DmTfwhU', '6XAca0QIiTvMaWfTnjjwrn'], 'Sonatine': ['2e8qWdt5W3wWxAs3L3DRqJ', '6LOPo5liG9RE6pBKTVUoEm', '6RMFRrVjtcvpyyBs6cM0xd'], 'Rain 51db': ['5n7igdr3vMrBA8tUTEqDyd', '3WALXPWdol0F0quHImXEYm', '0y6mgjArFlmksW6Qciycd5'], 'Love & Live': ['5IOZOsb4Y8K90YC54oKm3n', '1qOLmP7sv0JgMsyrtM5abd', '7uAD8DLwFDpZkFEJFSxxcb'], 'You and Me Together': ['1KxfMKXJdkr7vMAvFnlw3s', '60CamYLx3dnpHjG8KGDzyq', '2yIcpjnvw0ihKxHqWNFIuz'], 'Fairy Tale': ['4KwPYWo3LWjAuHMQeQ2KgU', '0znW2d5md1KOiZg8Wfu2XU', '0AH0dkzF93dcHFnmeBOTbE'], 'Valentine Girl': ['4SLf5mA4iIPTgN9GwS1Ot1', '08JjmBX616ab0JvtrulPfQ', '54aMoZIU4kF8o4MbIEObls'], 'Everyday I Love You (Feat. HaSeul) (ViVi)': ['308axn5I8B398prJ8kuac6'], 'Everyday I Need You (Feat. JinSoul) (ViVi)': ['652eEVQkB5nmyLgu9ylmfl'], 'Eclipse (Prod. by Daniel Obi Klein) (Kim Lip)': ['1GG5C0ugHo4OWjZUSe0zgp'], 'Twilight (Prod. by Cha Cha Malone) (Kim Lip)': ['7plTNMglT8GI4bqptvMHMh'], 'Singing in the Rain (JinSoul)': ['2wSKuveB7iYLSOg7qeldzj'], 'Love Letter (Kim Lip‚ JinSoul)': ['1B4ZWnHelZoizJnWzmSzwy'], 'Love Cherry Motion': ['1H3i6WXxrJB7LEoH5iStvb', '0JnwBhEJOwvtHxbCplWwGz'], 'Puzzle': ['0Y1oSjd9U7Qy5t7EDjAjPq', '05giLqSQDArF3euc2EhNjw'], 'ADD': ['4NzNeHybw9rIbbRb7ztgfm'], 'Sweet Crazy Love': ['5fgpCIjBJ098E9zqN9DS87'], 'Uncover': ['2oFbMd0TcgUm7Df4Sx16h9'], 'Girl Front': ['5OnchRw2yAuIAwp2RYLCBa', '6hDCBYBnbr4lfRj5H7bkC4'], 'LOONATIC': ['2FwFu6y1aXPWXWcD9RxA6v', '7h9wP4yMYuFdiciHMsdxWU'], 'Chaotic': ['4wOXL5AcwYT1Lc8IuqZfot', '1s8ZMgjthh2IGvYKWdgO2B'], 'Starlight': ['7hhXSyozEb30vG4dqzqQBv', '0DRvlkPs5FKt6Rh9q4B6Nh'], 'ODD Front': ['0ZsRFf3jsn4MvGHUoIcKLy'], 'new': ['7eUtsnBNOWfWDObBZyU4F4'], 'D-1': ['4ddaY4PJxvq47qIps1KQ6Q'], 'The Carol 2.0 (ViVi, Choerry, Yves)': ['5gkbQEgYlXajuf8CcYpojE'], 'Heart Attack (츄)': ['6SSC9KZQaxBdyipKRigrFC'], "Girl's Talk (이브, 츄)": ['1j3zXAq0W9cLIpiAXwcYXF'], 'One & Only (Go Won)': ['1DzpZ8HBR0MgGkZDhAdd7f', '6Wm4jenbkewv06BThVE7AI'], 'See Saw (Chuu, Go Won)': ['1tLmp8dEhaHvU0jm2aG6sS', '0ictXriMERBYpJmiKZxfi3'], 'Egoist (Olivia Hye)': ['5UUeEljsNQroCUNId8DIV6'], 'Rosy (고원, Olivia Hye)': ['6cfacimNXWogsp6DtJflyL'], 'dal segno': ['2GkF0nk8gmLYru7UZcZA9K', '797hb03Idz6rt4b1iSVXN4'], 'love4eva (feat. Grimes)': ['4rKEmhNA19JezqVsSQS4yo', '4oyPrhe8R8zpCSEcaZEDFD'], 'frozen': ['5zNzvVBEuk8EEQslNTe42B', '5IukD2TIEAGzfkoMYPRfh3'], 'one way': ['0ZoFCxoLfn2uKunJbm4ERr', '76mhBGKysOJOU1vXFEhDB5'], 'rendezvous 18.6y': ['3jueKDWC9DmTfnU2jMxE8U', '4HLDTUXRcGqVWV2nW5zWwd'], '+ +': ['0ywnB1ANtBR7RTT1uBpBZO'], 'Hi High': ['0RqzUS7AkBhQDrBxcGFeDv'], 'favOriTe': ['570A5teOwKNMPN7bboi8T4', '2hynpFtQsg5wqVevY8z6G7'], '열기': ['72NewffMWAO9kH55vT6dXj'], 'Perfect Love': ['1ILLB5uvWk1lQJOY7q645K'], 'Stylish': ['0vA82YPx1q4JRWFISf1vIZ'], 'X X': ['4TgYBLdExSoISFOfWLmBOh', '2iU7an5xjHihPBgMFXZjhR'], 'Butterfly': ['5jhYykolbcG1T9wZSyvhp5', '6wNKKoUQfLPmch7cqSFytV', '2PgfMrrprDO5kwwfpPzfvm'], 'Satellite': ['644aVns0mIqtLY9Wqzm7zD', '7nbKBoLQ8ZiQ5Ge8vMPcgF'], 'Curiosity': ['6Kke9MonigeJKLSmlmRnWD', '0dGoEd5azO9g3tKdONfBRZ'], 'Colors': ['1bg4MF45JFU0Dx1MjLJ5vn', '5udzPjfCFLvrKvdu5TyGn6'], 'Where you at': ['6OcDMIYoDm0DvybUM1jBWF', '06uHelfNbaIX9rkJ4ggc51'], '365': ['1FJPXCXDD9yt9naw8R5bfs', '3AAu0viADpL0jFsRzOrlmR'], '#': ['3Q4eFdGe02tM0whH8AH4F0', '0g4EXf2GxjePFGl6EXnGFZ'], 'So What': ['7w3pIUjz7BTTqj9uAws40m', '1ry2mTVmAJHbNLzl5qww5v'], 'Number 1': ['2GGzUBEJE1dN2PHrf7neS7', '1W9fuK1bUimZRvyckkQR05'], 'Oh (Yes I Am)': ['0WdCXlXSSfpIldlzZ4BrHi', '5l8Vpgx92aqAuniKsSKbyZ'], 'Ding Ding Dong': ['4bPY0n3hMVd6q39B2ePkZe', '5wXl54GxirvUdS9ne70mC7'], '12:00': ['2iv1U6ulyjUIWJPSlrawHN', '4kTM6FHd4rJ94pgXpgxq4n'], 'Why Not?': ['6yGQ86UppYULzTCxAWgwVN', '227y7s5IZ5TWN17Pkte5tc'], 'Voice': ['6tIKSYUpxyOOhE4OPDXjNi', '3RIBc0xd2STgLZKwzGskH7'], 'Fall Again': ['5t6ffoqxXwydvNlYC3niot', '3fCjr9vv9VK6xbqSm4QDaj'], 'Universe': ['3lVzntD100XcGaW3HZ5FuU', '6tGl0s9NstDi2JK45gf7n3'], 'Hide & Seek': ['5QZHS9YzYpNDY8nmG2h64N', '7A09W2N30JI3KncOCufbI6'], 'OOPS!': ['1PI5Nlv1bJESN0H1wBa7Pe', '59wNSk5SUZJrVRtrHafdDG'], 'Star': ['4wGt2KmqMQ7LC5bqPi51sf'], '&': ['4eEI7fEoKgZyoUgq48tsjd'], 'PTT (Paint The Town)': ['5awNIWVrh2ISfvPd5IUZNh', '0MEJznR74sW0mnSnkbiQia'], 'WOW': ['4ZsSeCSgARNHlLa69ejGzz'], 'Be Honest': ['7733b9hgMqNkq4DBfU8cz6'], 'Dance On My Own': ['7jVQ1WS5RqUxRaKQVRaokc'], 'A Different Night': ['676qfSjSg2f0Qo98tl1CpR'], 'U R': ['4iFf7g2UuvdzKjbPqUR5uI'], 'Not Friends (Sung by HeeJin, Kim Lip, JinSoul, Yves) (Prod. RYAN JHUN)': ['0kgNAZLjWVm7YSnrmoBLa3'], 'HULA HOOP': ['2YVzshKzFglQLBXPYNpGI8'], 'StarSeed 〜カクセイ〜': ['7IgkCiHFhpm8KwTgDa2eO3'], 'PTT（Paint The Town） - Japanese Ver.': ['0cdDgFpP63lWj0C29zJ15s', '2WAYPejv44bmgl7qQVPVW6'], 'HULA HOOP - City Pop Ver.': ['0nwgVSZaSkxUUjy8mYwVq8'], 'The Journey': ['4hy2mxKZbnlQgfQaxHJV21'], 'Flip That': ['7cHXwaBnIBFUPuP376z07E'], 'Need U': ['4V7sAUqroJrjmfrbANLGra'], 'POSE': ['2BdGXQ4MjeYCZ9JNte85Q4', '6L22JhubMtyZNBEFuzeZKB'], 'Pale Blue Dot': ['65Q3dBSnGq6rRGh7szSWYm'], 'Playback': ['6m81zUhuw7mVp37OummGgw'], 'SICK LOVE': ['4h2fIodPmm0JCSp7VI8JGJ'], 'LUMINOUS': ['5LORlaKLGzAAxeIeqxYxPd'], 'ViViD - Acoustic Mix Version': ['6Zx8b5jkkPgUWYNwmsdZUq', '3w9DXhZIfOJpStUSkLHxWg'], "I'll Be There": ['1z1nsNEnhzTfH3CX7fcsaz'], '다녀가요': ['5ugtjxSBLylCYzfVcJTLMw'], 'The Carol': ['26rb1fSEyuFGHvDGgIGjts', '2jvTBj2oSJi3fij1WH1AJR', '1CKJ1nmAYp1XD4ZajfhzIC'], '소년, 소녀': ['43Tga9iFJSfuk8FqKSoXlG', '0KsPxLQtEvfb04Sx1pmUsL'], '키스는 다음에': ['1gHIOHn4plsaFam4lTS96Q', '3DGKXLtVjawKFweymvHn84'], 'My Sunday': ['1IEGeQZD2By2YKow9pgqDU', '7vgLNwdUzUQelOr9aacuxA', '0oiVMsDM40biyMxhF1ooI0'], 'My Melody': ['4jfrzP6MkChOkHDpPptKS8', '6f1PlxNaKfbbBosoRXmoAF', '3uOuaBpMHwYcxej5qRDocD'], 'Into the New Heart': ['1vFgGSZOjdomaUakHJi3oB'], 'Everyday I Love You': ['5HGeTj4lVdLGed5c358q1f'], 'Everyday I Need You': ['089ima1riL9o88kUlCgFCp'], 'Eclipse': ['26K21MUaPDTnzHqtiiffFv'], 'Twilight': ['1QzbeeShhAATdT87ssWtK4'], 'Singing in the Rain': ['1uNTfm5WZVGdig95SAXajH', '6ZCugHZvchMlF6DqMDYIW1'], 'Love Letter': ['3GAKRdjL6Snq9C7u5tMC01', '3t7m1KLkT2aPvqyzVRnTBy'], 'ODD': ['3GRwM20EPVWjKoVsNsHjrj'], 'LOONATIC - Eng. Ver.': ['7xkpUBffveGC99B2UYIuFy'], 'Star (Voice English Ver.)': ['46Xt2hKFz0R8RiqNPO1ato'], 'MAXIS BY RYAN JHUN Pt. 2-Not Friends': ['7zYMDxOA7hYHzTh2ynIUGl'], 'Not Friends - ALAWN Remix Version': ['7e71lOzdUbODek6nuSB2TI'], 'Not Friends - TIDO Remix Version': ['5RasYGoFBYGimWdYlBeeKv'], 'Not Friends - ORBIT Remix Version': ['4FbeDsHUpm4djW9Pwoef6T'], 'Not Friends - Mix Version': ['460Ql9Wl8z2lMwEhnIlhBx'], 'SHAKE IT': ['1ezubi9SlRqI3fHoGXjuP7'], 'Don`t Go - Queendom2 Version': ['70HOn7S07x4fvvrt8lKRbT'], 'Tell me now': ['2kIYgg1tOBTjs7XLZNwuSs'], 'Hi High - Japanese Ver.': ['3MZFdBPYCFCn1YQLV0s7Vl'], 'I’ll be There': ['2cCj7bIY0jrdGn20lq88ae'], 'Let Me In': ['3Ir6BUnlnAGTMZBMIHlgSu'], 'Kiss Later': ['4TeqecANyRsllKmXNw641W'], 'Everyday I Love You (feat. HaSeul)': ['5e6Tii9571q3uKOC6wn8XU'], 'Everyday I Need You (feat. JinSoul)': ['6y0g4cJTSABiaaKECOISiI'], 'Into the New Heart (Guitar by JungMo)': ['7EG2HkWMW1mM7PIMznLyhW'], 'Eclipse (Prod. By Daniel Obi Klein)': ['6k3sl3Hs6bNN497d672gpR'], 'Twilight (Prod. By Cha Cha Malone)': ['0Eh58SEH7NMUS5r6saQ7W7'], 'Not Friends (ALAWN REMIX)': ['4JMSZR1HhsOyMm8JwXdYPX'], 'Not Friends (TIDO REMIX)': ['2GH8QibZN3lChxaIYjPdSw'], 'Not Friends (ORBIT REMIX)': ['3nSd7w3aOfhAoGxVZuUY7X'], 'Not Friends ORIGINAL MIX': ['0T6MBcbl5Y6stcLWorNQQ2']}
