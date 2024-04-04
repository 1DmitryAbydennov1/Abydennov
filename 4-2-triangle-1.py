import RPi.GPIO as GPIO
from time import sleep

def dec2bin(value):
    return [int(x) for x in bin(value)[2:].zfill(8)]

dac = [8,11,7,1,0,5,12,6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)

is_min = 1
x = 0
try:
    period = float(input("Enter period: "))

    while True:
        GPIO.output(dac,dec2bin(x))

        if x == 0:
            is_min = 1
        else:
            if x == 255:
                is_min = 0
        if is_min == 1:
            x = x + 1
        else:
            x = x - 1
        sleep(period/512)
except Exception:
    print("Period isn't correct")
finally:
    GPIO.output(dac,0)
    GPIO.cleanup()