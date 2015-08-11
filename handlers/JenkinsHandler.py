import tornado
from tornado.web import RequestHandler


class JenkinsHandler(RequestHandler):

    def initialize(self, state, minion_io):
        self.state = state
        self.minion_io = minion_io

    def get(self):
        self.write('Beedo Beedo Beedo')

    def post(self):
        data = tornado.escape.json_decode(self.request.body)

        branch = data['build']['parameters']['BRANCH']
        status = data['build']['status']

        print(status, branch, self.state['last_status'])

        if branch == 'default':
            if status == 'FAILURE':
                self.minion_io.signal_alarm()
            elif status == 'SUCCESS' and self.state['last_status'] == 'FAILURE':
                self.minion_io.signal_speech()

        self.state['last_status'] = status
        self.write('Hey')
