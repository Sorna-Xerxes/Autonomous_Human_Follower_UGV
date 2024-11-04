# Multi-Sensory Fusion for Autonomous Camera Control and Navigation

## ABSTRACT
**Task 1,** a Python script leveraging computer vision techniques and OpenCV library will be developed to detect humans within a camera's view. A control loop will then adjust the camera orientation to keep the human centrally located in the frame.

**Task 2** involves writing firmware for an STM32 microcontroller board to collect IMU data and correct any camera misalignment caused by robot movement or environmental factors. Sensor fusion algorithms will be implemented to enhance tracking accuracy.

**Task 3** focuses on integrating a Visual-Inertial Odometry (VIO) system to improve the robot's spatial awareness and movement accuracy. This involves fusing visual information from cameras with inertial data from IMUs, enabling precise navigation and mapping without GPS.

The project outcomes include gaining proficiency in implementing computer vision algorithms, developing real-time firmware for microcontrollers, applying sensor fusion algorithms, and understanding Visual-Inertial Odometry principles. Soft skills such as problem-solving, project management, teamwork, and communication will also be enhanced throughout the project.

Overall, this project seeks to advance the capabilities of autonomous systems in dynamic environments through the integration of multiple sensory inputs for robust navigation and control.

## SYSTEM OVERVIEW
The following **block diagram** illustrates the system architecture and data flow between the components:

![image](https://github.com/user-attachments/assets/b70b8875-493a-4d55-9569-f327590ae4d2)

### Hardware Requirements:
- STM32 F3 Discovery
- Jetson Nano
- Camera - Raspberry Pi
- Servo Motors x 2 (180°)
- Pan-Tilt Camera Mount
- Ethernet Cable
- Power Supply Adapter (5V)
- USB Cable

### STM32 Cube IDE figurtions:
![image](https://github.com/user-attachments/assets/1edb2786-5adc-478e-a4d0-8a8df31c877e)

![Task 1 printout](https://github.com/user-attachments/assets/27d47c7b-5fde-479e-8fb3-9a83fcd615ce)

### VSCode Requirements:
![image](https://github.com/user-attachments/assets/62aafecf-deaa-40bf-80b6-8efa85828417)

### Python programming algorithm:
![python programming methodology_page-0001](https://github.com/user-attachments/assets/bd274363-8dd0-43e6-8fe4-92e57328f67f)

### Output:
![Task1](https://github.com/user-attachments/assets/e20d1e41-4637-4e66-804e-3fe6f59beed7)


## INSTRUCTIONS
To run the code:

### STM32 Firmware:
- Import the provided STM32 project file Project_Gyro.zip into STM32CubeIDE. (Unarchive it into the STM32 Workspace before importing).
- All necessary project configurations, such as enabling USB communication and integrating the gyroscope sensor, have already been pre-configured. These settings encompass connectivity interfaces (SPI, I2C), clock configurations, baud rates (9600), etc.
- Flash the firmware onto the STM32 development board using STM32CubeIDE.
  
![STM32_Printout_ _Configurations](https://github.com/Sorna-Xerxes/Jetson-Nano-RxTx-Gyro-from-STM32-with-LED/assets/147555989/96b94cbe-d52a-43ed-8354-0e616d482035)

  
### Jetson Nano Connection with Visual Code:

- **Jetson Nano runs headless:** It operates without a monitor, keyboard, or mouse.
- **Configure network for SSH access:** Adjust network settings to connect to Jetson Nano remotely.
- **Use Visual Studio Code to manage port gateway:** VS Code sets up communication with Jetson Nano.Ensure that Python 3 is installed on Visual Code. Install the necessary dependencies by running the following command in the terminal:

Install pySerial on Jetson Nano
```bash
unzip pyserial-master.zip
cd pyserial-master
sudo python3 setup.py install
```
- **Setup Communication Device Class on STM32:**
Once connected figure out the address of the STM32, this can be done by running the following command in the terminal:
```bash
ls /dev/ttyA*
```
   set the access permissions on the device’s address by running the following, remembering to replace with the device’s address.
```bash
sudo chmod 666 /dev/ttyACM0
```
## PYTHON SCRIPT LOGIC
The `VS Code - X,Y,Z LED Logic (Final).py` provides real-time indication of the roll, pitch and yaw angles of the STM32 development board through the onboard LEDs. As the orientation of the board changes, the LEDs adjust accordingly to reflect the current roll and pitch angles. This visual feedback allows users to monitor the orientation of the device and make informed decisions based on its position

- **Request Gyro data**: print X,Y,Z of Previous posiiton, Current Position
- **Parsing Gyro Data**: calculates its difference
- **LED Logic**:
```
x_diff is > 5000, it's a "Pitch Down" movement. (LED 4)
x_diff is < -5000, it's a "Pitch Up" movement. (LED 0)
y_diff is > 20000, it's a "Roll West" movement (LED 6)
y_diff is < -20000, it's a "Roll East" movement. (LED 2)
```
## OUTCOME
The STM32 Roll, Pitch and Yaw Indicator project demonstrates the integration of gyroscopic data sensing and LED control to create a practical orientation indicator system. The project showcases the capabilities of microcontroller-based systems for sensor integration and real-time data processing. Additionally, the project serves as a foundation for further exploration into embedded systems development and sensor-based applications.

## DEPENDENCIES

- **PySerial:** It is a Python library used for serial communication. It provides support for accessing serial ports and communication with serial devices. Install PySerial using the following command:
```bash
pip install pyserial
```
- **re:** The regular expression module in Python, utilized for pattern matching with regular expressions. In this context, it's employed to `extract x, y, and z coordinates from gyro data`.

- **time:** Python's standard library module offering various time-related functions. Within the code, it `introduces delays between operations`, preventing the code from executing too rapidly and potentially overloading the connected device.

## TABLE OF CONTENTS

| File Name        | Brief           |
| ------------- |:-------------:|
| Project_Gyro_LED.zip      | Contains the entire STM32 project that is to be flashed onto the STM32 |
| VS Code - 4 LED Logic      | Contains the Python script with 4 LED Logic that is to be run in VS Code after setting up the connection      |
| pyserial-master.zip      | Install pySerial on Jetson Nano      |
|  VS Code - 8 LED Logic      | Contains the Python code with 8 LED logic where the code can be improvised with data parsing or improvising using data fusion      |

## CREDITS
The STM32F3 discovery board and Jetson Nano were provided as part of the project materials for the completion of our coursework in Embedded Systems for the MSc in Robotics, AI, and Autonomous Systems at City, University of London.

## CONTRIBUTIONS ARE WELCOMED
Contributions to this project are highly appreciated. To contribute:
- Fork the repository.
- Make your changes or enhancements.
- Submit a pull request for review.
