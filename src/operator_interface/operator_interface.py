import serial

def send_command(command):
    with serial.Serial('/dev/ttyUSB2', 9600) as ser:
        ser.write(command.encode())
        response = ser.readline().decode()
        print('Response:', response)

if __name__ == '__main__':
    while True:
        command = input('Enter command: ')
        send_command(command)
