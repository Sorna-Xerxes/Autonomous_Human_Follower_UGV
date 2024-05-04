import serial
import time

def request_imu():
    try:
        stm32.write(bytearray([0x03]))  # Send packet
        time.sleep(0.1)
        return stm32.readline().decode("utf-8")  # Read response
    except serial.SerialException as e:
        print("Error reading from serial port:", e)
        return None

port_name = "/dev/ttyACM0"
try:
    stm32 = serial.Serial(port_name, 9600, timeout=1)
except serial.SerialException as e:
    print("Error opening serial port:", e)
    exit(1)

while True:
    raw_data = request_imu()
    if raw_data:
        data = raw_data.lstrip('\x00').rstrip('\r\n')
        data_list = data.split(',')

        try:
            # Assuming the first three values are accelerometer readings and the next three are gyroscope readings
            accel_values = [float(value) for value in data_list[:3]]
            gyro_values = [float(value) for value in data_list[3:]]

            print("Accelerometer readings = X: {}, Y: {}, Z: {}".format(*accel_values))
            print("Gyroscope readings = X: {}, Y: {}, Z: {}".format(*gyro_values))
        except ValueError as e:
            print("Error converting data to float:", e)
    else:
        print("Failed to read data from STM32.")
