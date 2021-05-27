from gpiozero import Button, DigitalOutputDevice, LED
from time import sleep

class Hamtrack:
    def __init__(self, sensorPowerGpioPin, sensorOutGpioPin, irLightGpioPin ):
        self.sensorPowerGpioPin = sensorPowerGpioPin
        self.sensorOutGpioPin = sensorOutGpioPin
        self.irLightGpioPin = irLightGpioPin

    def on():
        print("turning on hamtrack")
