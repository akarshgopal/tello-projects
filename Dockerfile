# Use the official image as a parent image
FROM nvidia/cuda:10.0-cudnn7-devel-ubuntu18.04

# Set timezone to avoid interactive setup
# !!Temp workaround, needs to be fixed in case host time is to be used
ENV TZ=Europe/Berlin
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Dockerfile instructions taken from https://github.com/ExSidius/openpose-docker/blob/master/Dockerfile and updated to Ubuntu 18.04
# cmake 3.12.2 to fix build issue
RUN echo "Installing dependencies..." && \
	apt-get -y --no-install-recommends update && \
	apt-get -y --no-install-recommends upgrade
RUN	apt-get install -y --no-install-recommends build-essential 
RUN	apt-get install -y --no-install-recommends cmake
RUN	apt-get install -y --no-install-recommends git
RUN	apt-get install -y --no-install-recommends libatlas-base-dev
RUN	apt-get install -y --no-install-recommends libprotobuf-dev
RUN	apt-get install -y --no-install-recommends libleveldb-dev
RUN	apt-get install -y --no-install-recommends libsnappy-dev
RUN	apt-get install -y --no-install-recommends libhdf5-serial-dev \
	protobuf-compiler \
	libboost-all-dev \
	libgflags-dev \
	libgoogle-glog-dev \
	liblmdb-dev \
	pciutils
RUN	apt-get install -y --no-install-recommends python3-setuptools \
	python3-dev \
	python3-pip 
RUN	apt-get install -y --no-install-recommends opencl-headers \
	ocl-icd-opencl-dev \
	libviennacl-dev \
	libcanberra-gtk-module 
RUN	apt-get install -y --no-install-recommends pkg-config \
    libavformat-dev \
    libavdevice-dev \
    libsm6 libxext6 libxrender-dev \
    mplayer \
	libopencv-dev 

RUN pip3 install \
	numpy \
	protobuf 

# RUN pip install av
RUN pip3 install av==6.1.2
# trying to fix "No module named skbuild"
RUN pip3 install scikit-build
RUN pip3 install opencv-python
#RUN pip3 install imutils
RUN pip3 install tellopy

# for tello.py
RUN pip3 install pygame

# for arduino
RUN pip3 install pyserial

# for web-streaming
RUN pip3 install flask
RUN pip3 install imutils

# install latest version of cmake to avoid make issue
RUN apt purge -y --auto-remove cmake
RUN apt purge -y cmake-qt-gui
RUN apt-get -y --no-install-recommends install qtbase5-dev
RUN apt-get -y --no-install-recommends install wget
RUN apt-get -y --no-install-recommends install libssl-dev libtool
RUN wget https://github.com/Kitware/CMake/releases/download/v3.18.1/cmake-3.18.1.tar.gz && \
    tar -xvf cmake-3.18.1.tar.gz
RUN cd cmake-3.18.1 && \
    ./configure --qt-gui 
RUN cd cmake-3.18.1 && \
    ./bootstrap && make -j`nproc` && make install -j`nproc`

# -DBUILD_PYTHON=ON in order to turn on python api build
RUN echo "Downloading and building OpenPose..." && \
	git clone https://github.com/CMU-Perceptual-Computing-Lab/openpose.git && \
	mkdir -p /openpose/build && \
	cd /openpose/build && \
	cmake -DBUILD_PYTHON=ON .. && \
	make -j`nproc`
    
RUN pip3 install simple-pid

# Set the working directory
WORKDIR /usr/src/app