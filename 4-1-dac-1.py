import RPi.GPIO as GPIO

def dec2bin(value):
    return [int(x) for x in bin(value)[2:].zfill(8)]

dac = [8,11,7,1,0,5,12,6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)

try:
    while True:
        num = input("Enter number from 0 to 255: ")
        try:
            num = int(num)
            if ((num >= 0) and (num <= 255)):
                GPIO.output(dac,dec2bin(num))
                volt = float(num)*3.3/255
                print(volt, "V")
            else:
                if num < 0:
                    print("Number must be >= 0")
                if num > 255:
                    print("NUmber must be <= 255")
        except Exception:
            if num == 'q':
                break
            print("Entered not number")
finally:
    GPIO.output(dac,0)
    GPIO.cleanup()