import flask

import contents

app = flask.Flask(__name__)
app.config.from_object('pebl.settings')

PAGE_STORAGE = app.config['PAGE_STORAGE']
PAGE_DRAFT_STORAGE = app.config['PAGE_DRAFT_STORAGE']

content_api = contents.ContentApi(PAGE_STORAGE, PAGE_DRAFT_STORAGE)

import views

