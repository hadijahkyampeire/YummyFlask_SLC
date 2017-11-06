
from flask import Flask, flash, render_template, session, url_for, redirect, request
from models import User

app = Flask(__name__)
app.secret_key = 'secret'
Users = {}
categories = {}


def register(firstname, lastname, email, password):
    """ This function handles user registration"""
    if firstname and lastname and email and password:
        Users[email] = User(firstname, lastname, email, password)
        return "Registration successful"
    return "None input"


def login(email, password):
    """ Handles user login """
    if email and password:
        if Users.get(email):
            if Users[email].password == password:
                return "Login successful"
            return "Wrong password"
        return "User not found"
    return "None input"


@app.route("/")
def main():
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """ Handles the sign_up route """
    if request.method == 'POST':
        # creating an instance of the register fuction
        returnvalue = register(request.form['firstname_field'], request.form['lastname_field'],
                               request.form['email_field'], request.form['password_field'])
        if returnvalue == "Registration successful":
            flash(returnvalue, 'info')
            return redirect(url_for('showlogin'))
        flash(returnvalue, 'warning')
    return render_template('signup.html')


@app.route("/showlogin", methods=['POST', 'GET'])
def showlogin():
    """ Handles the login route """
    if request.method == 'POST':
        result = login(request.form['email_field'],
                       request.form['password_field'])
        if result == "Login successful":
            session['email'] = request.form['email_field']
            return redirect(url_for('category'))
        flash(result, 'warning')
    return render_template('login.html')


@app.route('/category')
def category():
    return render_template('dashboard.html')


@app.route('/add_category', methods=['GET', 'POST'])
def add_category():
    if request.method == 'POST':
        title = request.form['title']
        if title:
            categories['title'] = title

        return redirect(url_for('list'))
    return render_template('add category.html')
@app.route("/list")
def list():
    return render_template('view.html',  title=categories['title'])

# @app.route('/addcategory', methods=['GET', 'POST'])
# def addcategory():
#     if request.method == 'POST':
#         returnvalue = User.add_category('title')
#         if returnvalue == True:
#                return redirect(url_for('recipes'))
#                flash("category added")
#     if request.method=='GET':
#           return render_template('add recipe.html')
    # title = request.form['title']
    # item1 = request.form['item1']
    # item2 = request.form['item2']
    # item3 = request.form['item3']
    # item4 = request.form['item4']
    # if title and item1:
    #     Recipes['title']=title
    #     Recipes['item1']=item1
    #     Recipes['item2']=item2
    #     Recipes['item3']=item3
    #     Recipes['item4']=item4


# @app.route("/recipes")
# def recipes():
#     return render_template('view.html')
#  title=Recipes['title'] )
    # item1=Recipes['item1'], item2=Recipes['item2'],
    #     item3=Recipes['item3'], item4=Recipes['item4'])
if __name__ == "__main__":
    app.run(debug=True)
