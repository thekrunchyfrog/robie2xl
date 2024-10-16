import RPi.GPIO as gpio
from math import ceil
from random import randint
from time import sleep


class Guts:
    _btnA = 31
    _btnB = 33
    _btnC = 35
    _btnD = 37

    _rightEye = 22
    _leftEye = 38

    _domeRed = 36
    _domeGreen = 38
    _domeBlue = 40
    _freq = 50
    _button_pressed = None

    def __init__(self):
        gpio.setmode(gpio.BOARD)
        gpio.setwarnings(False)

        gpio.setup(self._btnA, gpio.IN, pull_up_down=gpio.PUD_DOWN)
        gpio.add_event_detect(self._btnA, gpio.RISING, callback = self.button_callback)

        gpio.setup(self._btnB, gpio.IN, pull_up_down=gpio.PUD_DOWN)
        gpio.add_event_detect(self._btnB, gpio.RISING, callback = self.button_callback)

        gpio.setup(self._btnC, gpio.IN, pull_up_down=gpio.PUD_DOWN)
        gpio.add_event_detect(self._btnC, gpio.RISING, callback = self.button_callback)

        gpio.setup(self._btnD, gpio.IN, pull_up_down=gpio.PUD_DOWN)
        gpio.add_event_detect(self._btnD, gpio.RISING, callback = self.button_callback)

        gpio.setup(self._rightEye, gpio.OUT)
        gpio.setup(self._leftEye, gpio.OUT)

        gpio.setup(self._domeRed, gpio.OUT)
        gpio.setup(self._domeGreen, gpio.OUT)
        gpio.setup(self._domeBlue, gpio.OUT)

        self.domeRED = gpio.PWM(self._domeRed, self._freq)
        self.domeGREEN = gpio.PWM(self._domeGreen, self._freq)
        self.domeBLUE = gpio.PWM(self._domeBlue, self._freq)

        self.button_pressed = 0

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

    def button_callback(self, channel):
        match channel:
            case 31:
                self.button_pressed = "a"
            case 33:
                self.button_pressed = "b"
            case 35:
                self.button_pressed = "c"
            case 37:
                self.button_pressed = "d"

    def getButtonPressed(self):
        return self.button_pressed