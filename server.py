from flask import Flask, render_template, make_response, request
import os
from fetchDB import fetchAllData

app = Flask(__name__, static_folder=os.path.abspath('static'))
data = fetchAllData()



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rev')
def news():
    return data[0].headerText + " " + data[0].contentText


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True, port=80)
