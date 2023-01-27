import json
from json import JSONDecodeError


def get_posts_all():
    """Возвращает посты"""
    try:
        with open('data/posts.json', 'r') as file:
            posts_data = json.loads(file.read())
        return posts_data
    except FileNotFoundError:
        print("Файл с данными постов не найден")
    except JSONDecodeError:
        print("Ошибка в чтении файла json с данными постов")


def get_comments_all():
    """Возвращает комментарии"""
    try:
        with open('data/comments.json', 'r') as file:
            comments_data = json.loads(file.read())
        return comments_data
    except FileNotFoundError:
        print("Файл с данными комментариев не найден")
    except JSONDecodeError:
        print("Ошибка в чтении файла json с данными комментариев")


def get_posts_by_user(user_name):
    """Возвращает посты определенного пользователя"""
    user_name_posts = []
    posts = get_posts_all()
    for post in posts:
        if user_name.lower() == post['poster_name'].lower():
            user_name_posts.append(post)
    try:
        if not user_name_posts:
            raise ValueError("Нет такого пользователя!")
    except ValueError as e:
        print(e)
    return user_name_posts


def get_comments_by_post_id(post_id):
    """Возвращает коментарии определенного поста"""
    comments = get_comments_all()
    comments_for_post = []
    for comment in comments:
        if post_id == comment['post_id']:
            comments_for_post.append(comment)
    try:
        if not comments_for_post:
            raise ValueError("Нет таких комментариев!")
    except ValueError as e:
        print(e)
    return comments_for_post


def search_for_posts(query):
    """Возвращает список постов по ключевому слову"""
    posts = get_posts_all()
    query_posts_list = []
    for post in posts:
        if query in post['content']:
            query_posts_list.append(post)
    return query_posts_list


def get_post_by_pk(pk):
    """Возвращает один пост по его идентификатору"""
    posts = get_posts_all()
    for post in posts:
        if pk == post['pk']:
            return post


def handle_bad_request(e):
    """Oбработчик запросов к несуществующим страницам"""
    return f'<h1>Page Not Found</h1>', 404


def internal_error(e):
    """Oбработчик ошибок, возникших на стороне сервера"""
    return "500 error", 500
