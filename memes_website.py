from flask import Flask, render_template
import json
import requests

app = Flask(__name__)

def get_memes():
# Uncomment these two lines and comment out the other url line if you want to use a specific meme from subreddit.
#   sr = '/wholesomememes'
#   url = "https://meme-api.herokuapp.com/gimme" + sr
    url = "https://meme-api.herokuapp.com/gimme"
    response = json.loads(requests.request("GET", url).text)
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    return meme_large, subreddit

@app.route('/')
def index():
    meme_pic, subreddit = get_memes()
    return render_template("index.html", meme_pic = meme_pic, subreddit = subreddit)

app.run(debug = True, host = "0.0.0.0", port = 80)

