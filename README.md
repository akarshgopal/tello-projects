# Some fun Projects with Ryze Tello 

## TODO for Tello Projects

### Project packaging ~ 6 hrs
- setup environment
- setup CI/CD
- <strike>setup git(hub)</strike>
- prep requirements file, environment file
- package into docker image?
- documentation

### General Comms ~ 2 hrs
- <strike> establish UDP connection to tello </strike>
- <strike>send key commands via UDP</strike>
    - <strike>perform two way comms using tellopy</strike>
- stream video over connection
    - <strike>figure out how to access video stream with tellopy</strike>
    - HUD
        - <strike>figure out how to access state info with tellopy </strike>
        - overlay on video (cv2.putText())
    - <strike>display video on browser using opencv + Flask </strike>
    - get it to work over docker

### Hand-Motion Control ~ 10hrs
- Comms ~ 5 hrs
    - IMU + Raspberry pi/ Arduino
        - get raw IMU data using MPU6050 w 
            -Raspberry Pi (multi sensor readings)
            -<strike>Arduino</strike>
    - bridge pi/arduino over to tello
    - linear acc + quaternion commands from IMU to tello commands

- Algos ~ 5 hrs
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