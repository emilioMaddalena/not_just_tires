'''
This will become a nice website in the future!
'''

from crypt import methods

from flask import Flask, flash, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

from not_just_tires.secrets import MYSQL_PASSWORD, MYSQL_USERNAME, MYSQL_DB_NAME, FLASK_APP_KEY

app = Flask(__name__)
app.secret_key = FLASK_APP_KEY

table_name = 'my_table'
app.config['SQLALCHEMY_DATABASE_URI'] = ''.join(['mysql://', MYSQL_USERNAME, ':', MYSQL_PASSWORD, '@localhost/', MYSQL_DB_NAME])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Entry(db.Model):
    
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(100))
    age = db.Column("age", db.String(100))
    desert = db.Column("desert", db.String(100))
    
    def __init__(self, name, age, desert):
        self.name = name
        self.age = age
        self.desert = desert

@app.route('/')
def index():
    my_msg = "We greet the user to our beautiful web page."
    return render_template("index.html", message=my_msg)

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template("error.html"), 404

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "GET":
        # the user is requesting the form
        return render_template("form.html")
    
    elif request.method == "POST":
        # the user has submitted something
        if not all(request.form.values()): print("Please, complete the whole form before submitting it.")
        form = request.form # that's a dict
        
        # adding form data into DB
        entry = Entry(name=form["name"], age=form["age"], desert=form["desert"])
        db.session.add(entry)
        db.session.commit()
        
        print('You\'ve successfully submitted your data! 🌝')
        return render_template("form.html")
        
if __name__ == '__main__':
    db.create_all()
    app.run()
