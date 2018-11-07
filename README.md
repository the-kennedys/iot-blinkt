podman build --tag fedora:rainbow -f ./Dockerfile
podman run -d --name rainbow --security-opt label=disable --device=/dev/gpiochip0 localhost/fedora:rainbow

