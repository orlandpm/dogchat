from flask import Flask, render_template
from data import test_posts, post1

app = Flask(__name__)

@app.route("/")
def feed():

    return render_template('feed.html', posts=test_posts, title="My Feed")


@app.route("/comments")
def comments():
    return render_template('comments.html', title="Comments", post=post1)