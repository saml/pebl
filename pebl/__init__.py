import yaml


class YamlFrontMatterParser(object):
	def __init__(self, file_like):
		self.file_like = file_like
		self.curr_state = self.Start
		self.yaml_lines = []
		self.body_lines = []
		for line in file_like:
			self.curr_state(line)
		self.yaml = yaml.safe_load(''.join(self.yaml_lines)) or {}
		self.body = ''.join(self.body_lines)
		

	def Start(self, line):
		if line == '---\n':
			self.curr_state = self.YamlState
		elif line != '\n':
			self.curr_state = self.BodyState

	def YamlState(self, line):
		if line == '---\n':
			self.curr_state = self.BodyState
		else:
			self.yaml_lines.append(line)

	def BodyState(self, line):
		self.body_lines.append(line)

class Content_(object):
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

