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
@app.route('/addrecipes', methods=['GET','POST'])
def addrecipes():
    if request.method=='POST':
        title=request.form['title']
        item1=request.form['item1']
        item2=request.form['item2']
        item3=request.form['item3']
        item4=request.form['item4']
        if title and item1:
            Recipes['title']=title
            Recipes['item1']=item1
            Recipes['item2']=item2
            Recipes['item3']=item3
            Recipes['item4']=item4
            return redirect(url_for('recipes'))
    return render_template('add recipe.html')
@app.route("/recipes")
def recipes():
    return render_template('view.html',  title=Recipes['title'], item1=Recipes['item1'], item2=Recipes['item2'], 
        item3=Recipes['item3'], item4=Recipes['item4'])

if __name__=="__main__":
    app.run(debug=True)
    