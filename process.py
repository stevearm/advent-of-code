#!/usr/local/bin/python
frequency = 0
seenFrequencies = set()
while True:
    with open("input.txt", "r") as inputFile:
        for line in inputFile:
            frequency += int(line)
            if frequency in seenFrequencies:
                print frequency
                exit(0)
            seenFrequencies.add(frequency)
