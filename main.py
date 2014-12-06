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
LEVELWRITE = 1500
LEVELUP = 2000
LEVELWIPE = 1750

#LEFTSERVONULL = 500
#RIGHTSERVONULL = 2500

SERVOFAKTOR = 620

LEFTSERVONULL = 1900
RIGHTSERVONULL = 984
# determines speed of the servo, higher is slower
LIFTSPEED = 1500

GPIO.cleanup()

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
# currentX = 75.0
# currentY = 47.5
currentX = 10.0
currentY = 10.0

p = 37
l = 47

# length of arms
L1 = 35.0
L2 = 55.1
L3 = 13.2


# origin points of left and right servo 
O1X = 22
O1Y = -25
O2X = 47
O2Y = -25

# keeps track of left right servo position
leftMicroseconds = 1500
rightMicroseconds = 1500

# Keeps track of the lift position of the pen
servoHeight = 500

# For each number, there is a set of angles that needs to be reached by the left and right servos
# Point A would be at the top of zero and point B would be at the bottom of zero; it would write out 0 in a counter clockwise fashion
#LEVELLEFT0A = TODO
#LEVELRIGHT0A = TODO
#LEvELLEFT0B = TODO
#LEVELLEFT0B = TODO
# Point A would be at the bottom of 1 and point B would be at the top of 1; 1 would be written as a straight line
#LEVELLEFT1A = TODO
#LEVELRIGHT1A = TODO
#LEVELLEFT1B = TODO
#LEVELRIGHT1B = TODO

def wipe():
	"""gets the eraser and then clears the board"""

	lift(UP)

# given a number as a string (or a decimal point)
def drawNum(num, x, y):
	"""Given a digit or . as a string, writes the digit by lifting up the pen,
	going to the appropriate location, putting the pen down, and then writing"""

	# if num == '0':
	# 	lift(UP)
	# elif num == '1':
	# 	lift(UP)

 #        """The outline for the code in the following seven lines was obtained from StackOverflow: "http://stackoverflow.com/questions/7207309/python-how-can-i-run-python-functions-in-parallel". This method will be used throughout our drawNum function. """
 #        if __name__ == '__main__':
 #            a = Process(target = rightadjust, args = (1,))
 #            a.start()
 #            b = Process(target = leftadjust, args = (1,))
 #            b.start()
 #            a.join()
 #            b.join()
 #        """The above method is called multiprocessing. It should allow us to executie both functions at the same time. Multiprocessing seems to be very important when we actually have to draw the 1. The left and right servos must move together, and at the same rate (taken care of by LIFTSPEED), so that the vertical straight line is drawn"""
 #        lift(DOWN)
 #        if __name__ == '__main__':
 #            a = Process(target = rightwrite, args = (1,))
 #            a.start()
 #            b = Process(target = leftwrite, args = (1,))
 #            b.start()
 #            a.join()
 #            b.join()
	# elif num == '2':
	# 	lift(UP)
	# elif num == '3':
	# 	lift(UP)
	# elif num == '4':
	# 	lift(UP)
	# elif num == '5':
	# 	lift(UP)
	# elif num == '6':
	# 	lift(UP)
	# elif num == '7':
	# 	lift(UP)
	# elif num == '8':
	# 	lift(UP)
	# elif num == '9':
	# 	lift(UP)
	# elif num == '.':
	# 	lift(UP)
	if num == 0:
		# linePath(x + 12.0, y + 6.0)
		lift(0)
    	arcPath(x + 1.0, y + 60.0, 15.0, -0.8, 6.7, 'Counterclockwise')
    	lift(1)
	if num == 1:
		linePath(x + 3.0, y + 15.0)
		lift(0)
		drawTo(x + 10.0, y + 20.0)
		drawTo(x + 10.0 , y + 0.0)
		lift(1)
	if num == 2:
		linePath(x + 2.0, y + 12.0)
		lift(0)
		arcPath(x + 8.0, y + 14.0, 6.0, 3.0, -0.8, 'Clockwise')
		linePath(x + 1.0, y + 0.0)
		drawTo(x + 12.0 * scale, y + 0.0 * scale)
		lift(1);
	if num == 3:
		linePath(x + 2 * scale, by + 17 * scale);
		lift(0);
		arcPath(x + 5.0, y + 15.0, 5.0, 3.0, -2.0, 'Clockwise');
		arcPath(x + 5.0, y + 5.0, 5.0, 1.57, -3.0, 'Clockwise');
		lift(1);
  # case 4:
  #   drawTo(bx + 10 * scale, by + 0 * scale);
  #   lift(0);
  #   drawTo(bx + 10 * scale, by + 20 * scale);
  #   drawTo(bx + 2 * scale, by + 6 * scale);
  #   drawTo(bx + 12 * scale, by + 6 * scale);
  #   lift(1);
  #   break;
  # case 5:
  #   drawTo(bx + 2 * scale, by + 5 * scale);
  #   lift(0);
  #   bogenGZS(bx + 5 * scale, by + 6 * scale, 6 * scale, -2.5, 2, 1);
  #   drawTo(bx + 5 * scale, by + 20 * scale);
  #   drawTo(bx + 12 * scale, by + 20 * scale);
  #   lift(1);
  #   break;
  # case 6:
  #   drawTo(bx + 2 * scale, by + 10 * scale);
  #   lift(0);
  #   bogenUZS(bx + 7 * scale, by + 6 * scale, 6 * scale, 2, -4.4, 1);
  #   drawTo(bx + 11 * scale, by + 20 * scale);
  #   lift(1);
  #   break;
  # case 7:
  #   drawTo(bx + 2 * scale, by + 20 * scale);
  #   lift(0);
  #   drawTo(bx + 12 * scale, by + 20 * scale);
  #   drawTo(bx + 2 * scale, by + 0);
  #   lift(1);
  #   break;
  # case 8:
  #   drawTo(bx + 5 * scale, by + 10 * scale);
  #   lift(0);
  #   bogenUZS(bx + 5 * scale, by + 15 * scale, 5 * scale, 4.7, -1.6, 1);
  #   bogenGZS(bx + 5 * scale, by + 5 * scale, 5 * scale, -4.7, 2, 1);
  #   lift(1);
  #   break;

  # case 9:
  #   drawTo(bx + 9 * scale, by + 11 * scale);
  #   lift(0);
  #   bogenUZS(bx + 7 * scale, by + 15 * scale, 5 * scale, 4, -0.5, 1);
  #   drawTo(bx + 5 * scale, by + 0);
  #   lift(1);
  #   break;

def getDigits(temp):
	"""Given the temp as a float, returns an array of the characters
	representing the digits (and the decimal point)"""

	return list(str(temp))
# # While the pen is up, move the right servo to the correct starting angle, defined by LEVELRIGHT1a
# def rightadjust(num):
#     if num == 1
#         if rightServo > LEVELRIGHT1A
#             while rightServo > LEVELRIGHT1A
#                 rightServo -= 1
#                 lwriteMicrosceonds(rightServo, rightServo)
#                 delayMicroseconds(LIFTSPEED)
#         else if rightServo < LEVELRIGHT1A
#             while rightServo > LEVELRIGHT1a
#                 rightServo += 1
#                 lwriteMicroseconds(rightServo, rightServo)
#                 delayMicroseconds(LIFTSPEED)

# # After the pen is down, the right servo must move counterclockwise (the angle from the Raspberry Pi perspective is decreasing)
# def rightwrite(num):
#     if num == 1
#         while rightServo > LEVELRIGHT1B
#             rightServo -= 1
#             lwriteMicroseconds(rightServo, rightServo)
#             delayMicroseconds(LIFTSPEED)

# # Move Left servo to the correct starting angle, defined by LEVELRIGHT1a
# def leftadjust(num):
#     if num == 1
#         if leftServo > LEVELLEFT1a
#             while leftServo > LEVELLEFT1a
#                 leftServo -= 1
#                     lwriteMicrosceonds(leftServo, leftServo)
#                     delayMicroseconds(LIFTSPEED)
#         else if leftServo < LEVELLEFT1a
#             while leftServo > LEVELLEFT1a
#                 leftServo += 1
#                 lwriteMicroseconds(leftServo, leftServo)
#                 delayMicroseconds(LIFTSPEED)
# # When the pen is down, the left servo must move clockwise (Raspberry Pi thinks the angle is increasing)
# def leftwrite(num):
#     if num == 1
#         while leftServo < LEVELLEFT1b
#             leftServo += 1
#                 lwriteMicroseconds(leftServo, leftServo)
#                 delayMicroseconds(LIFTSPEED)

def lift(level):
	"""Given the level UP, DOWN, or WIPE, raises or lowers the pen
	to the appropriate point based on the current lift position stored
	in servoHeight"""
	global servoHeight, UP, DOWN, WIPE, LIFTSPEED, LEVELUP, LEVELWRITE, LEVELWIPE, liftServo

	#start the servo at the current position
	# (microseconds / 1000 / 20 ms  * 100% = duty cycle)

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

	#liftServo.stop()

def linePath(x, y):
	"""Given a destination x,y, calls goToXY in a loop so that a straight
	is drawn between currentX, currentY and the destination"""
	global currentX, currentY

	dx = x - currentX
	dy = y - currentY

	# use distance formula
	steps = int(floor(4 * sqrt(dx*dx + dy*dy)))
	#steps = int(4 * distance) #how many steps per unit?

	# break the 
	for i in range(0,steps):
		goToXY(currentX+dx/steps,currentY+dy/steps)
		currentX += dx/steps
		currentY += dy/steps

def arcPath(centerX, centerY, radius, startAngle, endAngle, direction):
	sweptAngle = 0

	if direction == 'Clockwise':
		increment = -0.05 # how far to go each step 
	elif direction == 'Counterclockwise':
		increment = 0.05

	while startAngle + sweptAngle < endAngle:
		linePath(centerX + radius * cos(startAngle + sweptAngle), 
			centerY + radius * sin(startAngle + sweptAngle))
		sweptAngle += increment

# def goToXY (x, y):
	 
# 	"""Assumes global variables p (length of lower robot arm segment) and l (length of upper robot arm segment) and currentX and currentY.
# 	Takes in x, y coordinates of new destination with origin at the right servo.
# 	Takes in a, b which are exterior angles of the servo -- a is negative from the horizontal, b is positive from the horizontal.
# 	Returns the new angles of the servos. (Should newleft be negative of what it is now? Test and see.)
# 	"""
# 	global currentX, currentY, leftMicroseconds, rightMicroseconds, LEFTSERVONULL, RIGHTSERVONULL, leftServo, rightServo, p, linePath


# 	a = (leftMicroseconds - LEFTSERVONULL) / 1000.0 * pi / 2
# 	b = (rightMicroseconds - RIGHTSERVONULL) / 1000.0 * pi / 2 
#  	# Define the x and y distance the robot arms must travel
#  	dx = x - currentX
#  	dy = y - currentY

#  	# If you consider l and p as vectors, the vector L1 would be their sum (a.k.a. the shortest path from the position of the left servo to point (currentX, currentY)). 
#  	# The length L1 is defined using the Law of Cosines. It is defined as a length because Python hates vectors. 
#  	L1 = sqrt(l**2 + p**2 - 2*l*p*cos(pi/2 + a))
#  	# t1 is the angle between L1 and the horizontal. 
#  	# Defined by using the fact that L1*sin(t1) = currentY.
#  	t1 = asin(currentY / L1)
#  	# c is the length of the vector that takes you from the old point (currentX, currentY) to the new point (x,y).
#  	c = sqrt(dx**2 + dy**2)
#  	# L2 is the length of the shortest path between the position of the left servo and the new point (x,y).
#  	# Defined as the length of the vector sum of vectors L1 and c.
#  	L2 = sqrt((L1*cos(t1) + dx)**2 + (L1*sin(t1) + dy)**2)
 	
#  	#L3 is the right side equivalent of L1
#  	L3 = sqrt(l**2 + p**2 - 2*l*p*cos(pi/2 + b))
#  	# Right side equivalent of t1
#  	t2 = asin(currentY / L2)
#  	# Right side equivalent of L2
#  	L4 = sqrt((L3*cos(t2) + dx)**2 + (L3*sin(t2) + dy)**2)

# 	# Because Python hates vectors, we have hard-coded the dot products that we are going to use.
# 	L1dotL2 = (L1*cos(t1))*(L1*cos(t1) + dx) + (L1*sin(t1))*(L1*sin(t1) + dy)
# 	L3dotL4 = L3*cos(t2)*(L3*cos(t2) + dx) + (L3*sin(t2))*(L3*sin(t2) + dy)

#  	# ang1 is the angle between vectors L1 and L2
#  	# ang2 is the angle between vectors L3 and L4
#  	# Defined using Law of Cosines, we could alternatively use the dot product.
#  	val1 = (L1**2 + L2**2 - c**2) / (2*L1dotL2)
#  	if val1 > 1.0:
#  		ang1 = 0
#  	else:
#  		ang1 = acos((L1**2 + L2**2 - c**2) / (2*L1dotL2))
 	
#  	val2 = (L3**2 + L4**2 - c**2) / (2*L3dotL4)
#  	if val2 > 1.0:
#  		ang2 = 0
#  	else:
# 		ang2 = acos((L3**2 + L4**2 - c**2) / (2*L3dotL4))

#  	# leftf is the angle between p on the left and L2, rightf is the angle between p on the right and L3.
#  	leftf = acos((p**2 + L2**2 - l**2) / (2*p*L2))
#  	rightf = acos((p**2 + L4**2 - l**2) / (2*p*L4))

#  	newleft = t1 + ang1 - leftf
#  	newright = t2 + ang2 - rightf

#  	leftMicroseconds = LEFTSERVONULL + 1000 * newleft/(pi/2)
#  	rightMicroseconds = RIGHTSERVONULL +1000 * newright/(pi/2)

#  	writeMicroseconds(leftServo, leftMicroseconds)
#  	writeMicroseconds(rightServo, rightMicroseconds)

def return_angle(a, b, c):
 	#cosine rule for angle between c and a
 	x = (a * a + c * c - b * b) / (2 * a * c)
	# if (x > 1.0):
	# 	x = 1

 	return acos(x)

def goToXY(Tx, Ty):
 	#delayMicroseconds(10000)
	sleep(0.005)

 	global O1X, O1Y, L1, L2, L3, rightServo, leftServo, LEFTSERVONULL, RIGHTSERVONULL 

	#calculate triangle between pen, servoLeft and arm joint
  	# cartesian dx/dy
	dx = Tx - O1X
	dy = Ty - O1Y

    #polar lemgth (c) and angle (a1)
	c = sqrt(dx * dx + dy * dy) 
	a1 = atan2(dy, dx)
	a2 = return_angle(L1, L2, c)

	writeMicroseconds(leftServo, floor(((a2 + a1 - pi) * SERVOFAKTOR) + LEFTSERVONULL))

	#calculate joinr arm point for triangle of the right servo arm
	a2 = return_angle(L2, L1, c);
	Hx = Tx + L3 * cos((a1 - a2 + 0.621) + pi) #36,5
	Hy = Ty + L3 * sin((a1 - a2 + 0.621) + pi)

	#calculate triangle between pen joint, servoRight and arm joint
	dx = Hx - O2X
	dy = Hy - O2Y

	c = sqrt(dx * dx + dy * dy)
	a1 = atan2(dy, dx)
	a2 = return_angle(L1, (L2 - L3), c)

	writeMicroseconds(rightServo, floor(((a1 - a2) * SERVOFAKTOR) + RIGHTSERVONULL))

def writeMicroseconds(servo, microseconds):
	"""Calculates duty cycle based on desired pulse width"""
	servo.ChangeDutyCycle(microseconds/200.0)

def delayMicroseconds(microseconds):
	"""Coverts microsecond delay to seconds delay"""
	sleep(microseconds/1000000.0)

def calibrate():
	linePath(-3, 29.2)
  	sleep(0.5)
  	linePath(74.1, 28)
  	sleep(0.5)
# while (1):
# 	weatherGetter = Weather()
# 	temp = weatherGetter.getWeather()
# 	digits = getDigist(temp)
# 	print(digits)
# 	for i in range(1,len(digits)):
# 		drawNum(digits[i])
# 	break;

#test code
# for i in range(0,10):
# 	liftServo.start(500/200.0)
# 	lift(UP)
# 	sleep(1)
# 	lift(WIPE)
# 	sleep(1)
# 	lift(DOWN)
# 	sleep(1)
leftServo.start(leftMicroseconds/200.0)
rightServo.start(rightMicroseconds/200.0)
#sleep(1)
#linePath(5, 5);
# linePath(25.0,25.0)
# arcPath(32.0, 30.0, 10.0, -0.8, 6.7 , 'Counterclockwise')
#calibrate()

drawNum(5, 25, 0)
# drawNum(19,25, 1)
# drawNum(19,25,2)

"""for i in range (0, 1000):
	writeMicroseconds(leftServo, 1500-i)
	writeMicroseconds(rightServo, 1500+i)
	sleep(0.001)

for i in range (0, 1000):
	writeMicroseconds(leftServo, 500+i)
	writeMicroseconds(rightServo, 2500-i)
	sleep(0.001)"""

#leftServo.stop()
#rightServo.stop()

GPIO.cleanup()
