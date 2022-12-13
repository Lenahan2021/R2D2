import RPi.GPIO as GPIO
import time
ledPin = 11

def destroy():
    GPIO.cleanup()
    

def led():
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(ledPin, GPIO.OUT)
        GPIO.output(ledPin, GPIO.HIGH)
        print('led turned on >>>')
        time.sleep(3)
        GPIO.output(ledPin, GPIO.LOW)
        print('led turned off >>>')
        time.sleep(1)
        destroy()


def commands(data):
    if data == "1":
      led()