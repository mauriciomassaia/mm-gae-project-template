import os
import webapp2
from webapp2_extras import jinja2
from controllers import mainh


config = {
    'webapp2_extras.jinja2': {
        'template_path': [os.environ['TEMPLATES_PATH']]
    }
}


# class BaseHandler(webapp2.RequestHandler):

#     def dispatch(self):
#         self.view_data = {}
#         try:
#             # Dispatch the request.
#             webapp2.RequestHandler.dispatch(self)
#         finally:
#             # Save all sessions.
#             pass
#             # self.session_store.save_sessions(self.response)

#     @webapp2.cached_property
#     def jinja2(self):
#         # Returns a Jinja2 renderer cached in the app registry.
#         return jinja2.get_jinja2(app=self.app)

#     def render(self, view_file):
#         r = self.jinja2.render_template(view_file, **self.view_data)
#         self.response.out.write(r)

# class MainHandler(BaseHandler):
#     def get(self):
#         self.view_data['message'] = 'Hello Mate!'
#         self.render('index.html')


app = webapp2.WSGIApplication([
    ('/', mainh.MainHandler)
], debug=True, config=config)


def main():
    app.run()

if __name__ == '__main__':
    main()
