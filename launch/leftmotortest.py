from robot_hat import PWM, Pin
import time

# Manually test the left motor pins
pwm = PWM('P13')       # Left motor PWM
pwm.freq(50)
dir_pin = Pin('D5')     # Left motor DIR

def test_motor(speed):
    if speed > 0:
        dir_pin.value(1)
    else:
        dir_pin.value(0)
        speed = -speed
    pwm.pulse_width_percent(speed)

print("Testing Left motor forward (should spin forward)")
test_motor(50)
time.sleep(2)

print("Testing Left motor reverse")
test_motor(-50)
time.sleep(2)

print("Stopping motor")
test_motor(0)
