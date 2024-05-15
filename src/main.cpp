#include <WiFi.h>
#include <ros.h>
#include <std_msgs/String.h>
#include "esp_camera.h"
#include "MarauderFunctions.h"
#include "MotorControl.h"
#include "LoRaWAN.h"

ros::NodeHandle nh;

void setup()
{
    marauder_setup();
    setup_camera();
    motor_setup();
    setup_lorawan();
    nh.initNode();
    nh.subscribe(motor_command_sub);
}

void loop()
{
    marauder_loop();
    nh.spinOnce();
    os_runloop_once();
    delay(10);
}
