xhost +

## mounts pwd to docker container
## uses X-server for display passthrough

#    -v /dev/video0:/dev/video0 \
#   -v /dev/video1:/dev/video1 \

sudo docker run --rm -it --net=host  \
   --privileged \
   -e DISPLAY=$DISPLAY \
   -v ~/Projects/tello:/usr/src/app \
   -v /tmp/.X11-unix:/tmp/.X11-unix \
   -v /dev:/dev \
   --name tello_app \
   tello_app