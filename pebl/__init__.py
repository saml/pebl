import flask

import contents

app = flask.Flask(__name__)
app.config.from_object('pebl.settings')

PAGE_STORAGE = app.config['PAGE_STORAGE']

content_api = contents.ContentApi(PAGE_STORAGE)

import views

