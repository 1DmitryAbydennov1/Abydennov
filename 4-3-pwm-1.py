import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.OUT)

p = GPIO.PWM(25,1000)
p.start(0)

try:
    while True:
        f = int(input("Input coef: "))
        p.ChangeDutyCycle(f)
        print(3.3*f/100)
finally:
    p.stop()
    GPIO.output(25,0)
    GPIO.cleanup()