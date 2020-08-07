# Some fun Projects with Ryze Tello 

Goal is to learn ROS, practice sensor fusion, comms and implement Computer vision.
End Product should be a Docker Img, packages:

## Tello-IMU control:
- Invensense MPU 6050
- Arduino Uno
- Ubuntu w Tellopy

## Hardware:
- MPU6050
- Arduino compatible microcontrollers. (Tested on Uno)
- DJI/Ryze Tello

## Dependencies:
- Arduino
    i2cdevlib

## Installation
- Install Arduino I2Cdevlib
- 

## Docker Installation
#### Build Docker image
```
chmod +x build_docker.sh
./build_docker.sh
```
#### Accessing serial on container:
For more info, look [here](https://www.losant.com/blog/how-to-access-serial-devices-in-docker)
- Create the following file 
    ```
    sudo nano /etc/udev/rules.d/99-serial.rules
    ```
- Add the following line:
    ```
    KERNEL=="ttyUSB[0-9]*",MODE="0666"
    ```
- Save and exit

#### Run Docker container
```
chmod +x run_docker.sh
./run_docker.sh
```

# WIP
## Tello CV:
- Open-pose for pose recognition
- Tello control based on pose recognition

## Tello SLAM:
- Visual Inertial SLAM using ROS and Tello
