from tornado.web import RequestHandler
from tornado.gen import coroutine


class IndexHandler(RequestHandler):
  @property
  def db(self):
    return self.settings["db"]

  @coroutine
  def get(self):
    result = yield self.db.test2.find_one()
    print result
    self.render("shouye/index.html")
