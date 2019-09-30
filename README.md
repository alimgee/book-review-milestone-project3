
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
11. On the book review page, if I want to be able to delete or edit my reviews.
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
4. Users can use the search and filter functionality to search site content

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

  

I worked in sprints so every task was manually tested thoroughly via flash() messages or expected behaviors. I trialed google G suite and a kanban add on call [kanbanchi](https://gsuite.google.com/marketplace/app/kanbanchi/631025100586) as an agile task management tool. An csv output of most of the project tasks can be found in the [/documentation ](/documentation) folder. After each task completion, I would fully test it before moving on to the next task.

  

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

***Coding notes considerations to be added here***

## Deployment

I personally used vscode on my local machine to develop the site using Python 3.7.3  and deployed to Heroku via Github.

1. To download or clone the site to your local machine you will need to go to my [repo](https://github.com/alimgee/book-review-milestone-project3) see steps in https://help.github.com/en/articles/cloning-a-repository .
2.  Before you download or clone the site you will need to ensure you have [Python 3.7](https://www.python.org/downloads/) installed. 
3. Once you have Python installed, created a virtual environment as appropriate to you chosen IDE.
4. Run the requirements.txt file as appropriate to your IDE to install the relevant package dependencies for the project into your virtual environment.
5. Run the app.py file as appropriate to your chosen environment.
6. You should now be able to view the site on your localhost on port 5000.

### Acknowledgements

  

<strong>Code Institute</strong> tutors for their assistance in getting me this far in the course.

All the folk in the <strong>Code Institute Slack </strong> for their invaluable input to their fellow members development. I also learned a lot for this project from the [Corey Schaffer](https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g) series of you tube videos on python and flask, which assisted in particular my understanding of the usage of wtforms.

  
  

#### Disclaimer

The content of this website is educational purposes only and should not be used on a real world basis.
