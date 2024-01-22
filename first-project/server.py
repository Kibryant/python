from flask import Flask, render_template
from db import sample_db

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home/index.html")


@app.route("/posts")
def posts():
    posts = sample_db.get_posts()
    return render_template("posts/index.html", posts=posts)


@app.route("/posts/edit/<string:post_id>", methods=["GET", "PUT"])
def edit_post(post_id):
    post = sample_db.get_post(post_id)
    return render_template("posts/_partials/edit.html", post=post)


@app.route("/users")
def users():
    return render_template("users/index.html")
