
from flask import Flask, flash, render_template, session, url_for, redirect, request
from models import User, Category, Recipe
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = 'secret'
bootstrap = Bootstrap(app)
Users = {}


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
            flash('You are now registered go ahead and login')
            return redirect(url_for('showlogin'))
        flash('Account not created try again')
        return redirect(url_for('signup'))
    return render_template('signup.html')


@app.route("/showlogin", methods=['POST', 'GET'])
def showlogin():
    """ Handles the login route """
    if request.method == 'POST':
        result = login(request.form['email_field'],
                       request.form['password_field'])
        if result == "Login successful":
            session['email'] = request.form['email_field']
            flash("logged in successfully, welcome")
            return redirect(url_for('category'))
        flash("wrong credentials try again")
    return render_template('login.html')


@app.route('/category', methods=['POST', 'GET'])
def category():

    return render_template('dashboard.html', categories=Users[session['email']].categories)


@app.route('/add_category', methods=['GET', 'POST'])
def add_category():
    if request.method == 'POST':
        return_value = Users[session['email']
                             ].add_category(request.form['title'])
        if return_value == True:
            flash("category added successful")
            return redirect(url_for('category'))
        flash("category not added")
    return render_template('dashboard.html', categories=Users[session['email']].categories)


@app.route('/delete_category/<title>', methods=['POST', 'GET'])
def delete_category(title):
    result = Users[session['email']].delete_category(title)
    if result == True:
        flash("delete successful")
    else:
        flash("cant delete its empty")
    return redirect(url_for('category'))


@app.route('/edit_category/<title>', methods=['POST', 'GET'])
def edit_category(title):
    session['category_title'] = title
    if request.method == 'POST':
        return_value = Users[session['email']].edit_category(
            session['category_title'], request.form['title'])
        if return_value == True:
            flash("edited category successfully")
            return redirect(url_for('category'))
        flash("error! please put a category")
    return render_template('editcategory.html')


@app.route('/show_recipe/<category_title>', methods=['GET', 'POST'])
def show_recipe(category_title):
    """ Handles displaying recipes """
    session['current_category_title'] = category_title
    return render_template('viewrecipe.html', recipes=Users[session['email']]
                           .categories[category_title].recipes)


@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    """ Handles new addition of recipes requests """
    if request.method == 'POST':
        result = Users[session['email']].categories[session['current_category_title']].add_recipe(
            request.form['name'], request.form['contents'], request.form['instructions'])
        if result == True:
            flash("recipe added successfully")
        else:
            flash("Not added")
        return redirect(url_for('show_recipe', category_title=session['current_category_title']))
    return render_template('addrecipe.html', recipes=Users[session['email']]
                           .categories[session['current_category_title']].recipes)


@app.route('/delete_recipe/<name>', methods=['GET', 'POST'])
def delete_recipe(name):
    """ Handles request to delete a recipe """
    result = Users[session['email']].categories[session['current_category_title']].delete_recipe(
        name)
    if result == True:
        flash("recipe deleted")
    else:
        flash("not deleted")
    return redirect(url_for('show_recipe', category_title=session['current_category_title']))


@app.route('/update_recipe/<name>', methods=['GET', 'POST'])
def update_recipe(name):
    """ Handles request to update a recipe """
    session['name'] = name
    if request.method == 'POST':
        result1 = (Users[session['email']].categories[session['current_category_title']].
                   edit_recipe(session['name'], request.form['name']))
        if result1 == True:
            flash("update successfully")
        else:
            flash("not succeeded")
        return redirect(url_for('show_recipe', category_title=session['current_category_title']))
    return render_template('updaterecipe.html', recipe=Users[session['email']]
                           .categories[session['current_category_title']].recipes[name],
                           recipes=Users[session['email']].
                           categories[session['current_category_title']].recipes)


@app.route('/logout')
def logout():
    """ logs out users """
    session.pop('email')
    flash('You have logged out thanks')
    return redirect(url_for('main'))


if __name__ == "__main__":
    app.run(debug=True)
