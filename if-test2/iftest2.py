#!/usr/bin/env python3

ipchk = '192.168.0.1'

if ipchk:
   print('Looks like the IP address was set: ' + ipchk)


#fakeip = None
fakeip = "wallawalla washington"

if fakeip:
    print("Wow looks like that tested true")
else:
    print("That does not test true")


# this is assignment
#skycolor = "blue"
#skycolor = "grey"
#skycolor = "red"
skycolor = "flying toaster"

# this is conditional testing
if skycolor == "blue":
    print("Looks like a great day!")
elif skycolor == "grey":
    print("Sounds like a crummy day :( ")
elif skycolor == "red":
    print("Sounds dangerous")
else:
    print("I am not smart enough to know what is or is not happening")
