from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

from Django_tornado_server.wsgi import application

CERT_CRT_PATH = './server.crt'
CERT_KEY_PATH = './server.key'

http_server = HTTPServer(WSGIContainer(application), ssl_options={
       "certfile": CERT_CRT_PATH,
       "keyfile": CERT_KEY_PATH,
})
print("Django version 2.2.1, using settings 'Django_tornado_server.settings'")
print('Starting development server at https://127.0.0.1:8000/')
http_server.listen(8000)  # Django默认的端口
IOLoop.instance().start()
