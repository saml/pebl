
class Content(object):
	def __init__(self, path, ext='.html', title='', content=None, prefix='/content/',
		last_modified=None, created=None):
		self.path = path
		self.title = title
		self.ext = ext
		self.content = content
		self.prefix = prefix

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

