import RPi.GPIO as GPIO
from time import sleep

dac = [8,11,7,1,0,5,12,6]
comp = 14
troyka = 13
led = [2,3,4,17,27,22,10,9]
GPIO.setmode(GPIO.BCM)
GPIO.setup(led,GPIO.OUT)
GPIO.setup(dac,GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp,GPIO.IN)

def dec2bin(num):
    return [int(elem) for elem in bin(num)[2:].zfill(8)]

def adc1():
    for i in range(256):
        dac_val = dec2bin(i)
        GPIO.output(dac, dac_val)
        sleep(0.01)
        comp_val = GPIO.input(comp)
        if comp_val:
            return i
    return 0

def adc2():
    inValue = 0
    for i in range(7,-1,-1):
        inValue += 2**i
        GPIO.output(dac,dec2bin(inValue))
        sleep(0.01)
        comp_val = GPIO.input(comp)
        if comp_val == 1:
            inValue -= 2**i
    return inValue

def volume(val):
    val = int(val*8/255)
    arr = [0]*8
    for i in range(val):
        arr[i] = val
    return arr

try:
    while True:
        i = adc2()
        if i:
            GPIO.output(led,volume(i))

finally:
    GPIO.output(dac,0)
    GPIO.cleanup()