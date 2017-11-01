from flask import request
from flask import Flask, render_template,url_for,redirect
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
User={}
Recipes={}

@app.route("/")
def main():
    return render_template('index.html')
@app.route("/signup" , methods=['GET','POST'])
def signup():
    if request.method=='POST':

        email = request.form['email_field']
        f_name = request.form['firstname_field']
        l_name = request.form['lastname_field']
        p_word = request.form['password_field']
        
        if email and p_word:
            User[email]= p_word
            return redirect (url_for('showlogin'))
    return render_template('signup.html' )
@app.route('/showlogin', methods=['GET','POST'])
def showlogin():
    error=None
    if request.method=='POST':
        if request.form['email_field'] not in User.keys() or request.form['password_field'] not in User.values():
            error='invalid credentials'
        else:
            return redirect(url_for('addrecipes'))
    return render_template('login.html',error = error)

if __name__=="__main__":
    app.run(debug=True)
    