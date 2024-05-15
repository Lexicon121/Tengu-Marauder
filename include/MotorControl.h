#ifndef MOTOR_CONTROL_H
#define MOTOR_CONTROL_H

void motor_setup();
void motor_command_callback(const std_msgs::String &cmd);

#endif // MOTOR_CONTROL_H
