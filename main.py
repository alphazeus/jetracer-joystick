from nvidia_racecar import NvidiaRacecar
import time
import curses

print("Initializing I2C Communication...")
car = NvidiaRacecar()
print("Initialization Complete!")

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

car_throttle_value = 0.6

try:
	while True:
		char = screen.getch()
		if char ==ord('q'):
			break

		if char ==ord('h'):
			car.steering = 1
			car.throttle = 0
		elif char ==ord('k'):
			car.steering = -1
			car.throttle = 0
		elif char ==ord('j'):
			car.steering = 0
			car.throttle = 0
		elif char ==ord('u'):
			car.steering = 0
			car.throttle = car_throttle_value
		elif char ==ord('m'):
			car.steering = 0
			car.throttle = -car_throttle_value
		elif char ==ord('y'):
			car.steering = 1
			car.throttle = car_throttle_value
		elif char ==ord('i'):
			car.steering = -1
			car.throttle = car_throttle_value
		elif char ==ord('n'):
			car.steering = 1
			car.throttle = -car_throttle_value
		elif char ==ord(','):
			car.steering = -1
			car.throttle = -car_throttle_value
		else:
			car.throttle = 0
			car.steering = 0

		
finally:
	curses.nocbreak()
	screen.keypad(0)
	curses.echo()
	curses.endwin()

