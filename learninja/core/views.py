# home page, learn more, contact us
from flask import render_template, request, Blueprint

core = Blueprint('core', __name__)


@core.route('/')
def index():
    return render_template('index.html')


@core.route('/learn-more')
def learn_more():
    return render_template('learn-more.html')


@core.route('/hosting')
def hosting():
    return render_template('hosting-template.html')


@core.route('/index2')
def index2():
    return render_template('index2.html')