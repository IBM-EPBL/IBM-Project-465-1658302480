import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

ledPin = 8

GPIO.setup(ledPin, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
while True: # Run forever
    GPIO.output(ledPin, GPIO.HIGH) # Turn on
    sleep(1) # Sleep for 1 second
    GPIO.output(ledPin, GPIO.LOW) # Turn off
    sleep(1) # Sleep for 1 second

    break

red = 11
yellow = 13
green = 15

GPIO.setup(red, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(yellow, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(green, GPIO.OUT, initial=GPIO.LOW)

while 1:
    GPIO.output(red, GPIO.HIGH)
    sleep(2)
    GPIO.output(red, GPIO.LOW)
    GPIO.output(yellow, GPIO.HIGH)
    sleep(0.5)
    GPIO.output(yellow, GPIO.LOW)
    GPIO.output(green, GPIO.HIGH)
    sleep(1)
    GPIO.output(green, GPIO.LOW)
    