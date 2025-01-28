from robot_hat import Motor

motor = Motor(pwm=PWM("P1"), dir=Pin("D6"))  # Adjust pins as needed
motor.wheel(100, 0)  # Move motor 0 forward at full speed
