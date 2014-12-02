from weather import *
from time import sleep
import RPi.GPIO as GPIO
from math import *
from multiprocessing import Process

# GPIO pins for servo
SERVOPINLEFT = 11
SERVOPINRIGHT = 13
SERVOPINLIFT = 15

# Lift commands
UP = 0
DOWN = 1
WIPE = 2

# Positions for various leves of lifting
LEVELWRITE = 500
LEVELUP = 2500
LEVELWIPE = 1500

# determines speed of the servo, higher is slower
LIFTSPEED = 1500

# Set pin numbering mode
GPIO.setmode(GPIO.BOARD)

# Set servo pins as output
GPIO.setup(SERVOPINLEFT,GPIO.OUT)
GPIO.setup(SERVOPINRIGHT,GPIO.OUT)
GPIO.setup(SERVOPINLIFT,GPIO.OUT)

# Set up the pins for PWM at 50 HZ (meaning 20 ms periods)
leftServo = GPIO.PWM(SERVOPINLEFT, 50)
rightServo = GPIO.PWM(SERVOPINRIGHT, 50)
liftServo = GPIO.PWM(SERVOPINLIFT, 50)

# keeps track of location of pen
# currentX = TODO
# currentY = TODO

# Keeps track of the lift position of the pen
servoHeight = 500

# For each number, there is a set of angles that needs to be reached by the left and right servos
# Point A would be at the top of zero and point B would be at the bottom of zero; it would write out 0 in a counter clockwise fashion
LEVELLEFT0A = TODO
LEVELRIGHT0A = TODO
LEvELLEFT0B = TODO
LEVELLEFT0B = TODO
# Point A would be at the bottom of 1 and point B would be at the top of 1; 1 would be written as a straight line
LEVELLEFT1A = TODO
LEVELRIGHT1A = TODO
LEVELLEFT1B = TODO
LEVELRIGHT1B = TODO

def wipe():
	"""gets the eraser and then clears the board"""

	lift(UP)

# given a number as a string (or a decimal point)
def drawNum(num):
	"""Given a digit or . as a string, writes the digit by lifting up the pen,
	going to the appropriate location, putting the pen down, and then writing"""

	if num == '0':
		lift(UP)
	elif num == '1':
		lift(UP)

        """The outline for the code in the following seven lines was obtained from StackOverflow: "http://stackoverflow.com/questions/7207309/python-how-can-i-run-python-functions-in-parallel". This method will be used throughout our drawNum function. """
        if __name__ == '__main__':
            a = Process(target = rightadjust, args = (1,))
            a.start()
            b = Process(target = leftadjust, args = (1,))
            b.start()
            a.join()
            b.join()
        """The above method is called multiprocessing. It should allow us to executie both functions at the same time. Multiprocessing seems to be very important when we actually have to draw the 1. The left and right servos must move together, and at the same rate (taken care of by LIFTSPEED), so that the vertical straight line is drawn"""
        lift(DOWN)
        if __name__ == '__main__':
            a = Process(target = rightwrite, args = (1,))
            a.start()
            b = Process(target = leftwrite, args = (1,))
            b.start()
            a.join()
            b.join()
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
	"""Given the temp as a float, returns an array of the characters
	representing the digits (and the decimal point)"""

	return list(str(temp))
# # While the pen is up, move the right servo to the correct starting angle, defined by LEVELRIGHT1a
# def rightadjust(num):
#     if num == 1
#         if servoRight > LEVELRIGHT1A
#             while servoRight > LEVELRIGHT1A
#                 servoRight -= 1
#                 lwriteMicrosceonds(rightServo, servoRight)
#                 delayMicroseconds(LIFTSPEED)
#         else if servoRight < LEVELRIGHT1A
#             while servoRight > LEVELRIGHT1a
#                 servoRight += 1
#                 lwriteMicroseconds(rightServo, servoRight)
#                 delayMicroseconds(LIFTSPEED)

# # After the pen is down, the right servo must move counterclockwise (the angle from the Raspberry Pi perspective is decreasing)
# def rightwrite(num):
#     if num == 1
#         while servoRight > LEVELRIGHT1B
#             servoRight -= 1
#             lwriteMicroseconds(rightServo, servoRight)
#             delayMicroseconds(LIFTSPEED)

# # Move Left servo to the correct starting angle, defined by LEVELRIGHT1a
# def leftadjust(num):
#     if num == 1
#         if servoLeft > LEVELLEFT1a
#             while servoLeft > LEVELLEFT1a
#                 servoLeft -= 1
#                     lwriteMicrosceonds(leftServo, servoLeft)
#                     delayMicroseconds(LIFTSPEED)
#         else if servoLeft < LEVELLEFT1a
#             while servoLeft > LEVELLEFT1a
#                 servoLeft += 1
#                 lwriteMicroseconds(leftServo, servoLeft)
#                 delayMicroseconds(LIFTSPEED)
# # When the pen is down, the left servo must move clockwise (Raspberry Pi thinks the angle is increasing)
# def leftwrite(num):
#     if num == 1
#         while servoLeft < LEVELLEFT1b
#             servoLeft += 1
#                 lwriteMicroseconds(leftServo, servoLeft)
#                 delayMicroseconds(LIFTSPEED)

def lift(level):
	"""Given the level UP, DOWN, or WIPE, raises or lowers the pen
	to the appropriate point based on the current lift position stored
	in servoHeight"""
	global servoHeight, UP, DOWN, WIPE LIFTSPEED, LEVELUP, LEVELWRITE, LEVELWIPE, liftServo

	#start the servo at the current position
	# (microseconds / 1000 / 20 ms  * 100% = duty cycle)
	liftServo.start(servoHeight/200.0)

	if level == UP:
		if servoHeight >= LEVELUP:
			while servoHeight >= LEVELUP:
				servoHeight -= 1
				writeMicroseconds(liftServo, servoHeight)
				delayMicroseconds(LIFTSPEED)

		else:
			while servoHeight <= LEVELUP: 
				servoHeight += 1
				writeMicroseconds(liftServo, servoHeight)
				delayMicroseconds(LIFTSPEED)

	elif level == DOWN:
		if servoHeight >= LEVELWRITE:
			while servoHeight >= LEVELWRITE:
				servoHeight -= 1
				writeMicroseconds(liftServo, servoHeight)
				delayMicroseconds(LIFTSPEED)

		else:
			while servoHeight <= LEVELWRITE:
				servoHeight += 1
				writeMicroseconds(liftServo, servoHeight)
				delayMicroseconds(LIFTSPEED)

	elif level == WIPE:
		if servoHeight >= WIPE:
			while servoHeight >= LEVELWIPE:
				servoHeight -= 1
				writeMicroseconds(liftServo, servoHeight)
				delayMicroseconds(LIFTSPEED)

		else:
			while servoHeight <= LEVELWIPE:
				servoHeight += 1
				writeMicroseconds(liftServo, servoHeight)
				delayMicroseconds(LIFTSPEED)

	liftServo.stop()

def linePath(x, y):
	"""Given a destination x,y, calls goToXY in a loop so that a straight
	is drawn between currentX, currentY and the destination"""
	global currentX, currentY

	dx = x - currentX
	dy = y - currentY

	# use distance formula
	distance = sqrt(dx*dx + dy*dy)
	# steps = TODO * distance #how many steps per unit?

	# break the 
	for i in range(0,steps):
		goToXY(currentX+dx/steps,currentY+dy/steps)
		currentX += dx/steps
		currentY += dy/steps

def arcPath(centerX, centerY, radius, startAngle, endAngle, direction):
	sweptAngle = 0

	if direction == 'Clockwise':
		increment = -0.05 # how far to go each step 
	elif direction == 'Counterclockwise'
		increment = 0.05

	while startAngle + sweptAngle < endAngle:
		linePath(centerX + radius * cos(startAngle + sweptAngle), 
			centerY + radius * sin(startAngle + sweptAngle))
		sweptAngle += increment


def goToXY(x, y):
	"""Given an x,y points, determines the current number of microseconds to
	write to the left servo and the right servo"""

	# TODO
	#How to physics?

def writeMicroseconds(servo, microseconds):
	"""Calculates duty cycle based on desired pulse width"""
	servo.ChangeDutyCycle(microseconds/200.0)

def delayMicroseconds(microseconds):
	"""Coverts microsecond delay to seconds delay"""
	sleep(microseconds/1000000.0)

# while (1):
# 	weatherGetter = Weather()
# 	temp = weatherGetter.getWeather()
# 	digits = getDigist(temp)
# 	print(digits)
# 	for i in range(1,len(digits)):
# 		drawNum(digits[i])
# 	break;

#test code
for i in range(0,10):
	lift(UP)
	sleep(1)
	lift(WIPE)
	sleep(1)
	lift(DOWN)
	sleep(1)

GPIO.cleanup()
