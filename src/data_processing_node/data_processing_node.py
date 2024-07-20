import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class DataProcessingNode(Node):
    def __init__(self):
        super().__init__('data_processing_node')
        self.subscription = self.create_subscription(
            String,
            'esp32_out',
            self.data_callback,
            10)

    def data_callback(self, msg):
        self.get_logger().info(f'Received data: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = DataProcessingNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
