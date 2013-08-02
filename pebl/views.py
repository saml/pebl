from flask import request

from pebl import app, PAGE_STORAGE

import os

@app.route('/admin/pages/<path:page_id>.html')
def page_render(page_id):
    return PAGE_STORAGE
    #os.path.join(PAGE_STORAGE, page_id+
