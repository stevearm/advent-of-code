#!/usr/bin/env python

with open("input.txt", "r") as inputFile:
    input = [int(x) for x in inputFile.read().strip().split(" ")]

print("Input is {} integers".format(len(input)))
