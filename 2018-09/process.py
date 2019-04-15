#!/usr/bin/env python

import re

with open("input.txt", "r") as inputFile:
    regex = re.compile("([0-9]+) players; last marble is worth ([0-9]+) points")
    for line in inputFile:
        result = regex.match(line)
        if not result:
            raise Exception("Something wrong with input: {}. Got result {}".format(line, result))
        players = int(result.group(1))
        lastMarble = int(result.group(2))

def takeTurn(field, currentMarbleIndex, newMarbleValue):
    if newMarbleValue % 23 == 0:
        removeIndex = (currentMarbleIndex - 7) % len(field)
        newField = field[:removeIndex] + field[removeIndex+1:]
        return newField, removeIndex, field[removeIndex] + newMarbleValue

    insertIndex = (currentMarbleIndex + 2) % len(field)
    if insertIndex == 0:
        # This is just to make it print the same way as the examples
        insertIndex = len(field)
    newField = field[:insertIndex] + [newMarbleValue] + field[insertIndex:]

    return newField, insertIndex, 0

def printHighestScore(players, lastMarble):
    field = [0]
    currentMarbleIndex = 0
    marbleValue = 1
    while marbleValue <= 25:
        field, currentMarbleIndex, capturedValue = takeTurn(field, currentMarbleIndex, marbleValue)
        marbleValue += 1
        print(field)

printHighestScore(players, lastMarble)
