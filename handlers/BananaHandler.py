from tornado.web import RequestHandler


class BananaHandler(RequestHandler):

    def initialize(self, minion_io):
        self.minion_io = minion_io

    def get(self):
        self.write('Beedo Beedo Beedo')

    def post(self):
        signal = self.get_argument('signal', '')
        if signal == 'alarm':
            self.minion_io.signal_alarm()
            self.write('Minion Alarm Activated')
        elif signal == 'speech':
            self.minion_io.signal_speech()
            self.write('Minion Speech Activated')
        else:
            self.write('Signal not supported')
