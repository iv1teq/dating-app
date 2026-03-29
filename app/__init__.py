import flask
from .settings import app
from .urls import *


app.register_blueprint(blueprint = main_page)
app.register_blueprint(blueprint = registration_page)
app.register_blueprint(blueprint = login_page)