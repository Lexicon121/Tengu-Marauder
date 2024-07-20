from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='esp32_comm',
            executable='esp32_comm_node',
            name='esp32_comm_node'
        ),
        Node(
            package='motor_control',
            executable='motor_control_node',
            name='motor_control_node'
        ),
        Node(
            package='xbee_comm',
            executable='xbee_comm_node',
            name='xbee_comm_node'
        ),
        Node(
            package='command_node',
            executable='command_node',
            name='command_node'
        ),
        Node(
            package='data_processing_node',
            executable='data_processing_node',
            name='data_processing_node'
        ),
    ])
