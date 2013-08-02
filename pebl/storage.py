import yaml

import os
import re
import datetime

NON_WORD_RE = re.compile(r'[_\W]')
YYYY_MM_RE = re.compile(r'^.*/(\d\d\d\d/\d\d)/.*$')

class YamlFrontMatterParser(object):
    def __init__(self, file_like):
        self._curr_state = self._Start
        self._yaml_lines = []
        while True:
            line = file_like.readline()
            if not line:
                break
            if not self._curr_state(line):
                break

        self.yaml = yaml.safe_load(''.join(self._yaml_lines)) or {}
        self.body = file_like.read()
        

    def _Start(self, line):
        if line == '---\n':
            self._curr_state = self._YamlState
        elif line != '\n':
            self._curr_state = self._BodyState
        return True

    def _YamlState(self, line):
        if line == '---\n':
            return False
            #self._curr_state = self._BodyState
        else:
            self._yaml_lines.append(line)
        return True


def upsert_entry(yaml_front_matter):
    pass


def title_from_path(path):
    '''
    >>> title_from_path('/posts/2012/02/01-nice-way-of_flying')
    '01 Nice Way Of Flying'
    '''
    basename = os.path.basename(path)
    return NON_WORD_RE.sub(' ', basename).title()

def pub_date_from_path(path):
    '''
    >>> pub_date_from_path('/posts/2012/12/hola')
    datetime.datetime(2012, 12, 1, 0, 0)
    '''
    m = YYYY_MM_RE.match(path)
    if m:
        return datetime.datetime.strptime(m.group(1), '%Y/%m')
    return datetime.datetime.fromtimestamp(os.path.getctime(path))



class Content(object):
    def __init__(self, path, body, metadata={}):
        self.path = path
        self.body = body
        self.metadata = metadata
        self.title = metadata.get('title', title_from_path(path))
        self.pub_date = metadata.get('pub_date', pub_date_from_path(path))

class NoopPersistence(object):
    def upsert(self, content):
        pass

    def remove(self, content):
        pass

class FileSystemPersistence(NoopPersistence):
    def __init__(self, content_dir, asset_dir, publish_dir, work_dir):
        self.content_dir = content_dir
        self.asset_dir = asset_dir
        self.publish_dir = publish_dir
        self.work_dir = work_dir

    def upsert(self, content):
        pass

