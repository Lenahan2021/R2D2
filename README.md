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

![Capture](https://user-images.githubusercontent.com/91961435/207184545-3d31c1ac-a7ff-4850-abe4-250935b2ea99.PNG)

The final result of each pi should look like this.

![Capture1](https://user-images.githubusercontent.com/91961435/207184624-571efe13-3ea4-428c-9e42-286d8df8b284.PNG)

## Using the scripts

Once having both connections running, you should get a prompt on your server that reads “Choose 1 or 2”. Depending on which number is inputted, it will use that command to turn on the LED either on the server or the client using 1 and 2 respectively. 

This is very important when being able to distinguish which command will perform what action and on which area of the robot the action will be performed. The two commands could be used for all the lights and turning of the head, while 1 commands could be used to control the body movement, with each Pi handling the different sections. We can also make our own commands and see which command matches up with the specific functions that will control the LEDs or the servos.

## Breakdown

### Let's start with the bodyCommands.py file.

As of right now, I have specified that the server pi will be in charge of the body, so the bodyCommands.py file hosts all of the necessary functions to handle the body (open and close motors, turn on LEDs etc). As you progress more on this project, you will have to build out your own functions based on the objective. 

![1](https://user-images.githubusercontent.com/91961435/207185678-0d5b2b8b-e5cd-49e9-9849-f01a2dfdc819.PNG)

Let's start by importing our two modules we need. The GPIO module is our most important one as it will allow us to communicate with our Pi board. 

![2](https://user-images.githubusercontent.com/91961435/207185895-144ab7b2-3d0a-4dd9-85a1-9d3960ee1e40.PNG)

Then we assign our ledPin to pin 11 on the GPIO. This specifies which pin we will give voltage to.

![3](https://user-images.githubusercontent.com/91961435/207186077-dc8a5e00-38c3-4503-9c59-c71544f96d33.PNG)

Next is our cleanup function. This will be called after each function using the GPIO as it will get rid of any unnecessary pins that we are not using right now.  It is just good practice to use.

![4](https://user-images.githubusercontent.com/91961435/207186285-2557a01e-ad71-4c06-8e83-f5f55f09a5bf.PNG)

As you can see, we have an example led method that turns on and off an LED, which essentially just supplies power to the circuit, then turns off the power to the pin. This should be pretty self explanatory if you followed the electronics 101 tutorial.

![5](https://user-images.githubusercontent.com/91961435/207186382-709c4a68-1d31-4d92-a523-0b199fad34fb.PNG)

The commands method is where you call your other built out methods. It takes in a data variable, and that variable is the string you will pass in from the user input. If the data matches up with a specific command you choose, then call the specific method. 


