from auth import spotify_client as sp
"""
confusing because spotify sucks but...
show == playlist
episode == track

items: array of episodes
"""

def get_episodes(show_id: str):
    # show name : id
    episodes = {}

    results = sp.show_episodes(show_id=show_id)
    items = results["items"]

    while results["next"]:
        results = sp.next(results)
        items.extend(results["items"])
    
    for episode in items:
        episode_name_filter = {"Keeping these from getting deleted",
                               "Putting this so won't taken down",
                               "i̶t̶t̶o̶ ̶f̶v̶c̶k̶ ̶m̶e̶ ̶p̶l̶s̶"}

        episode_name = episode["name"]
        episode_id = episode["id"]
        if episode_name not in episode_name_filter:
            episodes[episode_name] = episode_id
    
    return episodes

"""
HARDCODED DICTIONARY OF ALL SONGS
dictionary = {song name: id, ...}
"""
loona_episodes_dict = {'# Burn (Teaser Ver.)': '159DQdLVvySG6yepIBC4hd', 'Star (Teaser Ver.)': '0VIm2nDGgsMDmtVG6dMsz4', 'Flower Way (하슬)': '4iLyDCpoGDD97V4YROdVBk', 'If We Have Four Seasons (최리)': '2ze00O3hirYKph1GVDo04H', 'SIDE (진솔)': '3l0M423gX2gjvy4ui4hPFk', 'A Journey (이브)': '3NuJl5mLYgaEFNpiSZD650', 'Every Moment of You (김립)': '3xmCVDi24iyPpzRFsc6bcj', 'In Winter (혜주)': '3yYACJIQ22Stq8OQkoYf3S', 'Paper Hearts (츄)': '2F7VUUP5TZ0mGy1hWzogGr', 'Christmas Carol Medley (하슬)': '6j8fXkvPuD5OfmZmzU2a1r', 'November Song (희진)': '5FCDn4LzgMtNr4fqagWnMu', 'i̶t̶t̶o̶ ̶f̶v̶c̶k̶ ̶m̶e̶ ̶p̶l̶s̶ ': '4aGL4f85HYLJAr6fuY4nSp', 'Vamos a la Playa - sped up': '4SNl71QsjaWIjKFKUIHs3e', 'Love Battery': '56UKOt9FTIP9i4CgE7Z7Iu', 'POSE': '2v50aI3ubYls09YGwPNnHv', 'Butterfly': '5jex5ILdfW69fWisMxtOSj', 'Tell me now': '10U0s0iYoeV142RGxOt3A6', 'SHAKE IT': '66wsFg5naGCAkDZI41qPWH', 'PTT (Paint The Town)': '4u913jmfEgIZE5uYgmlp4V', 'Hi High - Japanese Ver.': '6Me0v2G5ejWexjlCvmfV4P', 'LUMINOUS': '2EClJarnD3LTgjUeOfi75i', 'SICK LOVE': '6ZyiG6qkiqSN5rGGjvyeYP', 'Playback': '0FaUX9TwlHxwp2GfYyKuE1', 'Pale Blue Dot': '3kqRQPMq99tBgWVDwjZ6ER', 'Need U': '18es6HdFFMnYaBROl4FUwl', 'Flip That': '1SN0TwJrw4oq6HEiu3agdl', 'The Journey': '5aoRb112xKkZtsuVDx5lv3', "Don`t Go - Queendom2 Version": '3sdueN4fY4jbIiI0TELJ0U', 'Not Friends INSTRUMENTAL': '5UEwDyzsEEsz4E1mkikbxq', 'Not Friends ORIGINAL MIX': '5ytiotyQkY4z3Ze6Yjs0Yp', 'Not Friends (ORBIT REMIX)': '7qTvpcvBLsxMenTfhpSGO3', 'Not Friends (TIDO REMIX)': '0oOCyiwkVPrt3ofC90kH6L', 'Not Friends (ALAWN REMIX)': '2KHfM57l1yi8saaHXVBz9T', 'HULA HOOP - City Pop Ver.': '52PdIKurRjljWtTVlEgJaN', 'PTT（Paint The Town） - Japanese Ver.': '0162maheQa1lRFI8wQLk07', 'StarSeed 〜カクセイ〜': '7LSM0EaCjL26Vn9FWcgzET', 'HULA HOOP': '5lDvAIZBzuGh1Y8DF5gF1H', 'Not Friends': '4EQJCLtkb0pCv63oMamnns', 'U R': '7oyO5ahCxK14Yin2FaSqgv', 'A Different Night': '2Ir4SLxNLVJQks4kX71JjM', 'Dance On My Own': '0c4nTzudqtv8ZrO7KjQRdX', 'Be Honest': '3uEhAUSQpG8SaUxADuAtMA', 'WOW': '4RHoejhwsRC1WJoVSC2LcM', '&': '42Xgkd5PndEFB7qg8Dv83L', 'Star (Voice English Ver.)': '1m2By1cKGoj83X7pyjj6T0', 'OOPS!': '6X3Z4AkYduSCnP7aV4kHcd', 'Hide & Seek': '7IEe25uQYHzvhOq7qKlVmX', 'Universe': '2L8t0NDfkU3NHmt7uZa5gq', 'Fall Again': '40e96CrIxLnpEA2a8PH33P', 'Voice': '788MJzt52Wth06b6PZDDID', 'Why Not?': '2QkWYFKacoGDuXGee0vtOA', '12:00': '36Vnnids4GrpM54f9sXPt3', 'Day & Night': '6sA6hvrRjFQJBFrVgduD3u', '365': '7AJGTf44ZVLfGWcFOTysTv', 'Ding Ding Dong': '1222hygZ3T3Ud0Os7zL7kv', 'Oh (Yes I Am)': '23AevVEnys2BPe3LfdBK6l', 'Number 1': '2Oh6ugSvykMLssuNGuZ1Gr', 'So What': '3PDYsmZGadeaINcc830o3V', '#': '4b5jSzjyqwVVTFXXcKAME9', 'Bliss Ballad': '4EO1r4JZrU4stgcccqMOOk', 'Crystal Ballad': '5BtHu9Fp15pPDe3nnYltIE', 'Hyper Ballad': '7AAhmxKorZqiqGgxHwGmO4', 'Hyper Ballad instrumental': '52eEDzC3MNmmsedjEil80f', 'Where you at': '20Vvk4yNbt0WSmUvtieo1r', 'Colors': '0xe0Ba81Sbdq6t1YhGyAXt', 'Curiosity': '40JOP0UQKmTUCG9HpJ1JEy', 'Satellite': '7F47DlQ9jT0Kx295FXTulP', 'X X': '1haWUeiyPrODf4vBtwgoN8', 'Stylish': '1yPkbyOemvUrFCLtfNFzEr', 'Perfect Love': '0TI97UhNkQ9jLBYimi8ktc', '열기': '12IjgJe8E4Bra1fbPP0fTQ', 'favOriTe': '5NeUqwD7h3IlsM7gFrGdrP', 'Hi High': '3W2dRYlX7bUUSBrkgD46Og', '+ +': '3SGg5vuQ3P30EVxBB2Rx1f', 'Hi High (Remix Ver.)': '2HkM5HlIw8erIefQ6qROFZ', 'Egoist (Eng Rap Ver.)': '6wosnwggRKeIrUds7Y3JJD', '지금 더 좋아해': '08de5YzbCGgGS2SqyEBxtB', 'love4eva (Dance Break 4 ver.)': '7ENZquHuDIdhtxj1sucQC1', 'love4eva (Dance Break 3 ver.)': '7s6rd21vn8zoRgX8WbOsnV', 'love4eva (Dance Break 2 ver.)': '1c7mXxatPc24sVi62ffRds', 'rendezvous 18.6y': '1E3UXNwwWbx1LfFlovUitn', 'one way': '2ZewbrxDkSbPniF9AHZ7y4', 'frozen': '7KsGFqeFuBaZOItQqwOSkl', 'love4eva (feat. Grimes)': '6Zina7PpxHlIGDSJ6tjMHR', 'dal segno': '6xSWX73qG9ADhICCkYFtUK', 'Rosy (고원, Olivia Hye)': '7xHW399MdZYoMEmhbmbRuQ', 'Egoist (Olivia Hye)': '099A9igrNZZ3EFT5JQUyaF', 'See Saw (Chuu, Go Won)': '7rdabOycts0WqX6ofSA2Ks', 'One & Only (Go Won)': '4SgQMfewsUw7pKASxEmQlB', "Girl's Talk (이브, 츄)": '2Q6ikfnbzylzN1Dkx1pUWB', 'Heart Attack (츄)': '0UahcHWBUDtRzNI1SSw9Wh', 'The Carol 2.0 (ViVi, Choerry, Yves)': '5ECPP6eIlKNPABcEnOdTzs', 'D-1': '2Id42MkT8JuBIb73kF4LXc', 'new': '4zsUaXOHANL071jXOB4axJ', 'LOONATIC - Eng. Ver.': '3eqwztMFLJJxwoE4eI7mKw', 'ODD Front': '7HbjvSOjTQQuQiDwYdaA56', 'Uncover': '3dl1QJmGIfxnDECq48Bgn8', 'Sweet Crazy Love': '11D7HbCqRe11gUDJQE37Zk', 'ADD': '077YgnMIsCFtX9c0PJ7Bj9', 'Starlight': '4vHtojDlg4zm2ptJ0rayvu', 'Chaotic': '3J2a44Lvqkg1NnPjVLLjXc', 'LOONATIC': '1rZ8e4KBDdggnejWnEslq5', 'Girl Front': '5OS4DwfVeuZZZNXerK8ede', 'ODD': '5vjrNAWk2aznF3CUL5aovu', 'Puzzle': '3ty9IhHqHIawk2UUCCtGX6', 'Love Cherry Motion': '6TzCaCoeIW3ZOAmAnXyHJq', 'Love Letter': '0uPn01Vp9dqCGOJxDo1YMp', 'Singing in the Rain': '5xyulaPTcCMwi3deYvKAcG', 'Twilight': '0a0uS111flsS1q1ALkz0Ym', 'Eclipse': '2zy1tSJOo4idRk2QN882DI', 'You and Me Together (Remix)': '1HsDnDkndNN4X1FRJ3SqeS', 'Rain 51db': '3NVzKscWjkwTqHxxSCYlfB', 'Sonatine': '2poOg3stMhO4sELEKKuOcp', 'Love & Evil': '3cna63iQw5pp23UMKgMAGK', 'Everyday I Need You': '1MI3utrKim4Q5ScMpjpvQ3', 'Everyday I Love You': '7Hu3jlC5Bd8xCZ6fXlYNWX', 'Valentine Girl': '7DycHU4jl8y1LzecAtiE7h', 'Fairy Tale': '391VXmLU7waMSKbSShdhQj', 'You and Me Together': '3n76KvdsvUHzelo1VzbMIk', 'Love & Live': '0HztkV26TsAmj2HXXBUh3d', 'Into the New Heart': '118iIiJBACweHHWkslEmFx', 'My Melody': '4S6Dfaj7V3MbYCcyB5fau8', 'My Sunday': '6RhXmQfwK0d6Xbxrz93vdI', '키스는 다음에': '6c8cflGlHHBPcoUqPsl3En', '소년, 소녀': '2mcYp8zpZWs2Tz25Ut6OOa', 'The Carol': '1YCVjHlbDxi7f1i2rTdQlY', '다녀가요': '0uQA0KTSFl2RxatA8rBA8S', "I'll Be There": '2qgn0A7Qc0Q2zOgSkrk6Dd', 'ViViD - Acoustic Mix Version': '5dYxP6oer0vdeobZZywT0f', 'ViViD': '3WarTuPR4uHwOX8GSXEn0M'}
        
