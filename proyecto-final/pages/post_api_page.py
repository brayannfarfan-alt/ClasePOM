import requests

class PostsApi:
    URL_BASE = "https://jsonplaceholder.typicode.com/"

    def get_post(self,post_id):
        return requests.get(
            f"{self.URL_BASE}/users/{post_id}"
        )
    