'''
This will become a nice website in the future!
'''

from crypt import methods

from flask import Flask, flash, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

import pymysql

from my_secrets import DB_ENDPOINT, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME, FLASK_APP_KEY
import utils

app = Flask(__name__)
app.secret_key = FLASK_APP_KEY

app.config['SQLALCHEMY_DATABASE_URI'] = ''.join(['mysql+pymysql://', DB_USER, ':', DB_PASSWORD, '@', DB_ENDPOINT, '/', DB_NAME])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

STATE = 'DEBUG'

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
        
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        my_msg = "We greet the user to our beautiful web page."
        return render_template("index.html", message=my_msg)

    if request.method == "POST":
        return redirect(url_for('form'))

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template("error.html"), 404

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "GET":
        # the user is requesting the form
        print('new GET message!', flush=True)
        return render_template("form.html")
    
    elif request.method == "POST":
        utils.print_deb(f"{request.form}", STATE)
        
        if not utils.check_mandatory_fields(request.form): 
            utils.print_deb('Fill all mandatory fields before submitting!', STATE)
         
        else:
            utils.print_deb('You\'ve successfully submitted your data!', STATE)
            
            form = request.form 
            
            # adding form data into DB
            # entry = Entry(name=form["name"], age=form["age"], desert=form["desert"])
            # test = Test(num=form["num"])
            # db.session.add(test)
            # db.session.commit()
            
    return render_template("form.html")

@app.route("/history-pre", methods=["GET", "POST"])
def historyPre():
    if request.method == "GET":
        return render_template("history-pre.html")
    
    elif request.method == "POST":
        
        num = request.form["num-trans"]
        utils.load_transactions(num)
        
        return render_template("error.html"), 404
            
    return render_template("error.html"), 404
        
if __name__ == '__main__':
    #db.create_all()
    app.run(debug=True)
