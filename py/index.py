from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
  def get(self):
    self.write("hello")
    self.render("shouye/index.html")
