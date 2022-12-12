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

**Note:** When setting the interface, make sure to choose “eth0”. When setting each of the ip’s we chose the ip “192.168.100.101” and “192.167.100.100” for the client and server respectively. Both of our static routers were “192.168.100.0” With the default DNS as our “static domain_name_servers”
