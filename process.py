#!/usr/local/bin/python
frequency = 0
with open("input.txt", "r") as inputFile:
    for line in inputFile:
        frequency += int(line)
print frequency
