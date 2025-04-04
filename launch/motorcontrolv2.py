import sys
import termios
import tty
from robot_hat import Motor, PWM, Pin

# Correct motor assignments
motor_right = Motor(PWM('P12'), Pin('D4'))  # Right motor
motor_left = Motor(PWM('P13'), Pin('D5'))   # Left motor (needs speed inversion)

def get_key():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

# Movement functions with left motor inverted
def move_forward():
    print("TEST: Right motor only (forward)")
    motor_right.speed(50)
    motor_left.speed(-50)


def move_backward():
    print("Moving backward")
    motor_right.speed(-50)
    motor_left.speed(50)   # Inverted to move backward

def turn_left():
    print("Turning left")
    motor_right.speed(50)
    motor_left.speed(50)   # Inverted, so this turns left

def turn_right():
    print("Turning right")
    motor_right.speed(-50)
    motor_left.speed(-50)  # Inverted, so this turns right

def stop_motors():
    print("Stopping motors")
    motor_right.speed(0)
    motor_left.speed(0)

stop_motors()

print("Press 'W' to move forward, 'S' to move backward, 'A' to turn left, 'D' to turn right, 'Space' to stop. Press 'Q' to quit.")
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
