from flask import Flask, render_template
import os

app = Flask(__name__, static_folder=os.path.abspath('static'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rev')
def news():
    return render_template('review.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)
