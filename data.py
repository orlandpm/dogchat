from datetime import datetime

comment1 = {
    "Text" : "What time are you going?",
    "Name": "Charlie",
    "Username" : "chucky",
    "Picture" : "charlie_profile.png",
    "DateTime" : datetime(2021, 7, 1, 18, 0, 0),
}

comment2 = {
    "Text" : "I'm going to go at 7 tonight!",
    "Name": "Melba",
    "Username" : "melba",
    "Picture" : "melba_profile.png",
    "DateTime" : datetime(2021, 7, 1, 18, 30, 0),
}


post1 = {
    "Text": "I can't wait to go to the park today",
    "Name": "Melba",
    "Username" : "melba",
    "Likes": ["charlie"],
    "Comments" : [comment1, comment2],
    "DateTime" : datetime(2021, 7, 1, 17, 0, 0),
    "Picture" : "melba_profile.png"
}

post2 = {
    "Text": "I could really use a treat right now",
    "Name": "Melba",
    "Username" : "melba",
    "Likes": [],
    "Comments" : [],
    "DateTime" : datetime(2021, 6, 30, 12, 30, 0),
    "Picture" : "melba_profile.png"
}

post3 = {
    "Text": "Arent' naps the best?",
    "Name": "Charlie",
    "Username" : "chucky",
    "Likes": ["melba"],
    "Comments" : [],
    "DateTime" : datetime(2021, 6, 29, 9, 0, 0),
    "Picture" : "charlie_profile.png"
}

test_posts = [post1, post2, post3]