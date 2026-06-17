from pages.posts_api_page import PostsApi
from utils.logger import logger
import pytest_check as check

api = PostsApi()

def test_get_one_posts():
    logger.info("Obteniendo un posts")

    response = api.get_one_post(1)

    check.equal(
        response.status_code, #201
        200,
        "STATUS INCORRECTO"
    )

    body = response.json()
    check.equal(
        body["id"], #me da el valor del ID
        1,
        "EL ID NO COINCIDE"
    )

    
def test_posts():
    logger.info("Obteniendo TODOS posts")
    response = api.get_posts()

    check.equal(
        response.status_code, #201
        204,
        "STATUS INCORRECTO"
    )

    posts = response.json()

    check.is_true(
        len(posts) > 0 , # BOOLEAN
        "No se obtuvieron posts"
    )

    check.is_true(
        isinstance(posts,list),
        "LA RESPUESTA NO ES UNA LISTA"
    )

def test_create_post(posts_data):

    logger.info("CREANDO POSTS")
    response = api.create_posts(
        posts_data["title"],
        posts_data["body"],
        posts_data["userId"]
    )

    check.equal(
        response.status_code,
        201,
        "NO SE CREÓ EL POST"
    )
