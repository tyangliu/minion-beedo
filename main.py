import sys, os, configparser
from tornado.ioloop import IOLoop
from tornado.web import Application, url
from handlers.MainHandler import MainHandler
from handlers.BuildHandler import BuildHandler


def get_server_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['tornado.server']


def make_app():
    return Application([
        url(r"/", MainHandler),
        url(r"/build", BuildHandler)
    ])


def main():
    config = get_server_config()
    app = make_app()
    app.listen(config['port'])
    print('running')
    IOLoop.instance().start()


if __name__ == "__main__":
    main()
