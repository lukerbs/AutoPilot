import pyautogui
import threading
import datetime
import random
import time

pyautogui.FAILSAFE = False


print(datetime.datetime.now().strftime("%H:%M"))
def check_active_status(last_location):
	return pyautogui.position() != last_location

print('--👨🏽‍✈️ AUTOPILOT 👨🏽‍✈️--')
print(f'Start: {datetime.datetime.now().strftime("%H:%M")}')
screen_size = pyautogui.size()
x, y = screen_size[0], screen_size[1]

default_end_time = datetime.time(17,30) # 5:30
if datetime.datetime.now().time() < default_end_time:
	end_time = default_end_time
else:
	# end one hour from now if initiated past end time
	end_time = (datetime.datetime.now() + datetime.timedelta(hours=1)).time() 

while datetime.datetime.now().time() < end_time:
	# move to new position
	x_destination = random.randint(0, x)
	y_destination = random.randint(0, y)
	pyautogui.moveTo(x_destination, y_destination, duration=1)
	time.sleep(random.randint(1,7))

	# wait for 60 seconds if active
	last_location = (x_destination, y_destination)
	active = check_active_status(last_location)
	while active:
		last_location = pyautogui.position()
		time.sleep(60)
		active = check_active_status(last_location)

print(f'Close: {datetime.datetime.now().strftime("%H:%M")}')


