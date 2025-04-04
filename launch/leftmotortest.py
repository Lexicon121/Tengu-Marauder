from robot_hat import PWM, Pin
import time

pwm = PWM('P13')       # Left motor PWM
pwm.freq(50)
dir_pin = Pin('D5')     # Left motor DIR

def test_left_motor(direction):
    if direction == 'forward':
        dir_pin.value(1)
        print("DIR set to HIGH (forward)")
    else:
        dir_pin.value(0)
        print("DIR set to LOW (reverse)")
    pwm.pulse_width_percent(50)

print("Left motor: FORWARD")
test_left_motor('forward')
time.sleep(3)

print("Left motor: REVERSE")
test_left_motor('reverse')
time.sleep(3)

print("STOP")
pwm.pulse_width_percent(0)
