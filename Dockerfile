FROM fedora:latest
RUN dnf -y update && \
  dnf -y install libgpiod-utils python3-libgpiod
COPY blinkt_gpiod.py rainbow.py /usr/src
WORKDIR /usr/src
CMD ["python3", "rainbow.py"]
