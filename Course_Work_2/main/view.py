from flask import Blueprint, render_template, request
from Course_Work_2.utils import get_posts_all, get_comments_by_post_id, search_for_posts, get_posts_by_user


main_blueprint = Blueprint("main_blueprint", __name__, template_folder='templates')


@main_blueprint.route("/")
def main_page():
    posts = get_posts_all()
    return render_template("index.html", posts=posts)


@main_blueprint.route("/post/<int:postid>")
def page_post(postid):
    comments = get_comments_by_post_id(postid)
    posts = get_posts_all()
    post_info = ""
    for post in posts:
        if post['pk'] == postid:
            post_info = post
            if post_info != "":
                break
    return render_template("post.html", comments=comments, post=post_info, length=len(comments))


@main_blueprint.route("/search")
def page_search():
    search_term = request.values.get("q")
    search_list = search_for_posts(search_term)
    search_len = len(search_list)
    if search_len > 10:
        search_list = search_list[:10]
    return render_template("search.html", search_list=search_list, search_len=search_len)


@main_blueprint.route("/users/<username>")
def page_user(username):
    posts_user = get_posts_by_user(username)
    return render_template("user-feed.html", posts=posts_user)

