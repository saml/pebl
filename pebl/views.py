from flask import request, render_template, abort

from pebl import app
from pebl import content_api

@app.route('/admin/pages/<path:page_id>.html')
def page_render(page_id):
    page = content_api.get_page(page_id)
    if page is None:
        abort(404)
    return render_template('page.html', page=page)
