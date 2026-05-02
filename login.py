from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta


app = Flask(__name__)
#insted of calling every user , I can call the user globally in method by using session and use it all over
app.secret_key = 'Mounika'
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route('/')
def home():
    return "Welcome to home page!"

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
       session.permanent = True
       username = request.form.get('username')
       session['user'] = username
       return redirect(url_for('user'))
    else:
        if  "user" in session:
            return redirect(url_for) 
    return render_template('login.html')

@app.route('/user')
def user():
    if 'user' in session:
        user = session['user']
        return f"welcome to the page {user}!"
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    # flash('You have been logedout!', 'info')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
