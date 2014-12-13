from weather import * 
from time import sleep 
import RPi.GPIO as GPIO 
from math import * 
import sys

# GPIO pins for servo
SERVOPINLEFT = 11
SERVOPINRIGHT = 13
SERVOPINLIFT = 15

# Lift commands
UP = 0
DOWN = 1

# Positions for various leves of lifting
LEVELWRITE = 1500
LEVELUP = 2500

# respresents a sweep of 90 degrees (pi/2 rad) for each motor (found by trial and error)
SERVO90 = 620

# angles for which the left and right servos are parallel to the x axis (found by trial and error)
LEFTSERVONULL = 1900
RIGHTSERVONULL = 984

# determines speed of the servo, higher is slower
LIFTSPEED = 1500

# keeps track of location of pen
currentX = 10.0
currentY = 10.0

# length of arm closest to servo
SHORTARMLENGTH = 35.1
# length of arm connected to pen
LONGARMLENGTH = 55.2

#half the distance between the two motors 
SERVODISTANCE = 13.0


# origin points of left and right servo 
LEFTSERVOX = 22
LEFTSERVOY = -25
RIGHTSERVOX = 47
RIGHTSERVOY = -25

GPIO.cleanup()

# Set pin numbering mode
GPIO.setmode(GPIO.BOARD)

# Set servo pins as output
GPIO.setup(SERVOPINLEFT, GPIO.OUT)
GPIO.setup(SERVOPINRIGHT, GPIO.OUT)
GPIO.setup(SERVOPINLIFT, GPIO.OUT)

# Set up the pins for PWM at 50 HZ (meaning 20 ms periods)
leftServo = GPIO.PWM(SERVOPINLEFT, 50)
rightServo = GPIO.PWM(SERVOPINRIGHT, 50)
liftServo = GPIO.PWM(SERVOPINLIFT, 50)

def drawNum(num, x, y):
	"""Given a digit as an int, writes the digit by
	going to the appropriate location, putting the pen down, writing, and then lifting the pen up"""
	global UP,DOWN, WIPE

	if num == 0:
		linePath(x + 1.0, y + 5.0)
		lift(DOWN)
		arcPath(x + 1.0, y + 15.0, 7.0, -0.8, 7.6, 'Counterclockwise')
		lift(UP)
	if num == 1:
		linePath(x + 0.0, y + 5.0)
		lift(DOWN)
		linePath(x + 0.0, y + 20.0)
		lift(UP)
	if num == 2:
		linePath(x + 0.0, y + 3.0)
		lift(DOWN)
		arcPath(x - 12.0, y + 3.0, 12.0, 6.5, 3, 'Clockwise')
		linePath(x + 20.0, y + 25.0)
		sleep(0.01)
		linePath(x - 13.0, y + 20.0)
		lift(UP)
	if num == 3:
		linePath(x + 1.0, y + 5.0)
		lift(DOWN)
		arcPath(x - 7.0, y + 7.0, 7.0, 6.0, 1.0, 'Clockwise')
		sleep(0.01)
		arcPath(x + 1.0, y + 21.0, 7.0, 6.0, 0.0, 'Clockwise')
		lift(UP)
	if num == 4:
		linePath(x + 1.0, y - 3.0)
		lift(DOWN)
		linePath(x + 1.0, y + 12.0)
		sleep(0.01)
		linePath(x - 10.0, y + 12.0)
		sleep(0.01)
		linePath(x - 10.0, y - 3.0)
		sleep(0.01)
		linePath(x - 10.0, y + 19.0)
		lift(UP)
	if num == 5:
		linePath(x + 5.0, y + 0.0)
		lift(DOWN)
		sleep(0.5)
		linePath(x + 15.0, y + 0.0)
		sleep(0.5)
		linePath(x + 15.0, y + 22.0)
		sleep(0.5)
 		arcPath(x + 6.5, y + 20.0, 7.0, 6.0, 0.2, 'Clockwise')
		lift(UP)
	if num == 6:
		linePath(x + 1.0, y - 2.0)
		lift(DOWN)
		arcPath(x + 1.0, y + 18.0, 7.0, -0.8, 7.6, 'Counterclockwise')
		sleep(0.5)
		lift(UP)
	if num == 7:
		linePath(x + 6.0, y - 3.0)
		lift(DOWN)
		linePath(x - 15.0, y - 3.0)
		sleep(0.01)
		linePath(x + 6.0, y + 18.0)
		lift(UP)
	if num == 8:
		linePath(x + 3.0, y - 3.0)
		lift (DOWN)
		arcPath(x + 0.0, y + 0.0, 7.0, 4.5, -4.8, 'Clockwise')
		sleep(0.5)
		arcPath(x + 8.0, y + 14.0, 7.0, 4.5, 11.0, 'Counterclockwise')
		lift(UP)
	if num == 9:
		linePath(x + 1.0, y + 3.0)
		lift(DOWN)
		arcPath(x + 1.0, y + 2.0, 9.0, 5.5, -3.0, 'Clockwise')
		sleep(0.01)
		linePath(x -8.0, y + 20.0)
		lift(UP)

def lift(level):
	"""Given the level UP, DOWN, or WIPE, raises or lowers the pen
	to the appropriate point based on the current lift position stored
	in servoHeight"""
	global servoHeight, UP, DOWN, LIFTSPEED, LEVELUP, LEVELWRITE, liftServo

    # change the lift so that the pen is above the surface
	if level == UP:
		#pen is too high
		if servoHeight >= LEVELUP:
			while servoHeight >= LEVELUP:
				servoHeight -= 1
				writeMicroseconds(liftServo, servoHeight)
				delayMicroseconds(LIFTSPEED)
		#pen is too low
		else:
			while servoHeight <= LEVELUP: 
				servoHeight += 1
				writeMicroseconds(liftServo, servoHeight)
				delayMicroseconds(LIFTSPEED)

    # change the lift so the pen is on the writing surface
	elif level == DOWN:
		#pen is too high
		if servoHeight >= LEVELWRITE:
			while servoHeight >= LEVELWRITE:
				servoHeight -= 1
				writeMicroseconds(liftServo, servoHeight)
				delayMicroseconds(LIFTSPEED)
		#pen is too low
		else:
			while servoHeight <= LEVELWRITE:
				servoHeight += 1
				writeMicroseconds(liftServo, servoHeight)
				delayMicroseconds(LIFTSPEED)

def linePath(x, y):
	"""Given a destination x,y, calls goToXY in a loop so that a straight
	is drawn between currentX, currentY and the destination"""
	global currentX, currentY

	dx = x - currentX
	dy = y - currentY

	# use distance formula
	steps = int(floor(4 * sqrt(dx*dx + dy*dy)))
	#steps = int(4 * distance) #how many steps per unit?

	# Move in small increments
	for i in range(0,steps):
		goToXY(currentX+dx/steps,currentY+dy/steps)
		currentX += dx/steps
		currentY += dy/steps
		sleep(0.005)

def arcPath(centerX, centerY, radius, startAngle, endAngle, direction):
	"""Draws a circle of given radius about the given center point
	from startAngle to endAngle (in rad) in the designated direction 
	(either 'Clockwise' or 'Counterclockwise') """

	sweptAngle = 0
    # For the clockwise direction, 0 is on the left side, pi/2 is at the top, pi is on the right, and 3pi/2 is at the bottom
	if direction == 'Clockwise':
		increment = -0.05 # how far to go each step
        # Clockwise motion increases the angle.
		while startAngle + sweptAngle > endAngle:
        # The actual number we give the start angle is more than the actual number for the end angle. The servos will move over the difference between those two angles in the clockwise direction
            linePath(centerX + radius * cos(startAngle + sweptAngle),
				centerY + radius * sin(startAngle + sweptAngle))
			sweptAngle += increment
			
	elif direction == 'Counterclockwise':
		increment = 0.05
        # Counterclockwise motion also increases the angle
        # For the counterclockwise direction, 0 is on the right side, pi/2 is at the top, pi is on the left, and 3pi/2 is at the bottom
        while startAngle + sweptAngle < endAngle:
            # The actual number for the start angle is less than the number for the end angle. Only the difference between those two values matters
			linePath(centerX + radius * cos(startAngle + sweptAngle), 
				centerY + radius * sin(startAngle + sweptAngle))
			sweptAngle += increment

	sleep(0.005)

def return_angle(a, b, c):
 	"""Uses the law of cosinse to find the angle between c and a
 	for a triangle with side lengths a, b, c """
 	return acos((a * a + c * c - b * b) / (2 * a * c))

def goToXY(targetX, targetY):
	"""Based on the currentX and currentY position, moves the pen to
	the desired targetX, targetY coordinates"""

 	global LEFTSERVOX, LEFTSERVOY, SHORTARMLENGTH, LONGARMLENGTH, SERVODISTANCE, rightServo, leftServo, LEFTSERVONULL, RIGHTSERVONULL 

	#calculate triangle between pen, left servo and arm joint
	dx = targetX - LEFTSERVOX
	dy = targetY - LEFTSERVOY

    #polar lemgth (c) and angle (a1)
    # get distance between start and end point
	c = sqrt(dx * dx + dy * dy) 
	a1 = atan2(dy, dx)
	a2 = return_angle(SHORTARMLENGTH, LONGARMLENGTH, c)

	writeMicroseconds(leftServo, floor(((a2 + a1 - pi) * SERVO90) + LEFTSERVONULL))

	#calculate the triangle for the right servo arm
	a2 = return_angle(LONGARMLENGTH, SHORTARMLENGTH, c);
	rightX = targetX + SERVODISTANCE * cos((a1 - a2 + 0.621) + pi)
	rightY = targetY + SERVODISTANCE * sin((a1 - a2 + 0.621) + pi)

	#calculate triangle between pen joint, servoRight and arm joint
	dx = rightX - RIGHTSERVOX
	dy = rightY - RIGHTSERVOY

	c = sqrt(dx * dx + dy * dy)
	a1 = atan2(dy, dx)
	a2 = return_angle(SHORTARMLENGTH, (LONGARMLENGTH - SERVODISTANCE), c)

	writeMicroseconds(rightServo, floor(((a1 - a2) * SERVO90) + RIGHTSERVONULL))

def writeMicroseconds(servo, microseconds):
	"""Calculates duty cycle based on desired pulse width
	(emulates the way that arduino handles servo control)"""

	servo.ChangeDutyCycle(microseconds/200.0)

def delayMicroseconds(microseconds):
	"""Converts microseconds delay to seconds delay
	 (emulates arduino function)"""

	sleep(microseconds/1000000.0)

# start the servos in a "neutral" position
leftServo.start(1500.0/200.0)
rightServo.start(1500.0/200.0)
liftServo.start(servoHeight/200.0)

# if user does not give a number, get the temperature
if len(sys.argv) == 1:	
	weatherGetter = Weather()
	
	# get the temperature from weather object
	temp = weatherGetter.getWeather())	
	print(temp)

	# print the tens digit
    drawNum(temp / 10, 20.0, 25.0)
    # move over to write the next digit
	linePath(0.0, 25.0)
    # draw the ones digit
    drawNum(temp % 10, 5.0, 25.0)

    # move back to the start point for the next run
	linePath(10.0, 10.0)

# If the user inputs a number, then write that number
else:
	num = int(sys.argv[1])

	print(num)
    # Single-digit number
	if num < 10:
		drawNum(num, 20.0, 25.0)
		linePath(10.0, 10.0)
    # Two digit numbers
	else:
		drawNum(num / 10, 20.0, 25.0)
		linePath(0.0, 25.0)
		drawNum(num % 10, 5.0, 25.0)
		linePath(10.0, 10.0)

# cleanup
leftServo.stop()
rightServo.stop()
liftServo.stop()

GPIO.cleanup()