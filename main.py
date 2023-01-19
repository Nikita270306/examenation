from flask import Flask, render_template, request, jsonify
from utils import *

app = Flask(__name__, template_folder='templates')


@app.route("/")
def main_page():
    posts = get_posts_all()
    return render_template("index.html", posts=posts)


@app.route("/posts/<int:postid>")
def post_page(postid):
    post = get_post_by_pk(postid)
    comments = get_comments_by_post_id(postid)
    return render_template("post.html", post=post, comments=comments)


@app.route("/search/")
def search_page():
    query = request.args.get("query")
    posts = search_for_posts(query)
    return render_template("search.html", posts=posts)


@app.route("/users/<username>")
def user_posts_page(username):
    posts = get_posts_by_user(username)
    return render_template("user-feed.html", posts=posts)


@app.route("/api/posts")
def api_main_page():
    posts = get_posts_all()
    return jsonify(posts)


@app.route("/api/posts/<int:post_id>")
def api_post_page(post_id):
    post = get_post_by_pk(post_id)
    print(post)
    return jsonify(post)

@app.errorhandler(404)
def page_error_404(e):
    return '<h1>Error</h1><p>not found(((</p>', 404


@app.errorhandler(500)
def page_error_500(e):
    return '<h1>Error</h1><p>not found(((</p>', 500



app.run()
