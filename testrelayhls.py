import RPi.GPIO as GPIO
from gpiozero import InputDevice
import time

channel = 27
signal = InputDevice(21)
# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)


def motor_off(pin):
    GPIO.output(pin, GPIO.HIGH)  # Turn motor on


def motor_on(pin):
    GPIO.output(pin, GPIO.LOW)  # Turn motor off

while True:
    if not signal.is_active:
            print("motor om")
            motor_on(channel)
            time.sleep(1)
            
    else:
            print("motor off")
            motor_off(channel)
            time.sleep(2)
            