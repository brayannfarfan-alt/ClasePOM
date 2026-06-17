import requests

class PostsApi:
    URL_BASE = "https://jsonplaceholder.typicode.com/"


    def get_posts(self):
        return requests.get(
            f"{self.URL_BASE}/posts"
        )

    def get_one_post(self,post_id):
        return requests.get(
            f"{self.URL_BASE}/posts/{post_id}"
        )
    
    def create_posts(self,title, body, user_id):

        data = {
            "title":title,
            "body":body,
            "userId":user_id
        }

        return requests.post(
            f"{self.URL_BASE}/posts",
            json=data
        )

    
    