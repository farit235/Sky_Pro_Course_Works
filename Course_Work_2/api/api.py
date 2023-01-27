import json
import logging
from flask import Blueprint
from Course_Work_2.utils import get_posts_all, get_post_by_pk

logging.basicConfig(filename='api.log', encoding='utf-8', level=logging.INFO,
                    format="%(asctime)s [%(levelname)s]Запрос %(message)s", datefmt="%Y-%m-%d %H:%M:%S")


api_blueprint = Blueprint("api_blueprint", __name__, template_folder='templates')


@api_blueprint.route("/posts")
def get_posts_api():
    logging.info("Получение всего списка постов из json")
    posts = json.dumps(get_posts_all(), ensure_ascii=False)
    try:
        if type(posts) != list:
            raise ValueError("Не получен список постов")
    except ValueError as e:
        print(e)
    return posts


@api_blueprint.route("/posts/<int:post_id>")
def get_post_api(post_id):
    logging.info("Получение поста в виде словаря json")
    post = json.dumps(get_post_by_pk(post_id), ensure_ascii=False)
    try:
        if type(post) != dict:
            raise ValueError("Не получен словарь поста")
    except ValueError as e:
        print(e)
    return post
