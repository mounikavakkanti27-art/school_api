from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'Mounika'
app.permanent_session_lifetime = timedelta(minutes=5)


@app.route('/')
def home():
    return "Welcome to home page!"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')

        # ✅ correct validation
        if not username:
            flash("Username is required!", "error")
            return redirect(url_for('login'))

        session.permanent = True
        session['user'] = username

        flash("Logged in successfully!", "success")
        return redirect(url_for('user'))

    return render_template('login.html')


@app.route('/user')
def user():
    if 'user' in session:
        return render_template('user.html', user=session['user'])

    flash("Please login first!", "error")
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('user', None)
    flash("You have been logged out successfully!", "info")
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)