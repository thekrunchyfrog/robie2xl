import RPi.GPIO as gpio
from random import randint
from time import sleep


class Guts:
    _btnA = 12
    _btnB = 13
    _btnC = 14
    _btnD = 15

    _rightEye = 16
    _leftEye = 17

    _domeRed = 18
    _domeGreen = 19
    _domeBlue = 20
    _freq = 100

    def __init__(self):
        gpio.setmode(gpio.BOARD)
        gpio.setwarnings(False)

        gpio.setup(self._btnA, gpio.IN)
        gpio.setup(self._btnB, gpio.IN)
        gpio.setup(self._btnC, gpio.IN)
        gpio.setup(self._btnD, gpio.IN)

        gpio.setup(self._rightEye, gpio.OUT)
        gpio.setup(self._leftEye, gpio.OUT)

        gpio.setup(self._domeRed, gpio.OUT)
        gpio.setup(self._domeGreen, gpio.OUT)
        gpio.setup(self._domeBlue, gpio.OUT)

        self.domeRED = (self._domeRed, self._freq)
        self.domeGREEN = (self._domeGreen, self._freq)
        self.domeBLUE = (self._domeBlue, self._freq)

    def eyes_open(self):
        gpio.output(self._rightEye, gpio.HIGH)
        gpio.output(self._leftEye, gpio.HIGH)

    def eyes_close(self):
        gpio.output(self._rightEye, gpio.LOW)
        gpio.output(self._leftEye, gpio.LOW)

    def blink_eyes(self):
        if gpio.input(self._rightEye) == gpio.HIGH:
            self.eyes_close()
            sleep(1)
            self.eyes_open()

    def wink(self):
        self.eyes_open()
        eye = randint(1, 2)
        if eye == 1:
            gpio.output(self._rightEye, gpio.LOW)
        else:
            gpio.output(self._leftEye, gpio.LOW)
        sleep(0.5)
        self.eyes_open()

    def domeOn(self):
        self.domeRED.start(1)
        self.domeGREEN.start(1)
        self.domeBLUE.start(1)

    def domeOff(self):
        self.domeRED.stop()
        self.domeGREEN.stop()
        self.domeBLUE.stop()

    def domeSetColor(self, valRed, valGreen, valBlue):
        self.domeRED.ChangeDutyCyle()
        self.domeGREEN.ChangeDutyCyle()
        self.domeGREEN.ChangeDutyCyle()
