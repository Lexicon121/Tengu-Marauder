import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class CommandNode(Node):
    def __init__(self):
        super().__init__('command_node')
        self.publisher = self.create_publisher(String, 'esp32_in', 10)
        self.timer = self.create_timer(2.0, self.send_command)

    def send_command(self):
        command = String()
        command.data = 'SCAN'  # Example command to start a WiFi scan
        self.publisher.publish(command)

def main(args=None):
    rclpy.init(args=args)
    node = CommandNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
