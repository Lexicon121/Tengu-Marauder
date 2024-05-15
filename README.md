# Tengu Marauder

![Tengu Marauder Image](https://i.imgur.com/9w0ZMyg.gif)

## Features

- **Multi-Terrain Movement:** Navigate through diverse terrains with ease.
- **Wireless Testing:** Advanced tools and capabilities for thorough wireless testing.
- **Autonomous Operation:** Set it and forget it – the Tengu Marauder operates autonomously, ensuring thorough testing without constant oversight.
- **Integration with Strix Interceptor:** Designed to work seamlessly with the Strix Interceptor for enhanced capabilities.

## Installation

## Features

- WiFi scanning and attacks using ESP32 Marauder
- Camera streaming using ESP32-CAM
- Differential drive control for a two-wheeled robot
- Communication via LoRaWAN or Zigbee

## Directory Structure

- `include/`: Header files for different functionalities.
- `src/`: Source files for implementation.
- `lib/`: External libraries for LoRaWAN and Zigbee.
- `README.md`: Project documentation.
- `platformio.ini`: PlatformIO configuration file.
- `CMakeLists.txt`: CMake configuration file.

## Setup

1. Install [PlatformIO](https://platformio.org/) for your preferred IDE.
2. Clone this repository:
    ```sh
    git clone https://github.com/yourusername/Tengu-Marauder.git
    cd Tengu-Marauder
    ```
3. Build and upload the firmware to your ESP32 board:
    ```sh
    pio run --target upload
    ```

## Configuration

Configure your WiFi, ROS, and communication settings in the `platformio.ini` and header files.

## Usage

- Run the micro-ROS agent on your PC:
    ```sh
    ros2 run micro_ros_agent micro_ros_agent udp4 --port 8888
    ```

- Power on or reset your ESP32. It should connect to the micro-ROS agent and start streaming camera data and performing network security tasks.
