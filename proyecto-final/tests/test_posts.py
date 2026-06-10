import pytest

from pages.post_api_page import PostsApi
from utils.logger import get_logger

api = PostsApi()
logger = get_logger()

def test_get_one_posts():
    logger.info("SE INICIO EL LLAMADO A UN POSTS a LA url : ")
    logger.info(f"")
    posts_id = 2

    res = api.get_post(posts_id)
