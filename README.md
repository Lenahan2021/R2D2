# R2D2 Server Client Data Transfer

## Description

A small, but efficient way to transmit commands between two Raspberry Pi’s in order to run commands on the respective Pi.

## Prerequisites

I highly recommend you have some Electronics 101 acknowledgement before moving on to the rest of the project. This guide will get you started. (insert Bander’s Electronics 101 link)

Python 3

2 Raspberry Pi 3

Ethernet cable

## Installation

In order to get this project downloaded, clone this repo on both Raspberry pis using 
“git clone (link)”  picture of command in shell

We are going to need some prior setup before getting this project running. Before we get started, we are going to need to make sure that each Raspberry Pi has a static IP. A static IP is an IP address that doesn’t change after the system is rebooted. It is hard set into the network and the computer will always be able to be identified by this set IP address. In order to set the static IP of each Raspberry Pi, please follow this [guide](https://www.tomshardware.com/how-to/static-ip-raspberry-pi), 

**Note:** When setting the interface, make sure to choose “eth0” when setting each of the IPs. We chose the ip “192.168.100.101” and “192.167.100.100” for the client and server respectively. Both of our static routers were “192.168.100.0” With the default DNS as our “static domain_name_servers”

Once completed, connect the two Pis together using the LAN cable and do a quick check that the IPs you set are being used.

- Open up the terminal and run the command “ifconfig”
- Look for the eth0 connection and make sure the “inet” section is the same ip you have set on the pi.

If you have made it this far, great! You are one step closer to running the project. Running the python files is easy. Choose which pi you would like your server and client to run the respective file through the terminal. Make sure to run the server file first.

## To run the files
  
  python3 UDP_SERVER.py (on server pi)
	python3 UDP_CLIENT.py (on client pi)
  
Sweet! Once we have both scripts set up, we need to connect the breadboard to each pi. Using the GPIO cable that came with your kit, connect the female pins to the male GPIO pins on your Pi while connecting the other end to the breadboard. For our demonstration, we are going to setup the LED circuit like so:
