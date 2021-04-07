from flask import Flask, render_template, make_response, request
import os

app = Flask(__name__, static_folder=os.path.abspath('static'))


@app.route('/')
def index():
    id = 0
    resp = request.cookies.get('id')
    site = make_response(render_template('index.html'))
    if not resp:
        site.set_cookie('username', byte(id))
        id = id + 1
        print('gave you the id: %s' %(id))
    return site

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
    app.run(debug=True, port=80)
