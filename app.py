from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def feed():

    post1 = {
        "Text": "I can't wait to go to the park today",
        "Name": "Melba",
        "Username" : "melba",
        "LikeCount": 10,
        "CommentCount" : 4,
        "DateTime" : datetime(2021, 7, 1, 17, 0, 0),
        "Picture" : "melba_profile.png"
    }

    post2 = {
        "Text": "I could really use a treat right now",
        "Name": "Melba",
        "Username" : "melba",
        "LikeCount": 5,
        "CommentCount" : 1,
        "DateTime" : datetime(2021, 6, 30, 12, 30, 0),
        "Picture" : "melba_profile.png"
    }

    post3 = {
        "Text": "Arent' naps the best?",
        "Name": "Charlie",
        "Username" : "chucky",
        "LikeCount": 3,
        "CommentCount" : 0,
        "DateTime" : datetime(2021, 6, 29, 9, 0, 0),
        "Picture" : "charlie_profile.png"
    }


    test_posts = [post1, post2, post3]

    return render_template('feed.html', posts=test_posts, title="My Feed")


@app.route("/comments")
def comments():
    return render_template('comments.html', title="Comments")