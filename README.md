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

### bodyCommands.py file.

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

![image](https://user-images.githubusercontent.com/91961435/207186717-b2924120-ff83-4610-8185-87be9b029624.png)

Above is a hypothetical example of adding more commands. This is where you will do all your editing when adding or removing commands and running them. 

### UDP_SERVER.py

![image](https://user-images.githubusercontent.com/91961435/207186843-f89ab1fd-a126-4033-9a4a-0feb7005c98c.png)

Let’s import our neccessary modules.

![image](https://user-images.githubusercontent.com/91961435/207186879-e974a5fb-6f98-40f3-9dc3-fa6afb21f02f.png)

Let's start with our defined variables. We are gathering the IP and port number we are going to be using when identifying our server. The IP is being pulled from the current IP of the ethernet connection. Our port is just a random open port to allow communication.

![image](https://user-images.githubusercontent.com/91961435/207188389-a32de1f2-f827-4a4b-948b-0e53537b8720.png)

Let’s now create our socket. A socket is just an endpoint that receives data after being passed. Here, we are creating a UDP (much simpler, and is faster. Note: if the packet is lost over the transmission, it will not send again.) socket that is binded to our defined IP and Port.
This is how the other Pi will be able to communicate with us.

![image](https://user-images.githubusercontent.com/91961435/207188513-2cda0950-446c-4fbf-a94c-5055eca2ac0c.png)

Lets create a while loop to make sure our program never ends.

![image](https://user-images.githubusercontent.com/91961435/207188677-c593b382-66b0-4862-9f43-5112c942d1e5.png)

For testing purposes, we were going with manual input as it was easier, but when the controller is connected, this will all be handled automatically. As stated earlier, we chose strings that started with 1 to remain on the Server PI while strings that start with 2 to be sent to the other Pi. If the string starts with 2, send the data as a Byte String in the ascii format to the Address of ‘192.168.100.101’(this is the static IP of our Client Pi) on the specified port. (You can use any identifier you want, but 1 and 2 was just the simplest)

![image](https://user-images.githubusercontent.com/91961435/207188788-35765058-00b5-4709-9d9d-d601a6bf1af5.png)

Continuing on, we then set up a callback function to receive information of whether or not the task has been received from the other Pi. We create a new empty string called data. While that string is empty, we have not heard a response back from the other pi. We are actively listening and waiting for a response back. Once received, we decode the data, as it is a byte string(a sequence of bytes that can be decoded back to english), and print out the message and where it came from.

![image](https://user-images.githubusercontent.com/91961435/207188899-88fa06dd-7008-4367-bd55-da3781b33927.png)


If the string did start with a 1, we use the commands on the server to execute what we want our Pi to do.

### UDP_Client.py

![image](https://user-images.githubusercontent.com/91961435/207189254-09c4dc1e-11cf-47ab-a984-3a343312d842.png)

Import the required packages, we will use these later.

![image](https://user-images.githubusercontent.com/91961435/207189359-a919c086-e8e7-4521-8c03-4eeebe22b022.png)

Lets start with defining our variables. Our target IP is going to be our server Pi to which we will be relaying the feedback callbacks to. Our port is the same port that the server uses, and our IP is the IP we pull from our Pi.

![image](https://user-images.githubusercontent.com/91961435/207189509-4db965a1-2133-48bd-ae38-67c2657b0192.png)

We then create a socket that uses UDP once more. We bind our IP and Port to our socket, or our endpoint. This allows the server to be able to contact our Client, think of it like an address in order to receive mail packages.

![image](https://user-images.githubusercontent.com/91961435/207189628-0ba4ef31-8ba6-4be9-b13c-c3888e104ac3.png)

Lets then create a loop. This loop will listen for incoming data that is being sent our way. Once we receive the data, we will then decode it. (As it is being sent from the server as a byte string.) Then we print our the message we recieve. 

![image](https://user-images.githubusercontent.com/91961435/207189750-b43e1d74-ef5c-4da7-be92-a37c6bf74b94.png)

Create a conditional inside the loop. This checks to see if the first index of the command string is a “2”. If it is, then run the command we received. Once the command is finished, we then create a String callback variable and send it back to the server. Once the response is received, the server knows that function is completed.

![image](https://user-images.githubusercontent.com/91961435/207189909-fe43d99c-3039-43e4-ba8f-8f2ef9098117.png)

If the command does not start with “2”, then we know that command is not either “1” or “2” so just discard it.
