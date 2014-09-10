import webapp2
import os
from webapp2_extras import jinja2


class BaseHandler(webapp2.RequestHandler):
    def dispatch(self):
        self.view_data = {}
        try:
            webapp2.RequestHandler.dispatch(self)
        finally:
            pass
            
    @webapp2.cached_property
    def jinja2(self):
        # Returns a Jinja2 renderer cached in the app registry.
        return jinja2.get_jinja2(app=self.app)

    def render(self, view_file):
        r = self.jinja2.render_template(view_file, **self.view_data)
        self.response.out.write(r)


class MainHandler(BaseHandler):
    def get(self):
        self.view_data['message'] = 'Hello Mate!'
        self.render('index.html')
