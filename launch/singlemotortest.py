from robot_hat import PWM, Pin

# Ask user for PWM and direction pins
pwm_pin_input = input("Enter the PWM pin (e.g., P12, P13): ").strip().upper()
dir_pin_input = input("Enter the direction pin (e.g., D4, D5, D6): ").strip().upper()

# Initialize motor pins
try:
    pwm = PWM(pwm_pin_input)
    pwm.freq(50)
    direction_pin = Pin(dir_pin_input)
except Exception as e:
    print(f"Error initializing pins: {e}")
    exit(1)

# Function to set motor speed and direction
def set_motor(speed):
    if speed > 0:
        direction_pin.value(1)  # Forward
    elif speed < 0:
        direction_pin.value(0)  # Reverse
        speed = -speed
    else:
        speed = 0  # Stop

    pwm.pulse_width_percent(speed)

# Motor Test
print(f"Starting motor test on PWM: {pwm_pin_input}, DIR: {dir_pin_input}...")
try:
    print("Moving forward at 50% speed")
    set_motor(50)
    input("Press Enter to continue...")

    print("Moving backward at 75% speed")
    set_motor(-75)
    input("Press Enter to stop the motor...")

    print("Stopping motor")
    set_motor(0)
except KeyboardInterrupt:
    print("Test interrupted")
    set_motor(0)
