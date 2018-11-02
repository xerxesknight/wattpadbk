import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)

list=[37,35,33]
while True:
    for num in range(len(list)):
        GPIO.output(list[num],True)
        time.sleep(0.1)
        GPIO.output(list[num],False)
        time.sleep(0.1)
GPIO.cleanup()