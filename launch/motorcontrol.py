import sys
import termios
import tty
from robot_hat import Motor

# Initialize the motor object
motor = Motor()

# Function to get keyboard input
def get_key():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

# Control functions for a two-wheeled robot
def move_forward():
    print("Moving forward")
    motor.wheel(100, 0)  # Right motor forward (motor number 0)
    motor.wheel(100, 1)  # Left motor forward (motor number 1)

def move_backward():
    print("Moving backward")
    motor.wheel(-100, 0)  # Right motor backward (motor number 0)
    motor.wheel(-100, 1)  # Left motor backward (motor number 1)

def turn_left():
    print("Turning left")
    motor.wheel(-100, 0)  # Right motor backward (motor number 0)
    motor.wheel(100, 1)   # Left motor forward (motor number 1)

def turn_right():
    print("Turning right")
    motor.wheel(100, 0)  # Right motor forward (motor number 0)
    motor.wheel(-100, 1) # Left motor backward (motor number 1)

def stop_motors():
    print("Stopping motors")
    motor.wheel(0, 0)  # Stop Right motor (motor number 0)
    motor.wheel(0, 1)  # Stop Left motor (motor number 1)

# Start with motors stopped
stop_motors()

# Main loop to listen for key presses
print("Press 'W' to move forward, 'S' to move backward, 'A' to turn left, 'D' to turn right, and 'Space' to stop. Press 'Q' to quit.")
try:
    while True:
        key = get_key()
        if key == 'w':
            move_forward()
        elif key == 's':
            move_backward()
        elif key == 'a':
            turn_left()
        elif key == 'd':
            turn_right()
        elif key == ' ':
            stop_motors()
        elif key == 'q':
            break
        else:
            stop_motors()
finally:
    stop_motors()
    print("Program terminated.")
