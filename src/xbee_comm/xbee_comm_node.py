import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial

class XbeeCommNode(Node):
    def __init__(self):
        super().__init__('xbee_comm_node')
        self.serial_port = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)  # Adjust the port as needed
        self.publisher_cmd_vel = self.create_publisher(String, 'cmd_vel', 10)
        self.publisher_esp32 = self.create_publisher(String, 'esp32_in', 10)
        self.timer = self.create_timer(0.1, self.read_xbee_data)

    def read_xbee_data(self):
        if self.serial_port.in_waiting > 0:
            data = self.serial_port.readline().decode().strip()
            self.process_command(data)

    def process_command(self, command):
        if command in ['F', 'B', 'L', 'R', 'S']:
            self.publisher_cmd_vel.publish(String(data=command))
        elif command in ['SCAN', 'DEAUTH']:
            self.publisher_esp32.publish(String(data=command))

def main(args=None):
    rclpy.init(args=args)
    node = XbeeCommNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
