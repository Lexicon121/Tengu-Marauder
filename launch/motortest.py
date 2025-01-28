from robot_hat import Motor

motor0 = Motor(0)  # Initializes Motor 0 (default GPIO pins for Motor 0)
motor0.wheel(100)  # Spin Motor 0 forward

motor1 = Motor(1)  # Initializes Motor 1
motor1.wheel(-100)  # Spin Motor 1 backward
