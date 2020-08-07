# Use the official image as a parent image
FROM ubuntu:18.04

# Set timezone to avoid interactive setup
# !!Temp workaround, needs to be fixed in case host time is to be used
ENV TZ=Europe/Berlin
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Set the working directory
WORKDIR /usr/src/app

# Install any needed packages specified in requirements.txt
RUN apt-get update
RUN apt-get install -y pkg-config
RUN apt install -y python3-dev
RUN apt-get install -y python3-pip
RUN apt-get install -y libavformat-dev libavdevice-dev
RUN apt-get install -y libsm6 libxext6 libxrender-dev

# RUN pip install av
RUN pip3 install av==6.1.2
RUN pip3 install opencv-python
#RUN pip3 install imutils
RUN pip3 install tellopy

# for tello.py
RUN apt-get install -y mplayer 
RUN pip3 install pygame

# for arduino
RUN pip3 install pyserial

# for web-streaming
RUN pip3 install flask
RUN pip3 install imutils
