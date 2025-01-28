from robot_hat import Motor, PWM, Pin
from time import sleep

# Initialize motors
motor_right = Motor(PWM('P13'), Pin('D4'))  # Right motor (PWM on P13, direction on D4)
motor_left = Motor(PWM('P12'), Pin('D5'))   # Left motor (PWM on P12, direction on D5)

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
    motor_right.speed(0)  # Stop right motor
    motor_left.speed(0)   # Stop left motor

# Main loop to listen for key presses
try:
    while True:
        command = input("Enter command ('w'=forward, 's'=backward, 'a'=left, 'd'=right, 'space'=stop, 'q'=quit): ").lower()
        if command == 'w':
            move_forward()
        elif command == 's':
            move_backward()
        elif command == 'a':
            turn_left()
        elif command == 'd':
            turn_right()
        elif command == ' ':
            stop_motors()
        elif command == 'q':
            break
        else:
            print("Invalid command. Try again.")
finally:
    stop_motors()
    print("Program terminated.")
