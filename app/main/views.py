from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_News,get_News,search_news
from ..models import Review
# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to the best news website online'
    return render_template('index.html',title = title)

# Views
@main.route('/news/<int:news_id>')
def news(news_id):

    '''
    View root page function that returns the index page and its data
    '''
    message = 'Hello world'
    return render_template('news.html',message = message)