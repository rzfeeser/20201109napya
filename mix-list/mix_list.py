#!/usr/bin/env python3

my_list = ["192.168.0.5", 5060, "UP"]

# display to standard out item 0 in my_list
print(my_list[0])

# combine two strings, concatenate (add) 
print("The first item in the list (IP): " + my_list[0])

# display the next item in the list
print(my_list[1])

# this will cause an error
# print("The port is: " + my_list[1])
print("The port is: " + str(my_list[1]))

print("The port is:", my_list[1])

print(f"The port is: {my_list[1]}")

# print the value UP
print("The last item in the list (state): " + my_list[2] )

new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

print("When I ssh into IP address", new_list[3], "or", new_list[4], "I am unable to ping ports")
