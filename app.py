import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo

app = Flask(__name__)
# passing mongodb uri via environment 
app.config["MONGO_DBNAME"] = "booksDB"
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
# passing Secret key via environment 
app.secret_key = ('SECRET_KEY')
#creating mongo app
mongo = PyMongo(app)

# landing route - passing both collections to index.html to test
@app.route('/')
def index(): 
    users=mongo.db.users.find()
    reviews=mongo.db.reviews.find()
    return render_template("index.html", users=users, reviews = reviews)



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)