#!/usr/bin/env python3
"""RZFeeser | About to take a break
using csv data

Might be a good script to study later"""

import csv

def main():
    # open the CSV data set
    with open("vendor.csv", "r") as vendorfile:
        vendata = csv.reader(vendorfile, delimiter=",")
        # The CSV data is now nicely prepared.
        # Each new row is a Python list.
        # We can reference the items we want to print
        # as we loop over the data.
        for row in vendata:
            print("The IP address " + row[2] + " requires the driver " + row[3])

main()

