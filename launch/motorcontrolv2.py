import sys
import termios
import tty
from robot_hat import Motor, Pin

# Initialize motor objects for the two-wheeled robot
motor_right = Motor(pwm=Pin("D5"), dir=Pin("D6"))  # Right motor
motor_left = Motor(pwm=Pin("D4"), dir=Pin("D7"))   # Left motor

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

# Control functions for the two-wheeled robot
def move_forward():
    print("Moving forward")
    motor_right.wheel(100)  # Right motor forward
    motor_left.wheel(100)   # Left motor forward

def move_backward():
    print("Moving backward")
    motor_right.wheel(-100)  # Right motor backward
    motor_left.wheel(-100)   # Left motor backward

def turn_left():
    print("Turning left")
    motor_right.wheel(100)   # Right motor forward
    motor_left.wheel(-100)   # Left motor backward

def turn_right():
    print("Turning right")
    motor_right.wheel(-100)  # Right motor backward
    motor_left.wheel(100)    # Left motor forward

def stop_motors():
    print("Stopping motors")
    motor_right.wheel(0)  # Stop right motor
    motor_left.wheel(0)   # Stop left motor

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
