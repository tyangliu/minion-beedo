from tornado.web import RequestHandler
from gpio.TestMinionIO import TestMinionIO


class BuildHandler(RequestHandler):

    def get(self):
        self.write('Beedo Beedo Beedo')

    def post(self):
        status = self.get_argument('status')
        minion_io = TestMinionIO()

        if status == 'broken':
            minion_io.signal_alarm()
            self.write('Broken received')
        elif status == 'restored':
            minion_io.signal_speech()
            self.write('Restored received')

