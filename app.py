import os
import re
from flask import Flask, render_template, redirect, request, url_for, session, flash, Markup
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from forms import RegistrationForm, LoginForm, ReviewForm

app = Flask(__name__)
# passing mongodb uri via environment 
app.config["MONGO_DBNAME"] = "booksDB"
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
# passing Secret key via environment 
app.secret_key = ('SECRET_KEY')
# creating mongo app
mongo = PyMongo(app)

# landing page route
@app.route('/' , methods=['GET', 'POST'])
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
            flash(f'The username { form.username.data } already exists. Please try a different username' ,
             'warning')
            return redirect(url_for('register'))
    # load registration form
    return render_template('register.html', title='Register', form =form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    '''
    Function to allow a user to log into site with valid details. Session created on sucessful
    log in and user notified. User also informed of unsucessful login.
    '''
    form = LoginForm()
    if 'logged' in session: # if a session currently exists notify user
        # don't let logged in user log in again and send to index
        flash(f'You are already logged in on this device as  ' + session['username']  , 'warning')
        return redirect(url_for('index'))

    if form.validate_on_submit():
        # if log in form passes all validation check if username currently exists
        users = mongo.db.users
        find_user = users.find_one({'username': request.form['username']})
        if find_user: # if user is found in db
            password = form.password.data 
            if find_user['password'] == password:# if password entered matches whats in db for paticluar user
                myreviews_link = Markup(' Go to <a href="/myreviews">My Reviews</a> to view your reviews')
                flash(f'You  are logged in as  { form.username.data }' + myreviews_link  , 'success')
                session['username'] = request.form['username'] #create session
                session['logged'] = True
                return redirect(url_for('index'))
            else: # if passwords dont match
                flash(f'Your password is incorrect. Please log in again with correct details'  , 'warning')

                return redirect(url_for('login'))

        else: # if user not found in db
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

@app.route("/myreviews")
def my_reviews():
    '''
    Function to display a 'my reviews' page which displays only the reivews of the
    logged in user
    '''
    if 'logged' in session: # only let a logged in user edit thier own review page
        flash(f'This is your reviews page. View, edit and add your own reviews from here', 'success')
        current_user = session['username'] # setting db username to the current session username
        # return all content from db uploaded by the username in the session
        return render_template("myreviews.html",  reviews=mongo.db.reviews.find({'username': current_user}),
                                 title='My Reviews')
    else: # if user is not logged in
        flash(f'You need to be logged in to see your reviews' , 'warning')
        return redirect(url_for("login"))

@app.route("/addreview", methods=['GET', 'POST'])
def add_review():
    '''
    Function to display a page which displays a form to add a review for logged in user
    '''
    if 'logged' not in session: # if a user trys to go to add review without been logged in
        flash(f'You need to log in to add a review' , 'warning')
        return redirect(url_for("login")) # sending to log in

    form = ReviewForm()
    if form.validate_on_submit(): # if form submits successfully
        reviews = mongo.db.reviews

        amazon_link = create_amazon_search(request.form['book_title']) # creating amazon link
        icon = get_icon_class(request.form['category']) # creating icon font awesome class
        
        # add form content to db as a new record
        reviews.insert_one({'author': request.form['author'],
                            'book_title': request.form['book_title'],
                            'summary': request.form['summary'],
                            'review': request.form['review'],
                            'category': request.form['category'],
                            'amazon': amazon_link,
                            'icon' : icon,
                            'upvote' : 0,
                            'username' :  session['username']
                                 })
        flash(f'Review added ' , 'success') #send to my reviews template on successful add
        return redirect(url_for('my_reviews'))
   
    return render_template("addreview.html", form = form, title = 'Add Review')

@app.route("/editreview/<id>", methods=['GET', 'POST'])
def edit_review(id):
    '''
    Function to display a page which displays a form to edit a review for logged in user
    '''    
    if 'logged' not in session: # if a user trys to go to edit review without been logged in
        flash(f'You need to log in to edit a review' , 'warning')
        return redirect(url_for("login")) # sending to log in

    one_review = mongo.db.reviews.find_one({"_id": ObjectId(id)}) # retrieving record from db
   
    
    # if a user trys to go to edit review without been logged that they don't own
    if one_review['username'] !=  session['username']:
        flash(f'You do  not own this review and cannot edit it. ' , 'warning')
        return redirect(url_for("login")) # sending to log in

    form = ReviewForm(data =  one_review)
    

    if form.validate_on_submit(): # if form submits successfully
        reviews = mongo.db.reviews
        

        amazon_link = create_amazon_search(request.form['book_title']) # creating amazon link
        icon = get_icon_class(request.form['category']) # creating icon font awesome class
        
        # add form content to db as a new record
        
        reviews.update_one({'_id': ObjectId(id), } , { '$set' : {
                            'author': request.form['author'],
                            'book_title': request.form['book_title'],
                            'summary': request.form['summary'],
                            'review': request.form['review'],
                            'category': request.form['category'],
                            'amazon': amazon_link,
                            'icon' : icon,
                            }
                            })
        flash(f'Review Updated ' , 'success') #send to my review template on successful addupdate
        return redirect(url_for('review', id = id))

     
    return render_template("editreview.html", form = form, title = 'Edit a  Review')



@app.route("/search", methods=['GET', 'POST'])
def search():
    '''
    Function to allow a full text search of the db. Created an index on mongo db in atlas
    to allow a full text search of all string fields using ( { "$**": "text" } ) as the 
    index settings
    '''
    # passing contents of search field to search variable
    search = request.args['search']
    category = request.args['category']
    #count_doc = mongo.db.reviews.count_documents({'category' : category})

    if search != "" and category != "none": # checking for both search and filter been attempted at the same time
        flash(f'Search cannot check site search and filter category at the same time' , 'warning')
        return redirect(url_for("index"))

    if search == "" and category == "none": # checking if user has not entered text into search or used filter
        flash(f'You have not selected a category or enterd text into the search field' , 'warning')
        return redirect(url_for("index"))

    if search == "" and category != "none": # checking for just filter selection
        flash(f'Results showing ' +category +' reviews only ', 'success')
        # searching db for the select category in filter scount_docearch
        find_reviews = mongo.db.reviews.find({'category' : {'$regex' : category }})
        count_doc = find_reviews.count()

        if count_doc == 0 :

            flash(f'There are no reviews currently in the ' + category + ' category', 'warning')
            return redirect(url_for("index"))
            
        return render_template("index.html", title = 'Search', reviews = find_reviews)
        
        
    # running find on contents of search box using the multifield text search
    find_reviews = mongo.db.reviews.find({"$text": {"$search": search}})
    
    flash(f'Search results for ' + ' ' + search  , 'success')
    return render_template("index.html", title = 'Search', reviews = find_reviews)


def create_amazon_search(book):
    '''
    function to build an amazon search link based on the book title entered by the user
    '''
    amazonlink = "https://www.amazon.com/s?i=stripbooks-intl-ship&k="
    while ' ' in book: # replace spaces with +
        book = book.replace(' ', '+')
    amazonlink += book

    return amazonlink # returning newly built link

def get_icon_class(cat):
    '''
    function to check the review category assign by the user and to return
    the relevant font awesome icon classes based on the category sent in
    '''
    # dict of categorys -  modify this and the AddReviewForm class in forms.py to add new categorys
    icons = { 
        'factual' : 'fa fa-picture-o',
        'fiction' : 'fa fa-picture-o',
        'health' : 'fa fa-heartbeat',
        'nature' : 'fa fa-leaf',
        'science' : 'fa fa-cogs',
        'sport' : 'fa fa-futbo-o',
        'world history' : 'fa fa-globe',
        } 
    return icons[cat] # returning relevant classes
   

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)