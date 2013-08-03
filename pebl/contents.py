import os

from storage import YamlFrontMatterParser
import models

import misaka

markdown_extensions = (
    misaka.EXT_NO_INTRA_EMPHASIS | 
    misaka.EXT_AUTOLINK |
    misaka.EXT_TABLES |
    misaka.EXT_FENCED_CODE |
    misaka.EXT_LAX_HTML_BLOCKS |
    misaka.EXT_SPACE_HEADERS |
    misaka.EXT_SUPERSCRIPT
)
markdown_flags = (
    misaka.HTML_TOC
)

def markdown_to_html(s):
    return misaka.html(s, extensions=markdown_extensions, render_flags=markdown_flags)

BODY_PROCESSORS = {
    '.md': markdown_to_html,
    '.html': lambda x: x
}

SUPPORTED_EXTENSIONS = ['.md', '.html']


class ContentApi(object):
    def __init__(self, page_storage, draft_storage):
        self.page_storage = page_storage
        self.draft_storage = draft_storage

    def get_page(self, page_id, check_drafts=False):
        base_paths = []
        if check_drafts:
            base_paths.append(self.draft_storage)
        base_paths.append(self.page_storage)

        for storage_path in base_paths:
            for ext in SUPPORTED_EXTENSIONS:
                page_path = os.path.join(storage_path, page_id+ext)
                if os.path.exists(page_path):
                    with open(page_path, 'r') as page_file:
                        data = YamlFrontMatterParser(page_file)
                        title = data.head['title']
                        date = data.head['date']
                        body_processor = BODY_PROCESSORS[ext]
                        body = body_processor(data.body)
                        return models.Page(title, date, body)

