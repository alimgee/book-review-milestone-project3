import os
from flask import Flask, render_template, redirect, request, url_for, session, flash, Markup
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from forms import RegistrationForm, LoginForm

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
    '''
    Function to allow a new user to register a new account on the db
    CHecks if user is already logged in and checks that the user doesnt
    current exist in db
    '''
    form = RegistrationForm()
    if 'logged' in session: # if a session currently exists notify user
        # don't let logged in user register and send to index
        flash(f'You are already logged in on this device as  ' + session['username']  , 'warning')
        return redirect(url_for('index')) 
    if form.validate_on_submit():
        # if reigster form passes all validation check if username currently exists
        users = mongo.db.users
        find_user = users.find_one({'username': request.form['username']})
        if find_user is None: # if username is not in db insert the record into users collection
            password = request.form['password']
            users.insert_one({'username': request.form['username'],
                             'password': password})
            # Notify new user succesfully registration and create a logged in session
            flash(f'You have registered and are logged in as  { form.username.data }' , 'success')
            session['username'] = request.form['username']
            session['logged'] = True
            # Send user to index
            return redirect(url_for('index'))
        else:
            # if username already exists in db, notify user and reload register template
            flash(f'The username { form.username.data } already exists. Please try a different username' , 'warning')
            return redirect(url_for('register'))
    # load registration form
    return render_template('register.html', title='Register', form =form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if 'logged' in session: # if a session currently exists notify user
        # don't let logged in user register and send to index
        flash(f'You are already logged in on this device as  ' + session['username']  , 'warning')
        return redirect(url_for('index'))
    if form.validate_on_submit():
        # if reigster form passes all validation check if username currently exists
        users = mongo.db.users
        find_user = users.find_one({'username': request.form['username']})
        if find_user:
            password = form.password.data
            if find_user['password'] == password:
                flash(f'You  are logged in as  { form.username.data }'  , 'success')

                return redirect(url_for('index'))
            else:
                flash(f'Your password is incorrect. Please log in again with correct details'  , 'warning')
                session['username'] = request.form['username']
                session['logged'] = True
                return redirect(url_for('login'))

        else:
            register_link = Markup('<a href="/register">Register</a>')
            flash(f'User "{ form.username.data } " does not exist, please ' + register_link +  
            ' if you do not already have a valid username', 'warning')
            return redirect(url_for('login'))

    return render_template('login.html', title='Login', form =form)

@app.route("/sign-out")
def sign_out():
    '''
    function to allow a user to sign out of the current session
    '''
    session.clear() # Clear session, notify user and redirect to index
    flash(f'You are now signed out' , 'success')
    return redirect(url_for("index"))

    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)