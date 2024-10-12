import RPi.GPIO as gpio
from math import ceil
from random import randint
from time import sleep


class Guts:
    #_btnA = 12
    #_btnB = 13
    #_btnC = 14
    #_btnD = 15

    _rightEye = 37
    _leftEye = 38

    _domeRed = 8
    _domeGreen = 10
    _domeBlue = 12
    _freq = 50

    def __init__(self):
        gpio.setmode(gpio.BOARD)
        gpio.setwarnings(False)

        #gpio.setup(self._btnA, gpio.IN, pull_up_down=gpio.PUD_DOWN)
        #gpio.setup(self._btnB, gpio.IN, pull_up_down=gpio.PUD_DOWN)
        #gpio.setup(self._btnC, gpio.IN, pull_up_down=gpio.PUD_DOWN)
        #gpio.setup(self._btnD, gpio.IN, pull_up_down=gpio.PUD_DOWN)

        gpio.setup(self._rightEye, gpio.OUT)
        gpio.setup(self._leftEye, gpio.OUT)

        gpio.setup(self._domeRed, gpio.OUT)
        gpio.setup(self._domeGreen, gpio.OUT)
        gpio.setup(self._domeBlue, gpio.OUT)

        self.domeRED = gpio.PWM(self._domeRed, self._freq)
        self.domeGREEN = gpio.PWM(self._domeGreen, self._freq)
        self.domeBLUE = gpio.PWM(self._domeBlue, self._freq)

    def eyes_open(self):
        gpio.output(self._rightEye, gpio.HIGH)
        gpio.output(self._leftEye, gpio.HIGH)

    def eyes_close(self):
        gpio.output(self._rightEye, gpio.LOW)
        gpio.output(self._leftEye, gpio.LOW)

    def blink_eyes(self):
        if gpio.input(self._rightEye) == gpio.HIGH:
            self.eyes_close()
            sleep(0.5)
            self.eyes_open()

    def wink(self):
        self.eyes_open()
        eye = randint(1, 2)
        if eye == 1:
            gpio.output(self._rightEye, gpio.LOW)
        else:
            gpio.output(self._leftEye, gpio.LOW)
        sleep(0.25)
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
        red = self._colorToFreq(valRed)
        green = self._colorToFreq(valGreen)
        blue = self._colorToFreq(valBlue)

        self.domeRED.ChangeDutyCycle(red)
        self.domeGREEN.ChangeDutyCycle(green)
        self.domeBLUE.ChangeDutyCycle(blue)

    def cleanup(self):
        gpio.cleanup()

    def _colorToFreq(self, num):
        num = abs(num - 255)
        return int(ceil(1 + (float(num - 2) / float(255 - 1) * (100 - 1))))
