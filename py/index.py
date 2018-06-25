# coding=utf-8
from tornado.web import RequestHandler
from tornado.gen import coroutine


class IndexHandler(RequestHandler):
  def options(self, *args, **kwargs):
    self.set_header("Access-Control-Allow-OriGIN","*")
    self.set_header("Access-Control-Allow-headers","H")
    self.set_header("Access-Control-max-Age",100)
  @property
  def db(self):
    return self.settings["db"]

  @coroutine
  def get(self):
    self.set_header("Access-Control-Allow-OriGIN", "*")
    result = yield self.db.test2.find_one()
    print result
    self.render("shouye/index.html")


class CorsHandler(RequestHandler):
  def get(self, *args, **kwargs):
    print "get header", self.request.headers
    h = self.request.headers.get("Origin")
    self.set_header("Access-Control-Allow-Origin", h if h else "")
    self.set_header("Access-Control-Allow-Credentials", 'true')
    print "get cookie", repr(self.request.cookies)

    a = self.get_query_argument("test")
    print "get", repr(a)
    # 第一种方式
    # import requests
    # r=requests.post("http://localhost:8887/cors?test",headers=self.request.headers,cookies={'ggg':'8777'})
    # print r.content
    # 第二种方式
    # import tornado.httpclient
    # cli=tornado.httpclient.HTTPClient()
    # cli.fetch("http://localhost:8887/cors?test",headers=self.request.headers)
    # 第三种方式
    def cal(r):
      print "now is call back"
    import tornado.httpclient
    cli = tornado.httpclient.AsyncHTTPClient()
    r=cli.fetch("http://localhost:8887/cors?test",headers=self.request.headers,callback=cal,method="post")
    print "last is ended",r


  def post(self, *args, **kwargs):
    print "post json", repr(self.request.body)
    a = self.get_body_argument("testp", "")
    import requests
    requests.post("http://localhost:8887/cors?test",data=self.request.body,headers=self.request.headers)
    print "post", repr(a)


class Cors2Handler(RequestHandler):
  def get(self, *args, **kwargs):
    print "get header", self.request.headers
    h = self.request.headers.get("Origin")
    self.set_header("Access-Control-Allow-Origin", h if h else "")
    self.set_header("Access-Control-Allow-Credentials", 'true')
    print "get cookie2", repr(self.request.cookies)

    a = self.get_query_argument("test")
    print "get", repr(a)

  def post(self, *args, **kwargs):
    print "post json2", repr(self.request.body)
    print "get header", self.request.headers
    h = self.request.headers.get("Origin")
    self.set_header("Access-Control-Allow-Origin", h if h else "")
    self.set_header("Access-Control-Allow-Credentials", 'true')
    print "get cookie2", repr(self.request.cookies)

    a = self.get_body_argument("test", "")
    print "post", repr(a)
