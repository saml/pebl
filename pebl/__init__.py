import flask

app = flask.Flask(__name__)
app.config.from_object('pebl.settings')

PAGE_STORAGE = app.config['PAGE_STORAGE']

import pebl.views

