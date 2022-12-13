import netifaces as ni
import socket
import time
import headCommands as head
    
        

UDP_IP_TARGET = "192.168.100.100"
UDP_PORT = 12345

UDP_IP = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.bind((UDP_IP, UDP_PORT))
    sock.connect((UDP_IP_TARGET, UDP_PORT))
    while True:
        data, addr = sock.recvfrom(512)
        command = data.decode("ascii")
        print(data.decode("ascii"))
        if command[0]=="2":
            head(command)
            info="finished"
            sock.sendto(bytes(info, 'ascii'), (UDP_IP_TARGET, UDP_PORT))
        else:
            print("command is considered invalid")

