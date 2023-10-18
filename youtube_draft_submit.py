import mouse
import os
import time
def click_left():
	os.system("xdotool click 1")

def move_and_left_click(x,y):
	mouse.move(x,y,duration = 1.0)
	os.system("xdotool click 1")
	time.sleep(1)

def move_only(x,y):
	mouse.move(x,y,duration = 1.0)
	time.sleep(1)

x = 476
y = 452

while True:
	for i in range(0,8):
		# Click on Title
		move_and_left_click(x,y)

		#Click Next
		move_and_left_click(1400,1004)

		#Click Not for Kids
		move_and_left_click(659,796)

		#Click Next
		move_and_left_click(1400,1004)

		#Click Next
		move_and_left_click(1400,1004)

		#Click Next
		move_and_left_click(1400,1004)

		#Click Unlisted
		move_and_left_click(594,522)

		#Click Next
		move_and_left_click(1400,1004)
		time.sleep(3)

		#Click Close
		move_and_left_click(1171,793)

		y+=80

	# Refresh Page
	move_and_left_click(87,89)
	time.sleep(5)
	x = 476
	y = 452