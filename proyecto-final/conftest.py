import pytest

@pytest.fixture
def posts_data():
    return {
        "title": "Mi primer posteo",
        "body": "contenido referente a mi primer posteo",
        "userId": 1
    }


@pytest.fixture
def users_data():
    return{
        "name": "bray farfan",
        "username":"bray",
        "email":"bray@gmail.com"
    }


def pytest_html_report_title(report):
    report.title = "API JSONPLACEHOLDER - POST"