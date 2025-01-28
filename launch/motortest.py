from robot_hat import Pin
import time

# Initialize pins for the left and right motors
left_motor = Pin("D4")   # Left motor pin
right_motor = Pin("D5")  # Right motor pin

# Function to control motors
def move_forward():
    print("Moving forward")
    left_motor.value(1)  # Set left motor to high
    right_motor.value(1) # Set right motor to high

def move_backward():
    print("Moving backward")
    left_motor.value(0)  # Set left motor to low (reverse, if supported)
    right_motor.value(0) # Set right motor to low

def stop_motors():
    print("Stopping motors")
    left_motor.value(0)  # Stop left motor
    right_motor.value(0) # Stop right motor

# Test the motors
print("Testing motors...")
move_forward()
time.sleep(2)  # Run forward for 2 seconds
stop_motors()
time.sleep(1)

move_backward()
time.sleep(2)  # Run backward for 2 seconds
stop_motors()
print("Test complete!")
