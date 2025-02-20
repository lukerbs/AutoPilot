import pyautogui
import threading
import datetime
import random
import time

pyautogui.FAILSAFE = False

print(datetime.datetime.now().strftime("%H:%M"))


def check_active_status(last_location):
    return pyautogui.position() != last_location


print("--👨🏽‍✈️ AUTOPILOT 👨🏽‍✈️--")
print(f'Start: {datetime.datetime.now().strftime("%H:%M")}')
screen_size = pyautogui.size()
x, y = screen_size[0], screen_size[1]

default_end_time = datetime.time(17, 30)  # 5:30
if datetime.datetime.now().time() < default_end_time:
    end_time = default_end_time
else:
    # end one hour from now if initiated past end time
    end_time = (datetime.datetime.now() + datetime.timedelta(hours=1)).time()

# Initial direction
x_direction = 1  # 1 for right, -1 for left
y_direction = 1  # 1 for down, -1 for up
x_pos = random.randint(0, x)
y_pos = random.randint(0, y)
move_speed = 50  # pixels per movement

while datetime.datetime.now().time() < end_time:
    # Update position
    x_pos += move_speed * x_direction
    y_pos += move_speed * y_direction

    # Check for collisions with screen edges
    if x_pos >= x:
        x_pos = x
        x_direction = -1
    elif x_pos <= 0:
        x_pos = 0
        x_direction = 1

    if y_pos >= y:
        y_pos = y
        y_direction = -1
    elif y_pos <= 0:
        y_pos = 0
        y_direction = 1

    # Move cursor
    pyautogui.moveTo(x_pos, y_pos, duration=0.001)

    # Check if user is moving mouse
    last_location = (x_pos, y_pos)
    active = check_active_status(last_location)
    while active:
        last_location = pyautogui.position()
        time.sleep(1)
        active = check_active_status(last_location)
        if not active:
            x_pos, y_pos = last_location

print(f'Close: {datetime.datetime.now().strftime("%H:%M")}')
