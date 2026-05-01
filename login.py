
from curses import flash

from flask import Flask, render_template, redirect, url_for, request, session

from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'Mounika'
app.permanent_session_lifetime = timedelta(minutes=1) 

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        session['user'] = username 
        if username == 'admin' and password == 'password':
            return render_template('courses.html', username=username)
        else:
            if 'user' in session:
                return redirect(url_for('user'))
    return render_template('login.html')    

@app.route('/user')       
def user():
    username = session['user']
    return f"you loged in as {username}."

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('you have been loged out ')
    return redirect(url_for('login'))

if __name__ =='__main__':
    app.run(debug=True, port=5001)