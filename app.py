# coding=utf-8
import sys, os
reload(sys)
sys.setdefaultencoding("utf8")

from tornado.web import Application, StaticFileHandler
from tornado.ioloop import IOLoop

sys.path.append(os.path.join(os.path.dirname(__file__), "py"))#把py加入系统路径
from index import IndexHandler


def main():
  settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "dist/apps"),#静态资源路径
    "template_path": os.path.join(os.path.dirname(__file__), "dist/apps"),#render的路径
    "debug": True
  }
  handlers = [(r"/", IndexHandler),
              (r"/dist/apps/(.*)", StaticFileHandler, {"path": settings["static_path"]})]
  app = Application(handlers, **settings)
  app.listen(8888)
  IOLoop.current().start()


if __name__ == "__main__":
  print "app run at %s" % 8888
  main()
