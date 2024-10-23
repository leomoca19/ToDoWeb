from flask import Blueprint

views = Blueprint('views', __name__)
colors = '<body style="background-color:black;color:green;">'

@views.route('/')
def home():
    return colors + '<h1>Test<h1>'