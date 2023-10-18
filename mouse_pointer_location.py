import mouse
import time
mouse.move(150, 150)
while True:
	pos = mouse.get_position()
	print(pos)
	time.sleep(1)