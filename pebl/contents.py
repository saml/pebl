import os

from storage import YamlFrontMatterParser
import models

import misaka

class ContentApi(object):
    def __init__(self, page_storage):
        self.page_storage = page_storage

    def get_page(self, page_id):
        markdown_path = os.path.join(self.page_storage, page_id+'.pebl.md')
        if os.path.exists(markdown_path):
            with open(markdown_path, 'r') as markdown_file:
                parsed = YamlFrontMatterParser(markdown_file)
                return models.Page(parsed.yaml['title'], parsed.yaml['date'], misaka.html(parsed.body))
        
        html_path = os.path.join(self.page_storage, page_id+'.pebl.html')
        if os.path.exists(html_path):
            with open(html_path, 'r') as html_file:
                parsed = YamlFrontMatterParser(html_file)
                return models.Page(parsed.yaml['title'], parsed.yaml['date'], parsed.body)

        return None

