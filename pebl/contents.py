import os

from storage import YamlFrontMatterParser
import models

import misaka

def markdown_to_html(s):
    return misaka.html(s)

BODY_PROCESSORS = {
    '.md': misaka.html,
    '.html': lambda x: x
}

SUPPORTED_EXTENSIONS = ['.md', '.html']


class ContentApi(object):
    def __init__(self, page_storage):
        self.page_storage = page_storage

    def get_page(self, page_id):
        for ext in SUPPORTED_EXTENSIONS:
            page_path = os.path.join(self.page_storage, page_id+ext)
            print(page_path)
            if os.path.exists(page_path):
                with open(page_path, 'r') as page_file:
                    data = YamlFrontMatterParser(page_file)
                    title = data.head['title']
                    date = data.head['date']
                    body_processor = BODY_PROCESSORS[ext]
                    body = body_processor(data.body)
                    return models.Page(title, date, body)

