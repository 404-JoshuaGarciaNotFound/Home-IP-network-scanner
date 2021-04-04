#!/usr/bin/env python

from ping3 import ping, verbose_ping
print("Scanning home network for busy IP addresses. Please wait!...")

val1 = '192.168.0.'
x = 0
for x in range (1, 100):
    #convertnumconvertnum = str(x)
    string = str(x)
    string2 = val1 + string
    val = ping(string2)  # Returns delay in seconds.
    #print(val)
    #print("Tested" + string2)
    if type(val) == float:
        print("Found a active IP address: " + string2)

print("All Active IP addresses from range 1-99 tested!")
input("Press enter to exit.")
