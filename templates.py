from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('index.html', content = "interviews", loop= ["python", "Flask", "HTML","CSS","DSA", "DE", "ML", "AI", "DS", "SQL", "NoSQL"])

if __name__ == '__main__':
  app.run(debug=True, port=5001)