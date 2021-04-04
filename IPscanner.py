#!/usr/bin/env python

from ping3 import ping, verbose_ping
print("Scanning home network for busy IP addresses. Please wait!...")

IP_Start = '192.168.0.'
Range_Start = 1 #change this for starting range
Range_End = 100 #change this for ending range
for x in range (Range_Start, Range_End):
    string = str(x) #Turns the index into a string to concatenate
    string2 = IP_Start + string #concatenates the IP address from its current index
    val = ping(string2)  # Returns delay in seconds.
    #Prints active IP channels and its delay
    if type(val) == float:
        print("Found a active IP address: " + string2)
        print("IP delay: " + str(val) + " seconds")
print("All Active IP addresses from range 1-99 tested!")
input("Press enter to exit.")
