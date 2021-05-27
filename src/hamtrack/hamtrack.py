from gpiozero import Button, DigitalOutputDevice, LED
from time import sleep
import datetime

class Hamtrack:
    def __init__(self, sensorPowerGpioPin, sensorOutGpioPin, irLightGpioPin, encoderDiscValue,
                 bucketPeriodSeconds, dataCallback, wheelCircumferenceMetres ):
        self.SensorPowerGpioPin = sensorPowerGpioPin
        self.SensorOutGpioPin = sensorOutGpioPin
        self.IrLightGpioPin = irLightGpioPin
        self.IrLight = DigitalOutputDevice(self.IrLightGpioPin)
        self.IrSensorPower = DigitalOutputDevice(self.SensorPowerGpioPin)
        self.IrSensor = Button(self.SensorOutGpioPin)

        self.EncoderDiscValue = encoderDiscValue
        self.BucketPeriodSeconds = bucketPeriodSeconds
        self.DataCallback = dataCallback
        self.WheelCircumferenceMetres = wheelCircumferenceMetres 
        
    def flip(self):
        if (self.LastValue != self.IrSensor.value):
            self.LastValue = self.IrSensor.value
            newTime = datetime.datetime.utcnow()
            if (self.IrSensor.value == 0):
                deltaT = (newTime - self.BucketTime).total_seconds()
                if (deltaT >= self.BucketPeriodSeconds):
                    if (self.PartialRotationCount>0):
                        self.Rpm = (self.PartialRotationCount / self.EncoderDiscValue) * (60 / self.BucketPeriodSeconds)
                        self.Distance = self.PartialRotationCount / self.EncoderDiscValue * self.WheelCircumferenceMetres
                        self.Speed = self.Distance / 1000 * (60 * 60 / self.BucketPeriodSeconds)
                        data = {}
                        data["RPM"] = self.Rpm
                        data["Distance"] = self.Distance
                        data["Speed"] = self.Speed
                        data["Time"] = self.BucketTime
                        self.DataCallback(data)
                        self.PartialRotationCount=0
                    self.BucketTime = newTime
                else:
                    self.PartialRotationCount += 1
            

    def on(self):
        print("turning on hamtrack")
        self.IrSensorPower.on()
        self.IrSensor.when_released = self.flip
        self.IrSensor.when_pressed = self.flip
        self.PartialRotationCount = 0
        self.BucketTime = datetime.datetime.utcnow()
        self.LastValue = self.IrSensor.value

        
    def off(self):
        print("turning off hamtrack")
        self.IrSensorPower.off()
        self.IrLight.off()
        self.IrSensor.when_released = None
        self.IrSensor.when_pressed = None
        
