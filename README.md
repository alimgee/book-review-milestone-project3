
<h1  align="center">
<a  href=""  target="_blank"><img  src="/documentation/desktopBB.png"  alt="Book Bites Screen"/></a>
<a  href=""  target="_blank"><img  src="/documentation/mobileBB.gif"  alt="Book Bites mobile Screen"/></a>
</h1>
<h2  align="center">
BOOK BITES
</h2>
<div  align="center">

  

This is project is part of the 'DataCentric Milestone Prolect 3' module of the Code Institute Full Stack Software Development course. The marks from this project contribute to the receipt of a diploma level award.

<br>
</div>

  

## Table of Contents

1.  [**UX**](#ux)
-  [**Project Goals**](#project-goals)
-  [**User goals**](#user-goals)
-  [**User Stories**](#user-stories)
-  [**Design**](#design)
-  [**Wireframes**](#wireframes)

  
2.  [**Features**](#features)
-  [**Existing Features**](#existing-features)
-  [**Features Left to Implement**](#features-left-to-implement)
3.  [**Database**](#database)
4.  [**Technologies used**](#technologies-used)
5.  [**Testing**](#testing)
6.  [**Coding Notes**](#coding-notes)
7.  [**Deployment**](#deployment)
8.  [**Acknowledgements**](#acknowledgements)
9.  [**Disclaimer**](#disclaimer)

  
## UX

  

### Project Goals

  
The aim of this project is to  create a book review website that allows a user to read other users reviews of books they have read, and to also allow a user to create an account and add their own reviews to the site. i wanted to created a site that is easy on the eye and conducive to reading the reviews, in an uncluttered and clean space.

  

#### User goals
User goals in brief are as follows:

 1. To view other users book reviews and give a like to reviews
  2. To create an account on the site
   3. To add a review of their own and edit any existing ones they have
   4. To remove their reviews and account if they wish
   5. To have an amazon link that leads to the book

  

#### User Stories

1. I want to see book review summarys when i go to the landing page of the site.
2. I want reviews per page to be limited to a small amount with the ability to view all reviews through pagination.
3. Summary reviews on landing page should have button links to the full review.
4. The full book review should show the original user who created the review.
5. The full book review should show what category the book has been assigned to.
6. The full book review should show the full review, summary, author and book name.
7. The full book review should allow me to give the review a like and to link to the book in the amazon site.
8. I would like to be able to register an account so i can create my own reviews.
9. I would like to be able to log in without issues when i use the correct log in details.
10. I should not be able to edit or delete a review that is not mine.
11. On the book review page, I want to be able to delete or edit my reviews.
12. I want the abilty to view my profile and i should be able to view any reviews associated to my account.
13. I would like to be able to remove my account should i choose.
14. There should be options to register and login on the site navigation,
15. If im logged in i should see navigation options to log out, view all my reviews and to view my profile.

  

### Design

  
**Fonts**

I decided to use the 'Ubuntu' font from google("https://fonts.googleapis.com/css?family=Ubuntu") as i felt that it was an 'easy on the eye' font and aided reading the reviews.


**Colours**

![#E8D0A9](https://placehold.it/15/E8D0A9/000000?text=+) ***#E8D0A9***  ![#B7AFA3](https://placehold.it/15/B7AFA3/000000?text=+) ***#B7AFA3***![#C1DAD6](https://placehold.it/15/C1DAD6/000000?text=+) ***#C1DAD6***  ![#F5FAFA,](https://placehold.it/15/F5FAFA,/000000?text=+) ***#F5FAFA,***  ![#ACD1E9](https://placehold.it/15/ACD1E9/000000?text=+) ***#ACD1E9***  ![#6D929B](https://placehold.it/15/6D929B/000000?text=+) ***#6D929B***

I went with a soft blue / green colour scheme as i think the colours on a book site should be muted and non intrusive on the review itself for ease of reading. I found my [colour scheme](https://www.colorcombos.com/color-schemes/124/ColorCombo124.html) on colorcombos.com site and based my colour scheme off this.

From the site - "*This color palette contains the following web hex color codes: #E8D0A9, #B7AFA3, #C1DAD6, #F5FAFA, #ACD1E9, #6D929B. The colors from this colour combination are described by the following tags: BABY BLUE, BLUE, BLUE GREEN, CATSKILL WHITE, GOTHIC, JET STREAM, LIGHT BLUE, NOMAD, ORANGE, REGENT ST BLUE, TAN, ZOMBIE*."

**Topography**

The site uses bootstrap 4 to be fully responsive across multiple devices, also some media queries were used to change how the intro text appears across different devices to provide a smooth user experience.

### Wireframes

WIreFrames were created using balsamiq tool with license key provided by the Code Institute. https://balsamiq.com/ and came be found in the  [/documentation ](/documentation) folder.  The wireframes were created at the very start of the project. Throughout development scope changed,  i adjusted the layouts as appropriate to the projects end goals, there were also new pages added to accommodate journeys not initially thought of that became needed as the project progressed.

  

## Features

### Existing Features

1. Users can use pagination to view all reviews.
2. Users can create unique usernames to login and add, edit and delete a review.
3. Users can remove their own profiles.
4. Users can use the search and filter functionality to search site content.
5. Users can click on an amazon search link to find the relevant book.

### Future Features to Implement

Future versions of the project may have the following:

1. Ability to reset an account password.
2. Ability for user to view in their profile all likes they have added to other reviews.
3. Prevent the user adding multiple likes to the a review.
4. Prevent a user liking their own review.

 

## Database

MongoDB Atlas is used as my database backend for storing user and review details. There are 2 colllections, 'users' and 'reviews', 'user' holds the session details - username and password, 'reviews' holds the full book review details. As MongoDB is a non relational db model I both collections share the username an unique identifier that ties records in both collections together.

### Database schema

**users collection:**

```
{
"_id":"",
"username":"",
"password":""
}
```
**reviews collection:**
```

{
"_id":"",
"author":"",
"book_title":" ",
"summary":".",
"review":"",
"category":"",
"amazon":"",
"icon":"",
"upvote":{"$numberInt":""},
"username":""
}

```

  

## Technologies Used

  

This project utilizes Python, Flask, MongoDB, HTML, CSS and JavaScript technologies.

  

-  [Python](https://www.python.org/)
The project uses **Python 3** to create the app, create the routes, create the functions within those routes and handles all back end interactions.

-  [Flask](https://flask.palletsprojects.com/en/1.1.x/)
The project uses **Flask 1.1** framework to create and populate the templates.

-  [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
The project uses **MongoDB Atlas** as a backend database.

- [JQuery](https://jquery.com)
 The project uses **JQuery** as part of bootstrap 4 and to create a character counter on the text area fields.

-  [Bootstrap 4](https://getbootstrap.com/)
The project uses **Bootstrap** to simplify the structure of the website and make the website responsive easily.

-  **HTML 5 and CSS3**
The project uses **HTML5 and CSS3** for website structure and design.

-  [Google Fonts](https://fonts.google.com/)
The project used the **Google 'Ubuntu' font** across the site

-  [GitHub](https://github.com/)
This project uses **GitHub** to remotely store the source code in a repository. The project can be cloned or downloaded from here. See [Deployment](#deployment) section

-  [StackEdit](https://stackedit.io)
This project uses **StackEdit** to build the markdown for this readme file

 
  
  

## Testing

  

I worked in sprints so every task was manually tested thoroughly via flash() messages or expected behaviors. I trialed google G suite and a kanban add on call [kanbanchi](https://gsuite.google.com/marketplace/app/kanbanchi/631025100586) as an agile task management tool. An pdf output of most of the project tasks can be found in the [/documentation ](/documentation) folder. After each task completion, I would fully test it before moving on to the next task.

  

I initially tried using unit testing on the landing page but as this was my first major python / Flask / MongoDB project i decided to focus on learning these skill-sets and use a manual testing process instead, checking that the outputs form the functions were as expected using screen printouts.

  

When the project was fully completed i went through the below testing scenarios to further test the project.

  

| Test | Expected |Passed |
| :------------- |:-------------| :-----:|
| User loads the landing page of site | Page displays without error and reviews can be viewed | &#9745; |
| User loads the homepage of the site | Reviews are displayed by upvote bite like value in descending order | &#9745; |
| User selects the 'review' button of a particular review on homepage | Review page displays without error and the correct review can be viewed | &#9745; |
| User selects the 'review' button of a particular review on homepage whilst not logged in | Review page displays without error and the correct review can be viewed and the 'edit and 'delete' buttons are not visible | &#9745; |
| User clicks on the upvote bite like on a review page | bite like should increase by 1 | &#9745; |
| User clicks on amazon link on a review page | amazon site should load and show a link to the book if it exists in amazon based on the book title | &#9745; |
| User clicks on delete button on review page when logged in | delete modal should pop up with warning and confirm / cancel buttons | &#9745; |
| User clicks on confirm delete button on review page delete modal when logged in | review is removed from the db and confirmation message displayed | &#9745; |
| User clicks on any nav link | All nav links should be fully functional both logged in and logged out and go to the correct destination | &#9745; |
| User clicks on any nav link | All nav links should be fully functional both logged in and logged out and go to the correct destination | &#9745; |
| User logs in | Nav items change from ***login***, ***register*** and ***about*** to ***my profile***, ***my reviews***, ***about*** and ***log out*** | &#9745; |
| User selects ***Register*** from top nav | Register form page loads | &#9745; |
| User enters username smaller than 3 characters and larger than 20 characters and clicks ***Register Now***| Form does not submit and shows error message to user that username must be between 3 and 20 characters long | &#9745; |
| User enters correct **username** but enters different values in ***password*** and ***confirm password*** fields| Form does not submit and shows error message to user that passwords must match | &#9745; |
| User enters correct ***username*** and ***password*** and ***confirm password*** fields match| Forms submits, landing page is loaded with message confirming successful registration | &#9745; |
| User selects ***log In*** from top nav | ***log in*** form page loads | &#9745; |
| User enters username smaller than 3 characters and larger than 20 characters and clicks ***Log in Now***| Form does not submit and shows error message to user that username must be between 3 and 20 characters long | &#9745; |
| User enters correct **username** and enters correct values in ***password*** field of log in form| form submits and logs customer in and message is displayed to show successful log in | &#9745; |
| User enters correct **username** but enters the wrong values in ***password*** field of log in form| Form does not submit and shows error message to user that password is incorrect | &#9745; |
| User enters incorrect **username** | Form does not submit and shows error message to user that the user does not exist and shows a link to register | &#9745; |
| User tries to **edit** / **delete** a review that they havent created under their username | User is messaged that they can't delete / edit reviews they do not own | &#9745; |
| User **edits** a **review** they own| All edits are submitted successfully once they pass form validation and can be seen when review loads | &#9745; |
| User selects to **delete** a **review** they do not own| user gets warning message informing that they cant delete someone else review | &#9745; |
| User selects to **confirm delete** on delete modal| review is removed from list of reviews and user message| &#9745; |
| User selects to **cancel delete** on delete modal| review is not removed from list of reviews and user return to review page| &#9745; |
| User selects to **delete profile**| delete profile modal pops up with warning| &#9745; |
| User selects to **cancel delete profile** on modal| user is returned to profile without any removals| &#9745; |
| User selects **confirms to delete profile**| profile and all associated reviews are removed, user seesion is removed and user is sent back to index| &#9745; |




  

## Coding Notes
Some of the features of the code are as follows:
###  Displaying and sorting the reviews on the homepage
The landing page uses an index function to determine actions on homepage
~~~
@app.route('/', methods=['GET', 'POST'])
def index():
~~~
The index function makes a call to the Mongodb 'reviews' database and returns all records of reviews added to the 'reviews' collection in descending order using the 'upvote' field in the collection to sort. I am using the limit() and skip() functionality for pagination on the loaded page.
~~~
reviews = \
mongo.db.reviews.find().sort('upvote', pymongo.DESCENDING)\
.limit(page_limit).skip(offset)
~~~
### Pagination of the collection query results on the landing page

The pagination section of the landing page in index,html determines the values of 'current_page' and 'offset' when the user selects the next or previous buttons. The section also displays to the user the current page and the total number of pages. These values are passed to the index function on each click of the ''previous' or 'next' buttons and are detailed further below.
~~~
<!-- pagination -->
<!--requst.args.get function is used in the search route to keep track of offset and current page-->
<ul class="pagination pagination-sm justify-content-center">
{%if offset >0 %}
<!-- if offset is greater than 0 this means that the next button has been clicked previously so then show the previous button -->
<li class="page-item"><a class="page-link" title="Previous" href="{{url_for('index', current_page=current_page-1, offset=offset-page_limit )}}">Previous</a></li>
{% endif %}
<!-- showing user current page of total pages -->
<li class="page-item disabled"><a class="page-link" href="#">Page {{ current_page}} of {{max_pages}}</a></li>
{% if current_page < max_pages %}
<!-- if current page remains less than the maximum page count then show the next button--></max_pages>
<li class="page-item"><a class="page-link" title="Next" href="{{url_for('index', current_page=current_page+1, offset=offset+page_limit )}}">Next</a></li>
{% endif %}
</ul>
~~~
The index function also paginates the the results of the db query using the setting of the 'page_limit' global variable. This will tell the function to show 4 reviews on every page when either 'next' or 'previous' are selected on index.html.
~~~
page_limit = 4
~~~
The total number of records in the db query is stored in the 'total' variable.
~~~
total = mongo.db.reviews.count_documents({})
# total records in reviews db
~~~

The 'current_page' variable stores the current page the user is on, this will increase or decrease depending on whether the user selects the next or previous buttons on the page, this defaults to page 1 on first load of the page. I use the 'request.args.get' function to retrieve from the page the value of which button that is selected by the user.
~~~
# setting the current page of pagination
current_page = int(request.args.get('current_page', 1))
~~~
The 'offset' variable keeps track of where the pagination should begin of a particular page. eg. on first index page load 'offset' is set to 0 so it will start at the beginning of the query and display the amount of records set in the 'page_limit' variable (4), when the next button is clicked the offset value is then set to 4, the page will then load the next 4 records starting from the offset value of 4 and so on with each click of next. This variable values will reverse when previous option is selected by the user.
~~~
offset = int(request.args.get('offset', 0))
# setting offset initially to 0 (position in db for current page)
~~~
The 'max_pages' variable calculates the maximum number of pages needed to display all the records in the collection, which would be the total number of records divided by the amount of records to be put on each page.
~~~
max_pages = int(math.ceil(total / page_limit))
# calculating max pages needed to display all records
~~~
All values are then rendered to the index.html template
~~~
return render_template(
'index.html',
reviews=reviews,
total=total,
page_limit=page_limit,
current_page=current_page,
offset=offset,
max_pages=max_pages,
)
~~~
### Returning the full review from the db 
I encountered an issue when loading the full review page template 'review.html' which displays the relevant fields of the record from the db. When the full review field was been called from the db it intially returned the text as a full block of text with no paragraphs.  To fix this i passed the 'review' field to a variable 'formatted_review' , i then used the re.split functionality to find carriage returns or new lines characters in the review and to split the content of 'formatted_review' into a list of strings which i then loop through on the 'review.html, template to display as paragraphs
~~~
@app.route('/review/<id>', methods=['GET', 'POST'])
def review(id):
~~~
~~~
'''
Need to display paragraphs if entered by user into
the review field
'''
formatted_review = one_review['review']
# creating a list of strings from review field split on new lines
formatted_review = re.split(r"[~\r\n]+", formatted_review)
# pass review strings list into template to be looped through
~~~
~~~
<div class="col-12"><span class="review-title text-capitalize"><strong>Book
Review:</strong></span><br>
{% for paragraph in formatted_review %}
<p>{{ paragraph }}</p>
{% endfor %}</div>
</div>
~~~
### Sessions
For all the edit, delete and profile functionality i use sessions stored on the local machine when the user logs in to check that the user is the owner of the review or profile before allowing the user to preform the requested action. This is used as defensive security to ensure a user cannot do something they should be able to.

When a user logs in a check is done to make sure they aren't already logged in
~~~
def login():

form = LoginForm()
if 'logged' in session: # if a session currently exists notify user
# don't let logged in user log in again and send to index
flash('You are already logged in on this device as ' +
session['username'], 'warning')
return redirect(url_for('index'))
~~~
If the user is not already logged in and enters a correct username / pwd a session is created with their username stored in the session on the local machine which then allows me to check from any other function or template who the user is and whether they can preform certain actions based on db checks.
~~~
if find_user: # if user is found in db
password = form.password.data
if check_password_hash(find_user['password'], password):
# if password entered matches whats in db for paticluar user
myreviews_link = \
Markup(' Go to <a href="/myreviews">My Reviews</a>' +
' to view your reviews')
flash('You are logged in as "' + form.username.data + '" ' +
myreviews_link, 'success')
session['username'] = request.form['username']
session['logged'] = True
~~~
~~~
@app.route('/myprofile/')
def my_profile():
if 'logged' in session:
# only let a logged in user edit their own profile page
current_user = session['username']
flash('Hi "' + current_user + '". This is your profile ' +
'page. You can view a summary of your reviews and' +
' delete your profile from here', 'success')
~~~
~~~
@app.route('/addreview', methods=['GET', 'POST'])
def add_review():
if 'logged' not in session:
# if a user trys to go to add review without been logged in
flash('You need to log in to add a review', 'warning')
return redirect(url_for('login')) # sending to log in
~~~
~~~
@app.route('/delete/<id>', methods=['GET', 'POST'])
def delete_review(id):

flash('You need to log in to delete a review', 'warning')
return redirect(url_for('login')) # sending to log in
# retrieving record from db
# if a user trys to go to edit review that they don't own
one_review = mongo.db.reviews.find_one({'_id': ObjectId(id)})
# retrieving record from db
# if a user trys to go to edit review that they don't own
if one_review['username'] != session['username']:
flash('You do not own this review and cannot delete it.' +
' A user can only edit or delete their own reviews',
'warning')
return redirect(url_for('index')) # sending to log in
~~~
from review.html template:
~~~
<!-- ony show edit and delete buttons if the user is logged in -->
{% if session['logged'] == True %}
<div class="row mb-4 text-center">
<div class="col-12 col-md-6 mb-3"><a href=" {{ (url_for('edit_review', id=review._id )) }} " class="btn btn-info" title="Edit Review">Edit
Review</a></div>
<div class="col-12 col-md-6 mb-2">
<button type="button" class="btn btn-danger" data-toggle="modal" data-target="#deleteModal" title="Delete Review">Delete Review</button></div></div>
{% endif %}
~~~
All sessions are cleared when the user selects the 'log out' button.
~~~
@app.route('/sign-out')
def sign_out():
session.clear() # Clear session, notify user and redirect to index
flash('You are now signed out', 'success')
return redirect(url_for('index')) 
~~~

### Search

The search box is positioned in the base.html template so it appears across all pages. The values entered in the search input field and the category select field are returned to the search function upun the user selecting the search button, where querys will be processed based on the values entered.
~~~
<div class="mt-4 ml-4"><br>
<!-- Search form -->
<form class="form-inline" action="{{ (url_for('search')) }}">
<div class="form-group ">
<input class="form-control-sm mr-1 searchbar small" type="text" 
placeholder="Search Site" name="search" size="12">
~~~
~~~
<button class=" mr-1 searchbar small mr-1"
type="submit"><strong><i class="fa fa-search" aria-hidden="true"></i>
</strong></button>
~~~
~~~
<label for="category" class="small mr-2"><strong>Filter By:</strong> </label>
<select class="form-control-sm mr-1 searchbar small" id="category" name="category">
<option>none</option>
<option>comedy</option>
<option>drama</option>
<option>education</option>
<option>factual</option>
<option>fiction</option>
<option>health</option>
<option>history</option>
<option>music</option>
<option>nature</option>
<option>science</option>
<option>sport</option></select></div></form>
~~~
The search function takes the values posted when the search button is clicked using the request.args.get functionality.
~~~
@app.route('/search', methods=['GET', 'POST'])
def search():
search = request.args['search']
category = request.args['category']
~~~
If the user enters a value in the search box and selects a category filter the search will query the db for the value entered. The mongodb is text indexed which will allow a query of all fields in the relevant collection to be run. The search as part of the same query will also check that the category fields in the returned query also match what the user has selected in the filter. The search also uses the earlier discussed pagination functionality which is used on the landing page.
~~~
if search != '' and category != 'none':
# checking for both search and filter been attempted at the same time
find_reviews = \
mongo.db.reviews.find({'$and':[{'$text': {'$search': search}},{'category': category}]
}).limit(page_limit).skip(offset)
~~~
The records returned by the query are counted using the count_documents functionality, if there are no records for the search result the user is informed and returned to the index page, otherwise if records are found the results of the search is rendered to the 'search.html' template
~~~
count_doc = \
mongo.db.reviews.count_documents({'$and':[{'$text': {'$search': search}},{'category': category}]})
if count_doc == 0:
# if no records found for category selection and site search
flash('There are no reviews currently in the "' +
category.title() + '" category using "' + search +
'" as the site search', 'warning')
return redirect(url_for('index'))
flash('Search Results for "' + search + '" filtered by "' +
category.title() + '" category', 'success')
return render_template('search.html',title='Search',reviews=find_reviews,
total=total,page_limit=page_limit,current_page=current_page,offset=offset,
max_pages=max_pages,,search=search,category=category,
)
~~~
If the user clicks search button without entering text in the search field and doesnt select a filter search either they are infromed and returned to the index template.
~~~
elif search == '' and category == 'none':
# checking if user has not entered text into search or used filter
flash('You have not selected a category or enterd text ' +
' the search field', 'warning')
return redirect(url_for('index'))
~~~
If the user selects a catergory but doesnt enter text in the search field the search function will query the collection to find all reviews the match the selected category when the category field is queried. The function will again check for no records and message accordingly, if records are found the user will also be informed and the 'search.html' template will load the results.
~~~
elif search == '' and category != 'none':
# checking for just filter selection
# searching db for the selected category in filter
find_reviews = \
mongo.db.reviews.find({'category':
{'$regex': category}
}).limit(page_limit).skip(offset)

count_doc = \
mongo.db.reviews.count_documents({'category':
{'$regex': category}})
if count_doc == 0: # if no records found for category selection
flash('There are no reviews currently in the "' +
category.title() + '" category', 'warning')
return redirect(url_for('index'))

flash('Results showing "' + category.title() + '" reviews only ',
'success')

~~~
The search also checks for text only entry in the search field and returns all records to the search.html template from running the query. As its a text indexed db all fields in the collection are queried. And as before if the query returns no results the user is informed and returned to the landing page, otherwise the query results are returned to the search.html template paginated as previously described.
~~~
elif search != '' and category == 'none':
# checking for just search text entry

# running find on contents of search box using multifield text search
find_reviews = \
mongo.db.reviews.find({'$text':
{'$search': search}}) .limit(page_limit).skip(offset)
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
~~~
### Amazon link functionality

The amazon link functionality builds an amazon book search link based on the book title.
~~~
 # creating amazon link
        amazon_link = create_amazon_search(request.form['book_title'])
~~~
When the function is called it strips out spaces in the book title and replaces them with '+' to build up the search url. The function then returns the full url, which is then passed into the relevant field on the review record.
~~~
def create_amazon_search(book):
	amazonlink = 'https://www.amazon.com/s?i=stripbooks-intl-ship&k='
	while ' ' in book:  # replace spaces with +
        book = book.replace(' ', '+')
	amazonlink += book
       return amazonlink  # returning newly built link
~~~
The amazon link is stored in the' reviews' collection and is displayed in the template.
~~~
 <div class="col-md-6 mb-2"><a href="{{ review.amazon }} " class="btn amazon" target="_blank"> Search Amazon For Book </a>
~~~
### Setting category classes
The get_icon_class function is a very simple function that returns a font awesome class based on the category selection passed into the function that the user chooses when adding a new review or editing a review.
~~~
def get_icon_class(cat):
    # modify this and the AddReviewForm class in forms.py to add new categorys
    icons = {
        'comedy': 'fa fa-smile-o',
        'drama': 'fa fa-video-camera',
        'education': 'fa fa-book',
        'factual': 'fa fa-picture-o',
        'fiction': 'fa fa-rocket',
        'health': 'fa fa-heartbeat',
        'music': 'fa fa-music',
        'nature': 'fa fa-leaf',
        'science': 'fa fa-cogs',
        'sport': 'fa fa-futbol-o',
        'history': 'fa fa-globe',
        }
    return icons[cat]  # returning relevant classes

~~~

~~~
 icon = get_icon_class(request.form['category'])
~~~
### Other
I use **werkzeug.security** package to hash the password the user enters on registration.

I also use **wtforms** package to build the Registration, Login and Review forms. The forms are built in the forms.py file and called into the **app.py.** The forms are then called from the relevant template as per wtforms documentation, i use bootstrap classes to style the forms and also print out error messages return from the wtform to the user using a for loop in the template. 

Registration form in forms.py :
~~~
class RegistrationForm(FlaskForm):
username = StringField('Username', validators=[DataRequired(),
Length(min=3, max=20)])
password = PasswordField('Password', validators=[DataRequired()])
confirm_password = PasswordField('Confirm Password',
validators=[DataRequired(),
EqualTo('password')])
submit = SubmitField('Register Now')
~~~
username field and error checking in form on add_review template:
~~~
{{ form.author.label(class="form-control-label") }}
{% if form.author.errors %}
{{ form.author(class="form-control form-control is-invalid") }}
<div class="invalid-feedback">
{% for error in form.username.errors %}
<span>{{ error }}</span>
{% endfor %}
</div>
{% else %}
{{ form.author(class="form-control form-control") }}
{% endif %}
</div>
~~~
## Deployment

I personally used vscode on my local machine to develop the site using Python 3.7.3  and deployed to Heroku via Github.

1. To download or clone the site to your local machine you will need to go to my [repo](https://github.com/alimgee/book-review-milestone-project3) see steps in https://help.github.com/en/articles/cloning-a-repository .
2.  Before you download or clone the site you will need to ensure you have [Python 3.7](https://www.python.org/downloads/) installed. 
3. Once you have Python installed, created a virtual environment as appropriate to you chosen IDE and os.
4. Run the requirements.txt file as appropriate to your IDE to install the relevant required packages dependencies for the project into your virtual environment.
5. Run the app.py file as appropriate to your chosen environment and os.
6. You should now be able to view the site on your localhost on port 5000.

### Acknowledgements

<strong>Code Institute</strong> tutors for their assistance in getting me this far in the course.

All the folk in the <strong>Code Institute Slack </strong> for their invaluable input to their fellow members development. I also learned a lot for this project from the [Corey Schaffer](https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g) series of you tube videos on python and flask, which assisted in particular my understanding of the usage of wtforms.

  
  

#### Disclaimer

The content of this website is educational purposes only and should not be used on a real world basis.
