# iot-blinkt
A simple demonstration of using fedora iot to drive a gpio device. This runs the pimoroni blinkt rainbow example.

## Notes
The pimoroni blinkt library uses RPI.GPIO, which doesn't yet work on aarch64 (even fixing up its cpuinfo file, it segfaults). As libgpiod/python3-libgpiod work on fedora iot / fedora base images, I reworked the blinkt lib to use libgpio.

The built image runs a slightly modified rainbow example, installing sigterm and sigint handlers so that podman stop will cause a clean exit, turning off the leds.

Running this as a mortal user requires permissions on /dev/gpiobase, which I have set using udev

/etc/udev/rules.d/85-gpiochip.rules 
```
KERNEL=="gpiochip0", SUBSYSTEM=="gpio", MODE="0660", GROUP="gpio"
```
and adding the gpio group for my user

To build aand run first time:
```
podman build --tag fedora:rainbow -f ./Dockerfile
podman run -d --name rainbow --security-opt label=disable --device=/dev/gpiochip0 localhost/fedora:rainbow
```

Then you can use 
```
podman stop rainbow
podman start rainbow
```

