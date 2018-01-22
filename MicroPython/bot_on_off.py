import socket
from machine import Pin
from time import sleep

pinD4 = Pin(2, Pin.OUT)
pinD1 = Pin(5, Pin.OUT)


def pisca():
    for n in '101010101':
        sleep(0.5)
        pinD4.value(int(n))


def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', 1060))

    while True:
        data, address = sock.recvfrom(10)
        text = data.decode('ascii')
        if text == 'Liga':
            pinD1.on()
        elif text == 'Desliga':
            pinD1.off()
