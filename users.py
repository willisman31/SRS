import requests

def get_posts(user):
    reddit_url = "https://reddit.com/user/"
    posts = requests.get(reddit_url + user + "/submitted.json")
    return posts

