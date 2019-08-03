import os
from flask import Flask, render_template, redirect, request, url_for, session, flash

app = Flask(__name__)
app.secret_key = ('SECRET_KEY')



#setting default root
# testing flask
@app.route('/')
def index(): 
    return render_template("index.html")




if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)