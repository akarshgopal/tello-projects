# Some fun Projects with Ryze Tello 

## TODO for Tello Projects
### Project packaging
- setup environment
- setup dependencies for tello sdk, tello py, cv, and dl if needed
- setup CI/CD
- setup git(hub)
- prep requirements file, environment file
- package into docker image?

### General Comms
- <strike> establish UDP connection to tello </strike>
- send key commands via UDP
- stream video over connection

### Gesture Control
- Comms
    - IMU + Raspberry pi/ Arduino
    - bridge pi/arduino over to tello
    - linear acc + quaternion commands from IMU to tello commands

- Algos
    - State estimation and Parameter estimation
        - Kalman Filter
        - Sensor selection

### CV based Control
- establish a CV pipeline
    - get img/vid stream -> run model inference -> visualise output + return command
    - move to more complicated CV

### Visual + Inertial SLAM
- establish a SLAM pipeline
    - get img/vid stream + IMU state -> run SLAM algo -> visualize 
    - move to more complicated SLAM
    - integrate with ROS - learn ROS and related stuff

### Web-App
- Implement features in browser?
    - video stream
    - CV inference
    - gesture vis
    - 
### Hack
- Try and get access to internals of Tello?
- Get access to low-level controller?