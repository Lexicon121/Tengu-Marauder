import sys
import termios
import tty
from robot_hat import Motor, Pin, PWM

# Initialize PWM objects for the motors
pwm_right = PWM("P1")  # PWM for the right motor
pwm_left = PWM("P2")   # PWM for the left motor

# Set initial PWM frequency (e.g., 50 Hz)
pwm_right.freq(50)
pwm_left.freq(50)

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
    pwm_right.pulse_width_percent(75)  # Right motor forward at 75% speed
    pwm_left.pulse_width_percent(75)   # Left motor forward at 75% speed

def move_backward():
    print("Moving backward")
    pwm_right.pulse_width_percent(25)  # Right motor backward at 25% speed
    pwm_left.pulse_width_percent(25)   # Left motor backward at 25% speed

def turn_left():
    print("Turning left")
    pwm_right.pulse_width_percent(75)  # Right motor forward at 75% speed
    pwm_left.pulse_width_percent(25)   # Left motor backward at 25% speed

def turn_right():
    print("Turning right")
    pwm_right.pulse_width_percent(25)  # Right motor backward at 25% speed
    pwm_left.pulse_width_percent(75)   # Left motor forward at 75% speed

def stop_motors():
    print("Stopping motors")
    pwm_right.pulse_width_percent(0)  # Stop the right motor
    pwm_left.pulse_width_percent(0)   # Stop the left motor

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
