
import tempfile
import os
import shutil

import pytest
from flask import url_for

from pebl import app

@pytest.fixture(scope='module')
def storage_path(request):
    temp_dir = tempfile.mkdtemp(prefix='pebl-test-')
    app.config['PAGE_STORAGE'] = temp_dir
    
    def teardown():
        shutil.rmtree(temp_dir)
    request.addfinalizer(teardown)

    return temp_dir

@pytest.fixture(scope='module')
def flask_client():
    client = app.test_client()
    #def teardown():
    #    client.__exit__(None, None, None)
    #request.addfinalizer(teardown)
    return client

@pytest.fixture(scope='module')
def flask_context():
    context = app.test_request_context()
    context.__enter__()
    def teardown():
        context.__exit__(None, None, None)
    return context




def test_existing_page(storage_path, flask_client, flask_context):
    existing_page = os.path.join(storage_path, 'existing/page.pebl.md')
    os.makedirs(os.path.join(storage_path, 'existing'))

    resp = flask_client.get(url_for('page_render', page_id='existing/page'))
    assert resp.status_code == 200

