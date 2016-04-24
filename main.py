import os.path as os_path

from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from tornado.web import Application, RequestHandler
from tornado.options import define, options, parse_command_line

define("port", default=8888, help="run on the given port", type=int)
define("debug", default=True, help="run in debug mode")

class HttpServerApplication(Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/auth/login", AuthLoginHandler),
            (r"/auth/logout", AuthLogoutHandler),
        ]
        settings = dict(
            blog_title=u"Tornado Hello World",
            template_path=os_path.join(os_path.dirname(__file__), "template"),
            static_path=os_path.join(os_path.dirname(__file__), "static"),
            xsrf_cookies=True,
            cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            login_url="/auth/login",
            debug=options.debug,
        )
        Application.__init__(self, handlers, **settings)


class MainHandler(RequestHandler):
    # @authenticated
    def get(self):
        items = ["Item 1", "Item 2", "Item 3"]
        context = {"title": "My title", "items": items}
        self.render("index.html", **context)

class AuthLoginHandler(RequestHandler):
    def get(self):
        # If there are no authors, redirect to the account creation page.
        # if not self.any_author_exists():
        #     self.redirect("/auth/create")
        # else:
        #     self.render("login.html", error=None)
        pass

    # @gen.coroutine
    def post(self):
        # author = self.db.get("SELECT * FROM authors WHERE email = %s",
        #                      self.get_argument("email"))
        # if not author:
        #     self.render("login.html", error="email not found")
        #     return
        # hashed_password = yield executor.submit(
        #     bcrypt.hashpw, tornado.escape.utf8(self.get_argument("password")),
        #     tornado.escape.utf8(author.hashed_password))
        # if hashed_password == author.hashed_password:
        #     self.set_secure_cookie("blogdemo_user", str(author.id))
        #     self.redirect(self.get_argument("next", "/"))
        # else:
        #     self.render("login.html", error="incorrect password")
        pass


class AuthLogoutHandler(RequestHandler):
    def get(self):
        # self.clear_cookie("blogdemo_user")
        # self.redirect(self.get_argument("next", "/"))
        pass


def main():
    parse_command_line()
    http_server = HTTPServer(HttpServerApplication())
    http_server.listen(options.port)
    IOLoop.current().start()

if __name__ == "__main__":
    main()