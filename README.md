# Some fun Projects with Ryze Tello 

## TODO for Tello Projects

### Project packaging ~ 3 hrs
- setup environment
- setup CI/CD
- <strike>setup git(hub)</strike>
- prep requirements file, environment file
- package into docker image?

### General Comms ~ 2 hrs
- <strike> establish UDP connection to tello </strike>
- send key commands via UDP
- stream video over connection

### Hand-Motion Control ~ 5hrs
- Comms ~ 2 hrs
    - IMU + Raspberry pi/ Arduino
    - bridge pi/arduino over to tello
    - linear acc + quaternion commands from IMU to tello commands

- Algos ~ 3 hrs
    - State estimation and Parameter estimation
        - Kalman Filter
        - Sensor selection

### CV based Control ~ 10 hrs
- establish a CV pipeline
    - get img/vid stream -> run model inference -> visualise output + return command
    - move to more complicated CV

### Visual + Inertial SLAM ~ 25 hrs
- establish a SLAM pipeline
    - get img/vid stream + IMU state -> run SLAM algo -> visualize 
    - move to more complicated SLAM
    - integrate with ROS - learn ROS and related stuff

### Web-App ~ 5 hrs
- Implement features in browser?
    - video stream
    - CV inference
    - gesture vis

### Mobile App ~ 20 hrs
- Implement features as add-on to Tello App?
    - Combine IMU based + CV based control + VI SLAM   

### Hack
- Try and get access to internals of Tello?
- Get access to low-level controller?