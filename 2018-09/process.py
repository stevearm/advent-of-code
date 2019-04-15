#!/usr/bin/env python

import re

with open("input.txt", "r") as inputFile:
    regex = re.compile("([0-9]+) players; last marble is worth ([0-9]+) points")
    for line in inputFile:
        result = regex.match(line)
        if not result:
            raise Exception("Something wrong with input: {}. Got result {}".format(line, result))
        players = int(result.group(1))
        points = int(result.group(2))

print("Game has {} players and last marble is worth {}".format(players, points))
