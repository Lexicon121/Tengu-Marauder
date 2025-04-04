import time
from robot_hat import Motor, PWM, Pin

motor_right = Motor(PWM('P12'), Pin('D4'))
motor_left  = Motor(PWM('P13'), Pin('D5'))

print("Right motor FORWARD, left motor FORWARD (with inversion)")
motor_right.speed(50)
motor_left.speed(50)
time.sleep(3)

print("STOP")
motor_right.speed(0)
motor_left.speed(0)
