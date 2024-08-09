# Tengu Marauder

Tengu Marauder is a versatile ROS2-based robotic platform integrated with ESP32 for advanced communication and control functionalities. This project leverages XBee modules for wireless communication and provides a modular framework for various robotic components, including motor control, data processing, and operator interfaces.

## Features
- **Motor Control**: Manage and control the motors of the robotic platform.
- **XBee Communication**: Wireless communication using XBee modules.
- **ESP32 Integration**: Interface with ESP32 for additional functionalities.
- **Data Processing**: Handle and process sensor data.
- **Operator Interface**: Interface for manual control and monitoring.

## Installation

## Reccommended
- **Motor Test**: Test motor function with motorcontrol.py under launch

### Prerequisites
- **ROS2 Humble**: Ensure you have ROS2 Humble installed.
- **Python 3**: Make sure Python 3 is installed.
- **djitellopy**: We were testing this on a DJI Tello with the dji tello py library pip install djitellopy

### Steps
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/Tengu-Marauder.git
    cd Tengu-Marauder
    ```

2. **Setup ROS2 Workspace**:
    ```bash
    mkdir -p ~/ros2_ws/src
    cd ~/ros2_ws/src
    ln -s ~/path_to_cloned_repo/Tengu-Marauder .
    cd ~/ros2_ws
    colcon build
    source install/setup.bash
    ```

3. **Install Python Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Launching the Nodes
To launch the Tengu Marauder system, use the provided launch file:
```bash;
ros2 launch tengu_marauder tengu_marauder_launch.py

Running Individual Nodes
You can also run individual nodes separately for testing:

ros2 run motor_control motor_control_node
ros2 run xbee_comm xbee_comm_node
```

## Bill of Materials:
- **Raspberry Pi 4**
- **2x ttmotors**
- **SunFounder Raspberry Pi Motor Hat**
- **3D Printed Parts**
    1. Outershell
    2. Undershell
    3. Wheels
    4. Back wheel




