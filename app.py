import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from forms import RegistrationForm

app = Flask(__name__)
# passing mongodb uri via environment 
app.config["MONGO_DBNAME"] = "booksDB"
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
# passing Secret key via environment 
app.secret_key = ('SECRET_KEY')
# creating mongo app
mongo = PyMongo(app)

# landing page route
@app.route('/')
def index():
    ''' function to display all records on the landing page''' 
    # sort reviews by popularity (upvote)
    reviews=mongo.db.reviews.find().sort('upvote', pymongo.DESCENDING)
    return render_template("index.html", reviews = reviews)

@app.route('/review/<id>', methods=['GET', 'POST'])
def review(id):
    ''' function to return a single record of the review db
     on the basis of the id of the item in the collection,
     runs when 'view reeview' is clicked '''
    one_review = mongo.db.reviews.find_one({"_id": ObjectId(id)})
    title = one_review['book_title']
    return render_template("review.html",  review = one_review, title =title)

@app.route('/upvote/<id>', methods=['GET', 'POST'])
def upvote(id):
    '''function to increase upvote by 1, runs when upvote icon is clicked'''
    mongo.db.reviews.find_one_and_update({'_id': ObjectId(id)},{'$inc': {'upvote': 1}})
    return redirect(url_for('review', id=id))# run review route to reload review.html

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        
        users = mongo.db.users
        find_user = users.find_one({'username': request.form['username']})
        if find_user is None:
            password = request.form['password']
            users.insert_one({'name': request.form['username'],
                             'password': password})
            flash(f'You have registered as  {form.username.data}' , 'success')
            return redirect(url_for('index'))

    return render_template('register.html', title='Register', form =form)
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)