import requests

class User:

    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.get_user_url()

    def get_user_url(self):
        url = "https://reddit.com/user/" + self.name
        return url

    def is_error(self):
        response = requests.get(self.get_user_url())
        success_codes = [200, 201, 202]
        return response.status_code not in success_codes

    # returns first 25 submitted posts for user; not formatted in any way
    def get_posts(self):
        user_url = self.get_user_url() + "/submitted.json"
        if self.is_error():
            return False
        posts = requests.get(user_url)
        return posts.text

    def get_raw_page(self):
        response = requests.get(self.get_user_url())
        return response.text

