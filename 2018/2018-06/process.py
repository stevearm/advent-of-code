#!/usr/bin/env python

from collections import defaultdict, Counter
from functools import reduce
from itertools import chain
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

def createField(points, pointCreator):
    minX, minY, maxX, maxY = fieldSize(points)
    field = []
    for x in range(maxX - minX):
        column = []
        field.append(column)
        for y in range(maxY - minY):
            currentLocation = (x + minX, y + minY)
            point = pointCreator(currentLocation)
            column.append(point)
    return field

def edges(field):
    top = [column[0] for column in field]
    bottom = [column[-1] for column in field]
    left = field[0][1:-2]
    right = field[-1][1:-2]
    return top + bottom + left + right

def printLargestFiniteField(points):
    # None unresolved
    # -1 tie
    # [0-9]+ closest to that point
    def closestPoint(currentLocation):
        closest = None
        for pointIndex in range(len(points)):
            pointDistance = distance(currentLocation, points[pointIndex])
            if closest is None or pointDistance < closest[1]:
                closest = (pointIndex, pointDistance)
            elif pointDistance == closest[1]:
                closest = (-1, pointDistance)
        return closest

    field = createField(points, closestPoint)
    infinite = set([location[0] for location in edges(field)])
    frequency = Counter(map(lambda location: location[0], chain(*field)))

    largestField = None
    for fieldName, fieldSize in frequency.iteritems():
        fieldIndex = int(fieldName)
        if fieldIndex == -1 or fieldIndex in infinite:
            continue
        if largestField is None or fieldSize > largestField[1]:
            largestField = (fieldIndex, fieldSize)

    print("Have {} points".format(len(points)))
    print("Dropping {} infinite fields".format(len(infinite)))
    print("Largest field {} is size {}".format(*largestField)) # Largest field 4 is size 2906

printLargestFiniteField(points)

def printLargestTotalDistanceField(points):

    def totalDistancePoint(currentLocation):
        distanceToAllPoints = 0
        for point in points:
            distanceToAllPoints += distance(currentLocation, point)
        return distanceToAllPoints

    field = createField(points, totalDistancePoint)
    maxDistance = 10000
    locationsLowEnough = [x for x in chain(*field) if x <= maxDistance]
    print("{} locations had a total distance <= {}".format(len(locationsLowEnough), maxDistance))

printLargestTotalDistanceField(points) # 50530 locations had a total distance <= 10000
