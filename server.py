import bottle
import misaka

import settings


bottle.debug(settings.DEBUG)

def render_template(name, **kwargs):
    return bottle.template(name, 
            template_lookup=settings.TEMPLATE_DIRS, 
            CDN_URL=settings.CDN_URL,
            **kwargs)

@bottle.route('/admin')
def index():
    return render_template('creator.html')


if __name__ == '__main__':
    bottle.run(host=settings.HOST, port=settings.PORT, reloader=settings.DEBUG)
