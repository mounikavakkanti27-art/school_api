from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/') #http://127.0.0.1:5001/
def home():
    return "<h1>First Flask application</h1>"

@app.route("/courses") #http://127.0.0.1:5001/courses
def courses():
    return "<h1>Courses endpoint.</h1>"

@app.route('/admin') #http://127.0.0.1:5001/admin 
def admin():         #admin will redirect to  coursess url when accessed.
    return redirect(url_for('courses')) #redirects to the courses endpoint when the admin endpoint is accessed.

@app.route('/student/<name>/<course>') #http://127.0.0.1:5001/student/Mounika/Maths
def get_student(name: str, course: str):
    return f"I am {name} and I am studing {course} class."

if __name__ == '__main__':
    app.run(debug=True, port=5001)