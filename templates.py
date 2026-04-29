from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/') #http://127.0.0.1:5001/
def home():
    return render_template('home.html')

@app.route("/courses") #http://127.0.0.1:5001/courses
def courses():
    return render_template('about.html', course_list=['Python', 'Flask','DSA','ML', 'AI', 'Data Science'], context='I am learning below courses.')

if __name__ == '__main__':
    app.run(debug=True, port=5001)

 #in this covered render_template - helps to navigate html template
 # redirect - helps to redirect method
 # url_for - helps for the url_for the method. 

 #render_template - has extention to render the inheritance of base.html url.