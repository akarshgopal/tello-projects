xhost +local:root

## mounts pwd to docker container
## uses X-server for display passthrough

#    -v /dev/video0:/dev/video0 \
#   -v /dev/video1:/dev/video1 \
cwd=$(pwd)
sudo docker run --rm -it --net=host  \
   --privileged \
   --gpus all \
   -e DISPLAY=$DISPLAY \
   -v $cwd:/usr/src/app \
   -v /tmp/.X11-unix:/tmp/.X11-unix \
   -v /dev:/dev \
   --name tello-app \
   tello-app:openpose