import configparser
import RPi.GPIO as GPIO
from tornado import gen


class MinionIO:

    def __init__(self):
        config = self.get_config()
        self.config_gpio(config)
        self.out_alarm = int(config['out_alarm'])
        self.out_speech = int(config['out_speech'])
        self.in_button_a = int(config['in_button_a'])
        self.in_button_b = int(config['in_button_b'])

    def signal_alarm(self):
        self.signal(self.out_alarm)

    def signal_speech(self):
        self.signal(self.out_speech)

    def config_gpio(self, config):
        mode = config['mode']
        GPIO.setmode(GPIO.BOARD if mode == 'board' else GPIO.BCM)

        out_channels = (int(config['out_alarm']), int(config['out_speech']))
        in_channels = (int(config['in_button_a']), int(config['in_button_b']))

        GPIO.setup(out_channels, GPIO.OUT)
        GPIO.setup(in_channels, GPIO.IN)

        GPIO.add_event_detect(in_channels[0], GPIO.RISING, callback=self.input_cb, bouncetime=200)
        GPIO.add_event_detect(in_channels[1], GPIO.RISING, callback=self.input_cb, bouncetime=200)

    def input_cb(self, channel):
        print('input received', channel)
        if channel == self.in_button_a:
            self.signal(self.out_alarm)
        elif channel == self.in_button_b:
            self.signal(self.out_speech)

    @staticmethod
    @gen.coroutine
    def signal(channel):
        GPIO.output(channel, True)
        yield gen.sleep(0.1)
        GPIO.output(channel, False)

    @staticmethod
    def get_config():
        config = configparser.ConfigParser()
        config.read('config.ini')
        return config['rpi.gpio']
