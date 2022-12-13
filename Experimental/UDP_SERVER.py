#UDP SERVER
import netifaces as ni
import socket
import bodyCommands as body
import time


UDP_IP = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr'] # listen to everything
UDP_PORT = 12345 # port


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.bind((UDP_IP, UDP_PORT))

    
    while True:
        
        info = input("Choose 1 or 2: ")
        if info[0] == "2":
            sock.sendto(bytes(info, 'ascii'), ("192.168.100.101", UDP_PORT))
            data = ''
            while not data:
                data, addr = sock.recvfrom(512) 
                print("received message: " + data.decode("ascii") + " from " + addr[0])
        else:
            body.commands(info)
            
