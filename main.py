import configparser
from tornado.ioloop import IOLoop
from tornado.web import Application, url
from handlers.MainHandler import MainHandler
from handlers.JenkinsHandler import JenkinsHandler
from handlers.BananaHandler import BananaHandler
from gpio.MinionIO import MinionIO


def get_server_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['tornado.server']


def make_app():
    build_state = {'last_status': ''}
    minion_io = MinionIO()

    return Application([
        url(r"/", MainHandler),
        url(r"/jenkins", JenkinsHandler, {
            'state': build_state,
            'minion_io': minion_io
        }),
        url(r"/banana", BananaHandler, {
            'minion_io': minion_io
        })
    ])


def main():
    config = get_server_config()
    app = make_app()
    app.listen(config['port'])
    print('running')
    IOLoop.instance().start()


if __name__ == "__main__":
    main()
