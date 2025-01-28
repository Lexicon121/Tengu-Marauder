import sys
import termios
import tty
from robot_hat import Motor, Pin, PWM

# Initialize motor objects for the two-wheeled robot
motor_right = Motor(pwm=PWM("P1"), dir=Pin("D6"))  # Right motor
motor_left = Motor(pwm=PWM("P2"), dir=Pin("D7"))   # Left motor

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
    motor_right.set_speed(100)  # Right motor forward at speed 100
    motor_left.set_speed(100)   # Left motor forward at speed 100

def move_backward():
    print("Moving backward")
    motor_right.set_speed(-100)  # Right motor backward at speed 100
    motor_left.set_speed(-100)   # Left motor backward at speed 100

def turn_left():
    print("Turning left")
    motor_right.set_speed(100)   # Right motor forward at speed 100
    motor_left.set_speed(-100)   # Left motor backward at speed 100

def turn_right():
    print("Turning right")
    motor_right.set_speed(-100)  # Right motor backward at speed 100
    motor_left.set_speed(100)    # Left motor forward at speed 100

def stop_motors():
    print("Stopping motors")
    motor_right.set_speed(0)  # Stop right motor
    motor_left.set_speed(0)   # Stop left motor

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
