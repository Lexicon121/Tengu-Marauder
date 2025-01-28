from robot_hat import PWM, Pin, Motor

# Initialize PWM for the motor (adjust "P1" for the correct pin)
pwm = PWM("P1")  # PWM for motor speed control
pwm.freq(50)     # Set PWM frequency to 50 Hz

# Initialize direction control for the motor
direction_pin = Pin("D6")  # Direction control pin

# Function to set motor speed and direction
def set_motor(speed):
    if speed > 0:
        direction_pin.value(1)  # Set direction to forward
    elif speed < 0:
        direction_pin.value(0)  # Set direction to reverse
        speed = -speed  # Use positive value for PWM

    pwm.pulse_width_percent(speed)  # Set speed as a percentage (0-100)

# Motor Test
print("Starting motor test...")
try:
    print("Moving forward at 50% speed")
    set_motor(50)  # Forward at 50% speed
    input("Press Enter to continue...")

    print("Moving backward at 75% speed")
    set_motor(-75)  # Backward at 75% speed
    input("Press Enter to stop the motor...")

    print("Stopping motor")
    set_motor(0)  # Stop the motor
except KeyboardInterrupt:
    print("Test interrupted")
    set_motor(0)  # Ensure motor stops on exit
