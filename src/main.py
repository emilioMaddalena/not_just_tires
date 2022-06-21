'''
This will become a nice website in the future!
'''

from crypt import methods
import json

from flask import Flask, jsonify, flash, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

import pymysql
import uuid

from my_secrets import DB_ENDPOINT, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME, FLASK_APP_KEY, DB_FULL_URL
import utils

STATE = 'DEBUG'
DATA_PATH = './data/test-data.json'

app = Flask(__name__)
app.secret_key = FLASK_APP_KEY

app.config['SQLALCHEMY_DATABASE_URI'] = DB_FULL_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Transacoes(db.Model): # has to match the DB table you're targeting
    
    __tablename__ = 'transacoes'
    comprador = db.Column("comprador", db.String(100))
    tipo_transacao = db.Column("tipo_trasacao", db.String(100))
    tipo_pneu = db.Column("tipo_pneu", db.String(100))
    quantidade = db.Column("quantidade", db.Integer)
    preco_unitario = db.Column("preco_unitario", db.Float)
    data = db.Column("data", db.Date)
    observacoes = db.Column("observacoes", db.String(100))
    id = db.Column("id", db.String(100), primary_key=True)
    
    def __init__(self, attributes_dict):
        for key in attributes_dict:
            setattr(self, key, attributes_dict[key])
        
##################################################################
# These are the actual web app pages
##################################################################

@app.errorhandler(404)
def page_not_found(e):
    
    return render_template("error.html"), 404

@app.route('/', methods=["GET", "POST"])
def index():
    
    if request.method == "GET":
        my_msg = "We greet the user to our beautiful web page."
        return render_template("index.html", message=my_msg)

    else: return render_template("error.html"), 404

@app.route("/form", methods=["GET", "POST"])
def form(id=None):
    
    if request.method == "GET": 
        
        return render_template("form.html")
    
    elif request.method == "POST":
        
        utils.print_deb(f"{request.form}", STATE)
        
        if not utils.check_mandatory_fields(request.form): 
            
            utils.print_deb('Fill all mandatory fields before submitting!', STATE)
         
        else:
            
            utils.print_deb('You\'ve successfully submitted your data!', STATE)
            utils.store_in_json(DATA_PATH, request.form)
            
            def store_in_db(db, data):
                
                data = data.to_dict()
                id = data['id']
                if not id: data['id'] = str(uuid.uuid4())

                transacao = Transacoes(data)
                db.session.add(transacao)
                
                try: db.session.commit() 
                except: db.session.rollback()
                finally: db.session.close()
            
            store_in_db(db, request.form)
            
    return render_template("form.html")

@app.route("/history", methods=["GET", "POST"])
def history():
    
    if request.method == "GET": 
        
        return render_template("history.html", data="")
    
    elif request.method == "POST":
        
        num = int(request.form["num-trans"])
        trasacs = utils.load_transactions(DATA_PATH, num)
        
        return render_template("history.html", data=trasacs)
            
    else: 
        
        return render_template("error.html"), 404

##################################################################
# These are HTTP access points not associated with a specific page
##################################################################

@app.route("/del-trans", methods=["POST"])
def transac_delete():
    
    if request.method == "POST":
        
        del_id = request.data.decode("utf-8") 
        utils.delete_transaction(DATA_PATH, del_id)
        
        return "All good!"
            
    else: 
        
        return render_template("error.html"), 404

@app.route("/update-trans", methods=["POST"])
def transac_update():
    
    if request.method == "POST":
        
        update_id = request.data.decode("utf-8") 
        # data = ...
        utils.delete_transaction(DATA_PATH, update_id)
        
        return "All good!"
            
    else: 
        
        return render_template("error.html"), 404

#####################
# Initialization
#####################

if __name__ == '__main__':
    
    print("Hello there!")
    db.create_all()
    app.run(debug=False, use_reloader=False)
    
# #! To be deleted
# transacao = Transacoes(
#     id = 'idk1',
#     comprador="Renato Maddalena",
#     quantidade=11
# )
# db.session.add(transacao)
#try: db.session.commit() # if there's a problem
#except: db.session.rollback()
#finally: db.session.close()

# how to retrieve an entry and modify a field
# row = Transacoes.query.filter_by(id='idk2').first()
# print(row)
# row.quantidade = 12
# db.session.commit()