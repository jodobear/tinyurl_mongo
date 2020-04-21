from flask import Flask, request, render_template, redirect
from flask_pymongo import PyMongo

import hashlib
from math import floor


app = Flask(__name__)
host = 'http://localhost:5000/'
mongo = PyMongo(app, uri="mongodb://mongodb:27017/urldb")

def get_hash(url):
    return hashlib.md5(str(url).encode()).hexdigest()[:6]

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template("home.html")
    elif request.method == 'POST':
        url_submit = request.form['url-submit']
        tiny_url = get_hash(url_submit)
        new_entry = {"url_submit": url_submit, "tiny_url": tiny_url}
        mongo.db.urldb.insert(new_entry)
        result = host + tiny_url
        return render_template("home.html", result=result)

@app.route('/<tiny_url>', methods=['GET'])
def rerirect_page(tiny_url):
    entry = mongo.db.urldb.find_one_or_404({"tiny_url": tiny_url})
    return redirect(entry["url_submit"])


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
