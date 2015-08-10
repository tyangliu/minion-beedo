import configparser
import asyncio
import time
import RPi.GPIO as GPIO


class MinionIO:

    def __init__(self):
        config = MinionIO.get_config()
        self.config_gpio(config)
        self.out_alarm = config['out_alarm']
        self.out_speech = config['out_speech']
        self.in_button_a = config['in_button_a']
        self.in_button_b = config['in_button_b']

    def signal_alarm(self):
        self.signal(self.out_alarm)

    def signal_speech(self):
        self.signal(self.out_speech)

    @staticmethod
    def get_config():
        config = configparser.ConfigParser()
        config.read('config.ini')
        return config['rpi.gpio']

    @staticmethod
    def config_gpio(config):
        mode = config['mode']
        GPIO.setmode(GPIO.BOARD if mode == 'board' else GPIO.BCM)

        GPIO.setup(config['out_alarm'], GPIO.OUT)
        GPIO.setup(config['out_speech'], GPIO.OUT)

        GPIO.setup(config['in_button_a'], GPIO.IN)
        GPIO.setup(config['in_button_b'], GPIO.IN)

    @staticmethod
    def signal(pin):
        GPIO.output(pin, True)
        time.sleep(0.1)
        GPIO.output(pin, False)

