import requests

class User:

    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.get_user_url()

    def get_user_url(self):
        url = "https://www.reddit.com/user/" + self.name
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

# cakeday info is only sent on average for every 3 requests
    def attempt_get_cakeday(self):
        response = requests.get(self.get_user_url())
        page_source = response.text
        cakeday_magic_string = "faceplate-date"
        cakeday_magic_string_index = page_source.find(cakeday_magic_string)
        buffer = page_source[cakeday_magic_string_index:]
        placeholder = buffer.index('ts=')+3
        res = buffer[placeholder:placeholder+12]
        return res
    
    def get_cakeday(self):
        msg = ""
        for i in range(0, 3):
            try:
                msg = self.attempt_get_cakeday()
                return msg
            except:
                msg = "failed to retrieve cakeday"
        return msg
    
    def get_raw_page(self):
        response = requests.get(self.get_user_url())
        return response.text

