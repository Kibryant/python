from flask import Flask, render_template, request
from db import psql
from models.models import Post

app = Flask(__name__)


app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://userarthurgus:Tbjh980080@172.27.206.152:5432/python"


app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = psql.db

db.init_app(app)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("home/index.html")


@app.route("/posts")
def posts():
    posts = Post.query.all()
    return render_template("posts/index.html", posts=posts)


@app.route("/posts/create", methods=["GET", "POST"])
def create_post():
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        new_post = Post(title=title, content=content)
        db.session.add(new_post)
        db.session.commit()
        return show_post(new_post.id)
    return render_template("posts/_partials/create-post.html")


@app.route("/post/<string:post_id>")
def show_post(post_id: str):
    post = Post.query.get(post_id)
    return render_template("posts/_partials/show-post.html", post=post)


@app.route("/posts/edit/<string:post_id>", methods=["GET", "PUT"])
def edit_post(post_id):
    if request.method == "PUT":
        title = request.form.get("title")
        content = request.form.get("content")
        Post.query.filter_by(id=post_id).update({"title": title, "content": content})
        return show_post(post_id)
    post = Post.query.get(post_id)
    return render_template("posts/_partials/edit.html", post=post)


@app.route("/post/<string:post_id>/delete", methods=["DELETE"])
def delete_post(post_id):
    if request.method == "DELETE":
        Post.query.filter_by(id=post_id).delete()
        return ""
    return ""


@app.route("/users")
def users():
    return render_template("users/index.html")
