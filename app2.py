# coding=utf-8
import sys, os

reload(sys)
sys.setdefaultencoding("utf8")

import motor
from tornado.web import Application, StaticFileHandler
from tornado.ioloop import IOLoop
import setting

sys.path.append(os.path.join(os.path.dirname(__file__), "py"))  # 把py加入系统路径
from index import Cors2Handler


def main():
  settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "dist/apps"),  # 静态资源路径
    "template_path": os.path.join(os.path.dirname(__file__), "dist/apps"),  # render的路径
    "debug": True,
    "db": motor.MotorClient(setting.CMS_MONGO_STRING).test
  }
  handlers = [
    (r"/cors", Cors2Handler),
    (r"/dist/apps/(.*)", StaticFileHandler, {"path": settings["static_path"]})
  ]
  app = Application(handlers, **settings)
  app.listen(8887)
  IOLoop.current().start()


if __name__ == "__main__":
  print "app run at %s" % 8888
  main()
