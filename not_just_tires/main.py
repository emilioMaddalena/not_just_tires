'''
This will become a nice website in the future!
'''

from crypt import methods
from flask import Flask
from flask import render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    my_msg = "We greet the user to our beautiful web page."
    return render_template("index.html", message=my_msg)

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "GET":
        # the user is requesting the form
        return render_template("form.html")
    
    elif request.method == "POST":
        # the user has filled the form and the info is available
        if len(request.form) == 3: 
            print("You've filled the complete thing!")
        else:
            print("Please, complete the whole thing!")
        return render_template("form.html")

if __name__ == '__main__':
    app.run()