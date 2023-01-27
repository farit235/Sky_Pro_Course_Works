from api.api import get_posts_api, get_post_api
import json


def test_get_posts_api():
    """Тестирование эндпоинта get /api/posts"""
    assert type(json.loads(get_posts_api())) == list, "Test Passed"


def test_get_post_api():
    """Тестирование эндпоинта get /api/post/<id>"""
    assert type(json.loads(get_post_api(1))) == dict, "Test Passed"