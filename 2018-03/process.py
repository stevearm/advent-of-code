#!/usr/local/bin/python

from collections import defaultdict

def getSheet(x):
    return [[False] * x] * x

def parseLine(line):
    #3 @ 937,817: 10x25
    parts = line.split(" ")
    id = int(parts[0][1:])
    x, y = map(int, parts[2][:-1].split(","))
    length, width = map(int, parts[3].split("x"))

    return id, x, y, length, width

sheet = getSheet(1000)
overbooked = set()

with open("input.txt", "r") as inputFile:
    for line in inputFile:
        id, x, y, length, width = parseLine(line)
        for i in range(length):
            for j in range(width):
                if sheet[x+i][y+j]:
                    overbooked.add((x+i,y+j))
                sheet[x+i][y+j] = True

print overbooked
print "Overbooked spots: {}".format(len(overbooked))
