from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to the best news website online'
    return render_template('index.html',title = title)

# Views
@app.route('/news/<int:news_id>')
def news(news_id):

    '''
    View root page function that returns the index page and its data
    '''
    message = 'Hello world'
    return render_template('news.html',message = message)