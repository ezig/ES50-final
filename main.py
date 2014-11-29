
from weather import *
from time import sleep
import RPi.GPIO as GPIO


SERVOPINLEFT = 11
SERVOPINRIGHT = 13
SERVOPINLIFT = 15

UP = 0
DOWN = 1
WIPE = 2

#miliseconds
LEVELWRITE = TODO
LEVELUP = TODO
LEVELWIPE = TODO

LIFTSPEED = 0.0015

# Set pin numbering mode
GPIO.setmode(GPIO.BOARD)

# Set servo pins as output
GPIO.setup(SERVOLEFT,GPIO.OUT)
GPIO.setup(SERVOLEFT,GPIO.OUT)
GPIO.setup(SERVOLEFT,GPIO.OUT)

# Set up the pins for PWM at 50 HZ (meaning 20 ms periods)
leftPWM = GPIO.PWM(SERVOPINLEFT, 50)
rightPWM = GPIO.PWM(SERVOPINRIGHT, 50)
liftPWM = GPIO.PWM(SERVOPINLIFT, 50)

servoLift = TODO

def wipe():
	lift(WIPE)

def drawnum(num):
	if num == '0':
		lift(UP)
	elif num == '1':
		lift(UP)
	elif num == '2':
		lift(UP)
	elif num == '3':
		lift(UP)
	elif num == '4':
		lift(UP)
	elif num == '5':
		lift(UP)
	elif num == '6':
		lift(UP)
	elif num == '7':
		lift(UP)
	elif num == '8':
		lift(UP)
	elif num == '9':
		lift(UP)
	elif num == '.':
		lift(UP)

def getDigits(temp):
	return list(str(temp))

def lift(level):
	if level == UP:
		if servoHeight >= LEVELUP:
			while servoHeight >= LEVELUP:
				servoLift -= 0.001
				liftPWM.ChangeDutyCycle(servoLift/20.0*100)				
				sleep(LIFTSPEED)

		else:
			while servoLift <= LEVELUP:
				servoLift += 0.001
				servo1.writeMicroseconds(servoLift/20.0*100);
				sleep(LIFTSPEED)

	elif level == DOWN:
		if servoHeight >= LEVELDOWN:
			while servoHeight >= LEVELDOWN:
				servoLift -= 0.001
				liftPWM.ChangeDutyCycle(servoLift/20.0*100)				
				sleep(LIFTSPEED)

		else:
			while servoLift <= LEVELDOWN:
				servoLift += 0.001
				servo1.writeMicroseconds(servoLift/20.0*100);
				sleep(LIFTSPEED)

	elif level == WIPE:
		if servoHeight >= WIPE:
			while servoHeight >= LEVELWIPE:
				servoLift -= 0.001
				liftPWM.ChangeDutyCycle(servoLift/20.0*100)				
				sleep(LIFTSPEED)

		else:
			while servoLift <= LEVELWIPE:
				servoLift += 0.001
				servo1.writeMicroseconds(servoLift/20.0*100);
				sleep(LIFTSPEED)

while (1):
	weatherGetter = Weather()
	temp = weatherGetter.getWeather()
	print(getDigits(temp))
	break;