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
        
