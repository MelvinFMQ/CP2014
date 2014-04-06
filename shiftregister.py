# Author: Melvin Foo, contact me at foo.mawqing.melvin@gmail.com
# Distribution: Raspbian
# Python: 3.2

import RPi.GPIO as GPIO
import time


# Set up pins
DEBUG = 1    
GPIO.setmode(GPIO.BOARD) # tell the GPIO use board references

data_out = 7
shift_load = 21
clock = 26
clock_in = 23

GPIO.setup(shift_load, GPIO.OUT)
GPIO.setup(clock, GPIO.OUT)
GPIO.setup(data_out, GPIO.IN)
GPIO.setup(clock_in, GPIO.OUT)

GPIO.output(clock, GPIO.HIGH)


#load the data
GPIO.output(clock_in, GPIO.HIGH)
GPIO.output(shift_load, GPIO.LOW)
time.sleep(0.5)
GPIO.output(shift_load, GPIO.HIGH)
GPIO.output(clock_in, GPIO.LOW)


data = ""
for i in range(8):
    GPIO.output(clock, GPIO.LOW)
    time.sleep(1)
    if GPIO.input(data_out)== 1:
        data = data + '1'
    else:
        data = data + '0'
    GPIO.output(clock, GPIO.HIGH)
    time.sleep(1)
  
print(data)

GPIO.cleanup()
