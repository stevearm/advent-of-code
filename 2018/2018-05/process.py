#!/usr/bin/env python

import re
import string

def react(polymer):
    i = 1
    while i < len(polymer):
        if polymer[i-1].lower() == polymer[i].lower() and polymer[i-1] != polymer[i]:
            polymer = polymer[:i-1] + polymer[i+1:]
            i -= 1
            if i < 1:
                i = 1
        else:
            i += 1
    return polymer

# Read the polymer
with open("input.txt", "r") as inputFile:
    polymer = inputFile.read().strip()

print("Polymer is {} long".format(len(polymer)))
print("Plain reaction results in {} long".format(len(react(polymer))))

shortestLetter = None
shortestLength = len(polymer)
for character in string.ascii_lowercase:
    filteredPolymer = re.sub("[{}]".format(character), "", polymer, 0, re.I)
    reactedPolymer = react(filteredPolymer)
    if len(reactedPolymer) < shortestLength:
        shortestLetter = character
        shortestLength = len(reactedPolymer)
print("Shortest polymer is {} by removing {}".format(shortestLength, shortestLetter))
