import utils


def test_get_posts_all():
    """Test полечения данных из списка постов"""
    assert isinstance(utils.get_posts_all(), list), "Проблема с загрузкой данных из json"
    assert len(utils.get_posts_all()) >= 1, "Пустой список, данные не получены из json"
    assert len(utils.get_posts_all()[0]) >= 1, "Пустой словарь, данные не получены из json"


def test_get_comments_all():
    """Test полечения данных из списка комментариев"""
    assert isinstance(utils.get_posts_all(), list), "Проблема с загрузкой данных из json"
    assert len(utils.get_posts_all()) >= 1, "Пустой список, данные не получены из json"
    assert len(utils.get_posts_all()[0]) >= 1, "Пустой словарь, данные не получены из json"


def test_get_post_by_user():
    """Test поиска по пользователям"""
    assert len(utils.get_posts_by_user('a')) == 0, "Ошибка в получении данных о пользователе"


def test_get_comments_by_post_id():
    """Test поиска комментария по id"""
    assert len(utils.get_comments_by_post_id(0)) == 0, "Ошибка в получении данных о посте по id"
    assert len(utils.get_comments_by_post_id(1)) > 1, "Ошибка в получении данных о посте по id"


def test_search_for_posts():
    """Test поиска текста поста по слову-запросу"""
    assert len(utils.search_for_posts("Вышел")) == 1, "Ошибка в получении данных о посте по id"
    assert len(utils.search_for_posts("")) >= 1, "Ошибка в получении данных о посте по id"


def test_get_post_by_pk():
    """Test поиска текста поста по id"""
    pk = 2
    assert type(utils.get_post_by_pk(pk)) == dict, "Ошибка в получении данных о посте по id"
    # assert utils.get_post_by_pk(0) == None, "Ошибка в получении данных о посте по id"
