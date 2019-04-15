#!/usr/bin/env python

from collections import defaultdict
import re

# Read the points
points = []
with open("input.txt", "r") as inputFile:
    regex = re.compile("([0-9]+), ([0-9]+)")
    for line in inputFile:
        result = re.split(r"[^0-9]+", line.strip())
        if len(result) != 2:
            raise Exception("Something wrong with input: {}. Got result {}".format(line, result))
        x = int(result[0])
        y = int(result[1])
        points.append((x, y))

def distance(a, b):
    xDistance = max(a[0], b[0]) - min(a[0], b[0])
    yDistance = max(a[1], b[1]) - min(a[1], b[1])
    return xDistance + yDistance

def fieldSize(points):
    minX, minY = points[0]
    maxX, maxY = points[0]
    for point in points:
        minX = min(minX, point[0])
        minY = min(minY, point[1])
        maxX = max(maxX, point[0])
        maxY = max(maxY, point[1])
    return (minX, minY, maxX, maxY)

def createField(points):
    # None unresolved
    # -1 tie
    # [0-9]+ closest to that point
    minX, minY, maxX, maxY = fieldSize(points)
    field = []
    for x in range(maxX - minX):
        column = []
        field.append(column)
        for y in range(maxY - minY):
            currentLocation = (x + minX, y + minY)
            closest = None
            for pointIndex in range(len(points)):
                pointDistance = distance(currentLocation, points[pointIndex])
                if closest is None or pointDistance < closest[1]:
                    closest = (pointIndex, pointDistance)
                elif pointDistance == closest[1]:
                    closest = (-1, pointDistance)
            column.append(closest)
    return field

def edges(field):
    edgeNumbers = set()
    top = [column[0] for column in field]
    bottom = [column[-1] for column in field]
    left = field[0]
    right = field[-1]
    for location in top + bottom + left + right:
        edgeNumbers.add(location[0])
    return edgeNumbers

def frequency(field):
    freq = defaultdict(int)
    for column in field:
        for location in column:
            freq[str(location[0])] += 1
    return freq

field = createField(points)
infinite = edges(field)
freq = frequency(field)

largestField = None
for fieldName, fieldSize in freq.iteritems():
    fieldIndex = int(fieldName)
    if fieldIndex == -1 or fieldIndex in infinite:
        continue
    if largestField is None or fieldSize > largestField[1]:
        largestField = (fieldIndex, fieldSize)

print("Have {} points".format(len(points)))
print("{} infinite fields".format(len(infinite)))
print("Frequencies: {}".format(freq))
print("Largest field {} is size {}".format(*largestField))
