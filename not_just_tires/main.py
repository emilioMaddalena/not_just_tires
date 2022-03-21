'''
This will become a nice website in the future!
'''

from crypt import methods

from flask import Flask, flash, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

import pymysql

from secrets import MYSQL_PASSWORD, MYSQL_USERNAME, MYSQL_DB_NAME, FLASK_APP_KEY

app = Flask(__name__)
app.secret_key = FLASK_APP_KEY

app.config['SQLALCHEMY_DATABASE_URI'] = ''.join(['mysql+pymysql://', MYSQL_USERNAME, ':', MYSQL_PASSWORD, '@localhost/', MYSQL_DB_NAME])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Test(db.Model): # has to match the DB table you're targeting
    
    _id = db.Column("id", db.Integer, primary_key=True)
    num = db.Column("num", db.Integer)
    # data_transacao = db.Column("data_transacao", db.Integer)
    # quantidade = db.Column("quantidade", db.Integer)
    # tipo_pneu = db.Column("tipo_pneu", db.String(100))
    # valor_unit = db.Column("valor_unit", db.Float)
    # valor_tot = db.Column("valor_tot", db.Float)
    # cliente = db.Column("cliente", db.String(100))
    # tipo_transacao = db.Column("tipo_transacao", db.String(100))
    
    def __init__(self, num):
        self.num = num
        
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
        #entry = Entry(name=form["name"], age=form["age"], desert=form["desert"])
        test = Test(num=form["num"])
        db.session.add(test)
        db.session.commit()
        
        print('You\'ve successfully submitted your data! 🌝')
        return render_template("form.html")
        
if __name__ == '__main__':
    #db.create_all()
    app.run()
