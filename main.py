
from weather import *
from time import sleep
import RPi.GPIO as GPIO
from math import *

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

LIFTSPEED = 1500

# Set pin numbering mode
GPIO.setmode(GPIO.BOARD)

# Set servo pins as output
GPIO.setup(SERVOLEFT,GPIO.OUT)
GPIO.setup(SERVOLEFT,GPIO.OUT)
GPIO.setup(SERVOLEFT,GPIO.OUT)

# Set up the pins for PWM at 50 HZ (meaning 20 ms periods)
leftservo = GPIO.PWM(SERVOPINLEFT, 50)
rightservo = GPIO.PWM(SERVOPINRIGHT, 50)
liftservo = GPIO.PWM(SERVOPINLIFT, 50)

currentX = TODO
currentY = TODO

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
				servoLift -= 1
				lwriteMicroseconds(liftServo, servoLift)
				delayMicroseconds(LIFTSPEED)

		else:
			while servoLift <= LEVELUP:
				servoLift += 1
				writeMicroseconds(liftServo, servoLift)
				delayMicroseconds(LIFTSPEED)

	elif level == DOWN:
		if servoHeight >= LEVELDOWN:
			while servoHeight >= LEVELDOWN:
				servoLift -= 1
				writeMicroseconds(liftServo, servoLift)
				delayMicroseconds(LIFTSPEED)

		else:
			while servoLift <= LEVELDOWN:
				servoLift += 1
				writeMicroseconds(liftServo, servoLift)
				delayMicroseconds(LIFTSPEED)

	elif level == WIPE:
		if servoHeight >= WIPE:
			while servoHeight >= LEVELWIPE:
				servoLift -= 1
				writeMicroseconds(liftServo, servoLift)
				delayMicroseconds(LIFTSPEED)

		else:
			while servoLift <= LEVELWIPE:
				servoLift += 1
				writeMicroseconds(liftServo, servoLift)
				delayMicroseconds(LIFTSPEED)

def setDest(x, y):
	dx = x - currentX
	dy = y - currentY

	distance = sqrt(dx*dx + dy*dy)
	steps = TODO * distance #how many steps per unit?

	for i in range(0,steps):
		goToXY(currentX+dx/steps,currentY+dy/steps)
		currentX += dx/steps
		currentY += dy/steps


def goToXY(x, y):
	#How to physics?

def writeMicroseconds(servo, microseconds):
	servo.ChangeDutyCycle(microsends/200)

def delayMicroseconds(microseconds):
	sleep(microseconds/1000000)

while (1):
	weatherGetter = Weather()
	temp = weatherGetter.getWeather()
	print(getDigits(temp))
	break;