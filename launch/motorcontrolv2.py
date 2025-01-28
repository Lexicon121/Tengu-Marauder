import sys
import termios
import tty
from robot_hat import Motor, PWM, Pin

# Initialize motor objects for the two-wheeled robot
motor_right = Motor(PWM('P13'), Pin('D4'))  # Right motor (PWM on P13, direction on D4)
motor_left = Motor(PWM('P12'), Pin('D5'))   # Left motor (PWM on P12, direction on D5)

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
    motor_right.speed(50)  # Right motor forward at 50% speed
    motor_left.speed(50)   # Left motor forward at 50% speed

def move_backward():
    print("Moving backward")
    motor_right.speed(-50)  # Right motor backward at 50% speed
    motor_left.speed(-50)   # Left motor backward at 50% speed

def turn_left():
    print("Turning left")
    motor_right.speed(50)   # Right motor forward at 50% speed
    motor_left.speed(-50)   # Left motor backward at 50% speed

def turn_right():
    print("Turning right")
    motor_right.speed(-50)  # Right motor backward at 50% speed
    motor_left.speed(50)    # Left motor forward at 50% speed

def stop_motors():
    print("Stopping motors")
    motor_right.speed(0)  # Stop Right motor
    motor_left.speed(0)   # Stop Left motor

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
