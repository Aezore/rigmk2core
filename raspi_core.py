__author__ = 'Research'
import socket
import time

socket1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

timetosend = time.asctime()

server_address = ('192.168.0.193', 55555)
raspi_address = ('192.168.0.197', 55554)

socket2.bind(raspi_address)

while True:
    timetosend = time.asctime()
    data, addr = socket2.recvfrom(1024)
    socket1.sendto(str(timetosend), server_address)

socket1.close()
socket2.close()
