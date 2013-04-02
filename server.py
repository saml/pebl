import bottle
import misaka

import os

import settings
from pebl import YamlFrontMatterParser

bottle.debug(settings.DEBUG)

def render_template(name, **kwargs):
    return bottle.template(name, 
            template_lookup=settings.TEMPLATE_DIRS, 
            CDN_URL=settings.CDN_URL,
            **kwargs)

@bottle.route('/admin/<path:path>')
def index(path):
    return render_template('creator.html')

@bottle.route('/posts/<path:path>')
def blog_entry(path):
	entry_id,ext = os.path.splitext(path)
	content_path = os.path.join(settings.CONTENT_DIR, entry_id)
	content_path_html = content_path + '.html'
	content_path_markdown = content_path + '.md'
	if os.path.exists(content_path_html):
		with open(content_path_html, 'r') as f:
			yaml_front_matter = YamlFrontMatterParser(f)
			return render_template('blog_entry.html', 
				metadata=yaml_front_matter.yaml, body=yaml_front_matter.body)
	elif os.path.exists(content_path_markdown):
		with open(content_path_markdown, 'r') as f:
			yaml_front_matter = YamlFrontMatterParser(f)
			return render_template('blog_entry.html',
				metadata=yaml_front_matter.yaml, body=misaka.html(yaml_front_matter.body))
	else:
		bottle.abort(404, 'Not Found')


if __name__ == '__main__':
    bottle.run(host=settings.HOST, port=settings.PORT, reloader=settings.DEBUG)
