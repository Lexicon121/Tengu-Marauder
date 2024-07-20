import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from some_motor_driver_library import MotorDriver  # Replace with actual motor driver library

class MotorControlNode(Node):
    def __init__(self):
        super().__init__('motor_control_node')
        self.subscription = self.create_subscription(
            String,
            'cmd_vel',
            self.cmd_vel_callback,
            10)
        self.motor_driver = MotorDriver()  # Initialize motor driver

    def cmd_vel_callback(self, msg):
        command = msg.data
        if command == 'F':
            self.motor_driver.move_forward()
        elif command == 'B':
            self.motor_driver.move_backward()
        elif command == 'L':
            self.motor_driver.turn_left()
        elif command == 'R':
            self.motor_driver.turn_right()
        elif command == 'S':
            self.motor_driver.stop()

def main(args=None):
    rclpy.init(args=args)
    node = MotorControlNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
