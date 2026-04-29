from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('index.html', content = "interviews", loop= ["python", "Flask", "HTML","CSS","DSA", "DE", "ML", "AI", "DS", "SQL", "NoSQL"])

@app.route('/sub_selection')
def sub_selection():
    return redirect(url_for('about'))

if __name__ == '__main__':
  app.run(debug=True, port=5001)

 #in this covered render_template - helps to navigate html template
 # redirect - helps to redirect method
 # url_for - helps for the url_for the method. 