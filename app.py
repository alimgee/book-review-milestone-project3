import os
import re
import math
from flask import Flask, render_template, redirect, request, url_for, \
    session, flash, Markup
from flask_pymongo import pymongo, PyMongo
from bson.objectid import ObjectId
from forms import RegistrationForm, LoginForm, ReviewForm


app = Flask(__name__)
# passing mongodb uri via environment
app.config['MONGO_DBNAME'] = 'booksDB'
app.config['MONGO_URI'] = os.getenv('MONGO_URI')

# passing Secret key via environment
app.secret_key = 'SECRET_KEY'

# creating mongo app
mongo = PyMongo(app)

page_limit = 2
# for pagination - amount of records to be displayed per page


@app.route('/', methods=['GET', 'POST'])
def index():
    ''' function to display all records on the landing page'''

    # pagination section
    total = mongo.db.reviews.count_documents({})
    # total records in reviews db

    # setting the current page of pagination
    current_page = int(request.args.get('current_page', 1))
    offset = int(request.args.get('offset', 0))
    # setting offset initially to 0 (position in db for current page)
    max_pages = int(math.ceil(total / page_limit))
    # calculating max pages needed to display all records
    page_range = (1, max_pages)
    # creating a tuple with the page range in it

    # sort reviews by popularity (upvote)
    reviews = \
        mongo.db.reviews.find().sort('upvote', pymongo.DESCENDING)\
        .limit(page_limit).skip(offset)
    return render_template(
        'index.html',
        reviews=reviews,
        total=total,
        page_limit=page_limit,
        current_page=current_page,
        offset=offset,
        max_pages=max_pages,
        page_range=page_range,
        )


@app.route('/review/<id>', methods=['GET', 'POST'])
def review(id):
    ''' function to return a single record of the review db
     on the basis of the id of the item in the collection,
     runs when 'view reeview' is clicked '''

    one_review = mongo.db.reviews.find_one({'_id': ObjectId(id)})
    title = one_review['book_title']
    return render_template('review.html', review=one_review,
                           title=title)


@app.route('/upvote/<id>', methods=['GET', 'POST'])
def upvote(id):
    '''function to increase upvote by 1, runs when upvote icon is clicked'''

    mongo.db.reviews.find_one_and_update({'_id': ObjectId(id)},
                                         {'$inc': {'upvote': 1}})
    return redirect(url_for('review', id=id))


@app.route('/register', methods=['GET', 'POST'])
def register():
    '''
    Function to allow a new user to register a new account on the db
    CHecks if user is already logged in and checks that the user doesnt
    current exist in db
    '''
    form = RegistrationForm()
    if 'logged' in session:
        # if a session currently exists notify user
        # don't let logged in user register and send to index
        flash('You are already logged in on this device as  ' +
              session['username'], 'warning')
        return redirect(url_for('index'))
    if form.validate_on_submit():
        # if reigster form passes all validation check if username  exists
        users = mongo.db.users
        find_user = users.find_one({'username': request.form['username']})
        if find_user is None:
            # if username is not in db insert the record into users collection
            password = request.form['password']
            users.insert_one({'username': request.form['username'],
                             'password': password})
            # Notify new user succesfully registration and create a  session
            flash('You have registered and are logged in as ' +
                  form.username.data, 'success')
            session['username'] = request.form['username']
            session['logged'] = True
            return redirect(url_for('index'))
        else:
            # if username already exists in db, notify
            username = request.form['username']
            flash('The username "' + username +
                  '" already exists. Please try a different username',
                  'warning')
            return redirect(url_for('register'))
    # load registration form
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    '''
    Function to allow a user to log into site with valid details.
    Session created on sucessful log in and user notified. User also informed
    of unsucessful login.
    '''
    form = LoginForm()
    if 'logged' in session:  # if a session currently exists notify user

        # don't let logged in user log in again and send to index
        flash('You are already logged in on this device as  ' +
              session['username'], 'warning')
        return redirect(url_for('index'))

    if form.validate_on_submit():

        # if log in form passes all validation check if username  exists
        users = mongo.db.users
        find_user = users.find_one({'username': request.form['username']})
        if find_user:  # if user is found in db
            password = form.password.data
            if find_user['password'] == password:
                # if password entered matches whats in db for paticluar user

                myreviews_link = \
                    Markup(' Go to <a href="/myreviews">My Reviews</a>' +
                           ' to view your reviews')
                flash('You  are logged in as  "' + form.username.data + '" ' +
                      myreviews_link, 'success')
                session['username'] = request.form['username']
                session['logged'] = True
                return redirect(url_for('index'))
            else:
                # if passwords dont match
                flash('Your password is incorrect.' +
                      ' Please log in again with correct details',
                      'warning')

                return redirect(url_for('login'))
        else:
            # if user not found in db
            register_link = Markup('<a href="/register">Register</a>')
            flash('User "' + form.username.data + '" does not exist, please ' +
                  register_link +
                  ' if you do not already have a valid username',
                  'warning')
            return redirect(url_for('login'))

    return render_template('login.html', title='Login', form=form)


@app.route('/sign-out')
def sign_out():
    '''
    function to allow a user to sign out of the current session
    '''

    session.clear()  # Clear session, notify user and redirect to index
    flash('You are now signed out', 'success')
    return redirect(url_for('index'))


@app.route('/myreviews')
def my_reviews():
    '''
    Function to display a 'my reviews' page which displays only the
    reivews of the logged in user
    '''

    if 'logged' in session:
        # only let a logged in user edit thier own review page
        flash('This is your reviews page. ' +
              'View, edit and add your own reviews from here',
              'success')
        current_user = session['username']
        # setting db username to the current session username

        reviews = mongo.db.reviews.find({'username': current_user})
        return render_template('myreviews.html',
                               reviews=reviews,
                               title='My Reviews')
    else:
        # if user is not logged in
        flash('You need to be logged in to see your reviews', 'warning')
        return redirect(url_for('login'))


@app.route('/addreview', methods=['GET', 'POST'])
def add_review():
    '''
    Function to display a page which displays a form to
    add a review for logged in user
    '''

    if 'logged' not in session:
        # if a user trys to go to add review without been logged in
        flash('You need to log in to add a review', 'warning')
        return redirect(url_for('login'))  # sending to log in

    form = ReviewForm()
    if form.validate_on_submit():
        # if form submits successfully
        reviews = mongo.db.reviews

        # creating amazon link
        amazon_link = create_amazon_search(request.form['book_title'])

        icon = get_icon_class(request.form['category'])
        # creating icon font awesome class

        # add form content to db as a new record
        reviews.insert_one({
            'author': request.form['author'],
            'book_title': request.form['book_title'],
            'summary': request.form['summary'],
            'review': request.form['review'],
            'category': request.form['category'],
            'amazon': amazon_link,
            'icon': icon,
            'upvote': 0,
            'username': session['username'],
            })
        flash('Review added ', 'success')

        # send to my reviews template on successful add
        return redirect(url_for('my_reviews'))

    return render_template('addreview.html', form=form,
                           title='Add Review')


@app.route('/editreview/<id>', methods=['GET', 'POST'])
def edit_review(id):
    '''
    Function to display a page which displays
    a form to edit a review for logged in user
    '''

    if 'logged' not in session:
        # if a user trys to go to edit review without been logged in

        flash('You need to log in to edit a review', 'warning')
        return redirect(url_for('login'))  # sending to log in

    one_review = mongo.db.reviews.find_one({'_id': ObjectId(id)})
    # retrieving record from db

    # if a user trys to go to edit review that they don't own
    if one_review['username'] != session['username']:
        flash('You do  not own this review and cannot edit it. ',
              'warning')
        return redirect(url_for('login'))  # sending to log in

    form = ReviewForm(data=one_review)

    if form.validate_on_submit():  # if form submits successfully
        reviews = mongo.db.reviews

        # creating amazon link
        amazon_link = create_amazon_search(request.form['book_title'])
        icon = get_icon_class(request.form['category'])
        # creating icon font awesome class

        # add form content to db as a new record
        reviews.update_one({'_id': ObjectId(id)}, {'$set': {
            'author': request.form['author'],
            'book_title': request.form['book_title'],
            'summary': request.form['summary'],
            'review': request.form['review'],
            'category': request.form['category'],
            'amazon': amazon_link,
            'icon': icon,
            }})

        flash('Review Updated ', 'success')

        # send to my review template on successful addupdate
        return redirect(url_for('review', id=id))

    return render_template('editreview.html', form=form,
                           title='Edit a  Review')


@app.route('/delete/<id>', methods=['GET', 'POST'])
def delete_review(id):
    # function to allow a logged in user delete their own reviews
    if 'logged' not in session:
        '''
        In app journey only a logged in user will see the delete
        button, however i am adding a logged in query to the route
        for further security to prevent url manipulation
        '''
        flash('You need to log in to delete a review', 'warning')
        return redirect(url_for('login'))  # sending to log in

    # retrieving record from db

    # if a user trys to go to edit review that they don't own
    one_review = mongo.db.reviews.find_one({'_id': ObjectId(id)})
    if one_review['username'] != session['username']:
        flash('You do not own this review and cannot delete it.' +
              'A user can only edit or delete their own reviews',
              'warning')
        return redirect(url_for('index'))  # sending to log in

    flash("You have successfully deleted your review.",
          'warning')
    mongo.db.reviews.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('index'))


@app.route('/search', methods=['GET', 'POST'])
def search():
    '''
    Function to allow a full text search of the db. Created an index on mongo
    db in atlas to allow a full text search of all string fields using
    ( { "$**": "text" } ) as the index settings
    '''

    # passing contents of search field to search variables
    search = request.args['search']
    category = request.args['category']

    if search != '' and category != 'none':
        # checking for both search and filter been attempted at the same time

        # pagination section
        total = \
            mongo.db.reviews.count_documents({'$and':
                                             [{'$text': {'$search': search}},
                                              {'category': category}]})

        # setting the current page of pagination
        current_page = int(request.args.get('current_page', 1))

        offset = int(request.args.get('offset', 0))
        # setting offset initially to 0 (position in db for current page)

        max_pages = int(math.ceil(total / page_limit))
        # calculating max pages needed to display all records

        page_range = (1, max_pages)
        # creating a tuple with the page range in it

        find_reviews = \
            mongo.db.reviews.find({'$and':
                                  [{'$text': {'$search': search}},
                                   {'category': category}]
                                   }).limit(page_limit).skip(offset)
        count_doc = \
            mongo.db.reviews.count_documents({'$and':
                                             [{'$text': {'$search': search}},
                                              {'category': category}]})
        if count_doc == 0:
            # if no records found for category selection and site search

            flash('There are no reviews currently in the "' +
                  category.title() + '" category using "' + search +
                  '" as the site search', 'warning')
            return redirect(url_for('index'))

        flash('Search Results for "' + search + '" filtered by "' +
              category.title() + '" category', 'success')

        return render_template(
            'search.html',
            title='Search',
            reviews=find_reviews,
            total=total,
            page_limit=page_limit,
            current_page=current_page,
            offset=offset,
            max_pages=max_pages,
            page_range=page_range,
            search=search,
            category=category,
            )
    elif search == '' and category == 'none':
        # checking if user has not entered text into search or used filter
        flash('You have not selected a category or enterd text ' +
              ' the search field', 'warning')
        return redirect(url_for('index'))

    elif search == '' and category != 'none':
        # checking for just filter selection

        # pagination section
        total = \
            mongo.db.reviews.count_documents({'category':
                                             {'$regex': category}})
        # total records in query

        # setting the current page of pagination
        current_page = int(request.args.get('current_page', 1))

        offset = int(request.args.get('offset', 0))
        # setting offset initially to 0 (position in db for current page)

        max_pages = int(math.ceil(total / page_limit))
        # calculating max pages needed to display all records

        page_range = (1, max_pages)
        # creating a tuple with the page range in it

        # searching db for the selected category in filter
        find_reviews = \
            mongo.db.reviews.find({'category':
                                  {'$regex': category}
                                   }).limit(page_limit).skip(offset)
        count_doc = \
            mongo.db.reviews.count_documents({'category':
                                             {'$regex': category}})

        if count_doc == 0:  # if no records found for category selection
            flash('There are no reviews currently in the "' +
                  category.title() + '" category', 'warning')
            return redirect(url_for('index'))

        flash('Results showing "' + category.title() + '" reviews only ',
              'success')
        return render_template(
            'search.html',
            title='Search',
            reviews=find_reviews,
            total=total,
            age_limit=page_limit,
            current_page=current_page,
            offset=offset,
            max_pages=max_pages,
            page_range=page_range,
            search=search,
            category=category,
            )
    elif search != '' and category == 'none':
        # checking for just search text entry

        # pagination section
        total = \
            mongo.db.reviews.count_documents({'$text': {'$search': search}})
        # total records in query

        # setting the current page of pagination
        current_page = int(request.args.get('current_page', 1))

        offset = int(request.args.get('offset', 0))
        # setting offset initially to 0 (position in db for current page)

        max_pages = int(math.ceil(total / page_limit))
        # calculating max pages needed to display all records

        page_range = (1, max_pages)
        # creating a tuple with the page range in it

        # running find on contents of search box using multifield text search
        find_reviews = \
            mongo.db.reviews.find({'$text':
                                  {'$search': search}
                                   }) .limit(page_limit).skip(offset)
        count_doc = \
            mongo.db.reviews.count_documents({'$text': {'$search': search}})
        if count_doc == 0:

            # if no records found for site search

            flash('There are no search results for "' + search +
                  '" in the site search. Please try a different search, or' +
                  ' combination of words if using small regular words such ' +
                  'as "the" or "on"', 'warning')
            return redirect(url_for('index'))
        flash('Search results for "' + search + '"', 'success')
        return render_template(
            'search.html',
            title='Search',
            reviews=find_reviews,
            total=total,
            page_limit=page_limit,
            current_page=current_page,
            offset=offset,
            max_pages=max_pages,
            page_range=page_range,
            search=search,
            category=category,
            )


@app.errorhandler(400)
def bad_request(e):
    """Route for handling 400 errors"""

    return render_template('400.html', title='Bad request!')


@app.errorhandler(404)
def page_not_found(e):
    """Route for handling 404 errors"""

    return render_template('404.html', title='Page not found!')


def create_amazon_search(book):
    '''
    function to build an amazon search link based on the book
    title entered by the user
    '''

    amazonlink = 'https://www.amazon.com/s?i=stripbooks-intl-ship&k='
    while ' ' in book:  # replace spaces with +
        book = book.replace(' ', '+')
    amazonlink += book

    return amazonlink  # returning newly built link


def get_icon_class(cat):
    '''
    function to check the review category assign by the user and to return
    the relevant font awesome icon classes based on the category sent in
    '''

    # modify thisand the AddReviewForm class in forms.py to add new categorys

    icons = {
        'factual': 'fa fa-picture-o',
        'fiction': 'fa fa-picture-o',
        'health': 'fa fa-heartbeat',
        'nature': 'fa fa-leaf',
        'science': 'fa fa-cogs',
        'sport': 'fa fa-futbo-o',
        'world history': 'fa fa-globe',
        }
    return icons[cat]  # returning relevant classes


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=os.environ.get('PORT'),
            debug=True)
