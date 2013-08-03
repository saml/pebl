
import tempfile
import os
import shutil

import pytest
from flask import url_for

from pebl import app

@pytest.fixture(scope='module')
def storage_path(request):
    temp_dir = tempfile.mkdtemp(prefix='pebl-test-')
    
    def teardown():
        shutil.rmtree(temp_dir)
    request.addfinalizer(teardown)

    return temp_dir

#@pytest.fixture(scope='module')
#def flask_client(storage_path):
#    client = app.test_client()
#    #def teardown():
#    #    client.__exit__(None, None, None)
#    #request.addfinalizer(teardown)
#    return client

#@pytest.fixture(scope='module')
#def flask_context():
#    context = app.test_request_context()
#    context.__enter__()
#    def teardown():
#        context.__exit__(None, None, None)
#    return context




def test_existing_page(storage_path):
    existing_page = os.path.join(storage_path, 'existing/page.pebl.md')
    os.makedirs(os.path.join(storage_path, 'existing'))
    with open(existing_page, 'w') as f:
        f.write('''---
title: Existing Page
date: 2013-12-30 00:01:50
---
# Hello

World
''')

    app.config['PAGE_STORAGE'] = storage_path
    flask_client = app.test_client()
    with app.test_request_context():
        page_url = url_for('page_render', page_id='existing/page')
        resp = flask_client.get(page_url)
        assert(resp.status_code == 200)
        assert(resp.data.find('<title>Existing Page') > 0)

