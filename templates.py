from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('base'))

@app.route('/about')
def base():
    return render_template('about.html')

if __name__ == '__main__':
   app.run(debug=True)