import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial

class ESP32CommNode(Node):
    def __init__(self):
        super().__init__('esp32_comm_node')
        self.serial_port = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
        self.subscription = self.create_subscription(
            String,
            'esp32_in',
            self.esp32_in_callback,
            10)
        self.publisher = self.create_publisher(String, 'esp32_out', 10)
        self.timer = self.create_timer(0.1, self.read_esp32_data)

    def esp32_in_callback(self, msg):
        self.serial_port.write((msg.data + '\n').encode())

    def read_esp32_data(self):
        if self.serial_port.in_waiting > 0:
            data = self.serial_port.read(self.serial_port.in_waiting).decode().strip()
            self.publisher.publish(String(data=data))

def main(args=None):
    rclpy.init(args=args)
    node = ESP32CommNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
