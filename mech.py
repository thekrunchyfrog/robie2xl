import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(20, gpio.OUT)
gpio.setup(26, gpio.OUT)

gpio.output(20, gpio.HIGH)
gpio.output(26, gpio.HIGH)
time.sleep(1)
gpio.output(20, gpio.LOW)
gpio.output(26, gpio.LOW)