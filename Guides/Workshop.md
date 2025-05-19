# Getting Started with Drone Security Using the Tengu Marauder and DJI Tello

This guide walks you through setting up a drone cybersecurity test environment using the Tengu Marauder and the DJI Tello drone. This is intended for educational and ethical security research purposes only.

---

## Requirements

### Hardware

* **DJI Tello Drone**
* **ESP32-S2/S3 Board** (For Tengu Marauder)
* **Raspberry Pi 4** or **Jetson Nano** (optional, for video stream analysis)
* **USB Wi-Fi Adapter** (supports monitor mode and packet injection; e.g., Alfa AWUS036ACH)
* **Power bank** (for mobile ESP32 deployment)

### Software

* **Tengu Marauder** firmware (based on ESP32 Marauder)
* **Python 3.8+**
* **djitellopy** (Python SDK for Tello)
* **Wireshark**
* **Scapy** (for packet analysis and spoofing)
* **Linux OS or Kali Linux** recommended

---

## Step 1: Flashing Tengu Marauder to ESP32

1. Clone the repository:

   ```bash
   git clone https://github.com/ExMachinaParlor/Tengu-Marauder.git
   cd Tengu-Marauder
   ```

2. Install the ESP32 board drivers and `esptool.py`:

   ```bash
   pip install esptool
   ```

3. Put your ESP32 into bootloader mode and flash the firmware:

   ```bash
   esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 firmware.bin
   ```

4. Connect to the ESP32 Wi-Fi access point to access the web interface.

---

## Step 2: Interfacing with the DJI Tello

1. Install `djitellopy`:

   ```bash
   pip install djitellopy
   ```

2. Connect your computer to the Tello Wi-Fi network (`TELLO-XXXXXX`).

3. Create a simple Python control script:

   ```python
   from djitellopy import Tello

   tello = Tello()
   tello.connect()

   print(f"Battery: {tello.get_battery()}%")
   tello.takeoff()
   tello.move_up(50)
   tello.land()
   ```

4. Extend the script to record logs or stream video:

   ```python
   tello.streamon()
   frame_read = tello.get_frame_read()
   frame = frame_read.frame
   # Add OpenCV processing here
   ```

---

## Step 3: Wi-Fi Reconnaissance with Tengu Marauder

1. Boot the Tengu Marauder and access the web terminal.
2. Use the scan command to identify the Tello drone:

   ```bash
   scan
   ```
3. Note the MAC address and channel of the drone.
4. Optionally use the ESP32 to deauth (educational only):

   ```bash
   deauth MAC_ADDRESS CHANNEL
   ```

---

## Step 4: Packet Capture and Analysis

1. Use your USB Wi-Fi adapter to monitor the drone's traffic:

   ```bash
   sudo airmon-ng start wlan0
   sudo airodump-ng wlan0mon --bssid TELLO_MAC --channel CHANNEL
   ```
2. Use Wireshark to open `.cap` files and analyze:

   * Look for unencrypted telemetry.
   * Identify commands sent via UDP.

---

## Step 5: Optional Security Hardening Testing

* Simulate MITM or rogue APs with `hostapd`
* Test resilience to MAC spoofing
* Evaluate effectiveness of encrypted comms (custom firmware required)

---

## References

* [Tengu Marauder GitHub](https://github.com/ExMachinaParlor/Tengu-Marauder)
* [DJI Tello SDK](https://dl-cdn.ryzerobotics.com/downloads/Tello/20210114/Tello_SDK_2.0_User_Guide.pdf)
* [djitellopy GitHub](https://github.com/damiafuentes/DJITelloPy)
* [Wireshark](https://www.wireshark.org/)
* [ESP32 Marauder](https://github.com/justcallmekoko/ESP32Marauder)
* [NIST SP 800-183](https://csrc.nist.gov/publications/detail/sp/800-183/final)
* [NIST IR 8259 & 8260 Series](https://www.nist.gov/publications)
* [DHS Best Practices for Securing UAS](https://www.cisa.gov/sites/default/files/publications/securing_unmanned_aircraft_systems.pdf)
* [RTCA DO-326A/DO-356A](https://www.rtca.org/standards-committees/)
* [DroneSploit](https://github.com/EntySec/DroneSploit)
* [Skyjack](https://github.com/samyk/skyjack)
* [Aircrack-ng](https://www.aircrack-ng.org/)
* [Kismet](https://www.kismetwireless.net/)
* [UAVCAN Tools](https://github.com/UAVCAN)
* [IEEE: UAV Cybersecurity](https://ieeexplore.ieee.org/document/8711226)
* [ACM: Drone Security Survey](https://dl.acm.org/doi/10.1145/3386364)
* [MAVSec Paper](https://www.ndss-symposium.org/ndss-paper/mavsec-securing-mavlink-communication-via-lightweight-cryptography/)
* [Journal of Network and Computer Applications UAV Cybersecurity](https://www.sciencedirect.com/science/article/pii/S1084804520302733)
* [Drone Security Project](https://drone-security.org/)
* [PX4 Discuss Forum](https://discuss.px4.io/)
* [MAVSDK GitHub](https://github.com/mavlink/MAVSDK)
* [Aerospace Village – DEF CON](https://aerospacevillage.org/)
* [Drone Security by David Michel](https://www.routledge.com/Drone-Security-Safeguarding-UAVs-from-Cyberattack/Michel/p/book/9780367334031)
* [RAND – UAS Security](https://www.rand.org/topics/unmanned-aerial-vehicles.html)
* [FAA UAS Cybersecurity](https://www.faa.gov/uas)

Need help setting this up or creating a workshop around it? Feel free to reach out!
