#!/usr/bin/env python

from collections import defaultdict
import dateutil.parser

# [1518-03-11 00:45] wakes up
# [1518-07-13 00:13] falls asleep
# [1518-11-02 23:56] Guard #3463 begins shift
def readLine(line):
    parts = line.strip().split("]")
    date = dateutil.parser.parse(parts[0][1:])
    guardId = -1
    if parts[1] == " wakes up":
        event = "wake"
    elif parts[1] == " falls asleep":
        event = "sleep"
    elif parts[1][-12:] == "begins shift":
        event = "new guard"
        guardId = int(parts[1].split("#")[1].split(" ")[0])
    else:
        raise Exception("Unparsable event: {}".format(parts[1]))

    # print("{} -- {} -- {}".format(date, event, guardId))
    return (date, event, guardId)

def sleepTime(shift, fromMinutes, toMinutes=60):
    for i in range(fromMinutes, toMinutes):
        shift[2][i] = True

def collapse(eventStream):
    shifts = []
    currentShift = None
    slept = -1
    for timestamp, eventName, guardId in eventStream:
        minutes = timestamp.minute
        if eventName == "new guard":
            if currentShift != None:
                if slept != -1:
                    sleepTime(currentShift, slept)
                shifts.append(currentShift)
            currentShift = ["{}-{}".format(timestamp.month, timestamp.day), guardId, [False] * 60]
        elif eventName == "sleep":
            if currentShift is None:
                raise Exception("Got sleep event without a guard: {} {} {}".format(timestamp, eventName, guardId))
            if slept != -1:
                raise Exception("Guard {} fell asleep for the second time at {}".format(currentShift[1], timestamp))
            slept = minutes
        elif eventName == "wake":
            if currentShift is None:
                raise Exception("Got sleep event without a guard: {} {} {}".format(timestamp, eventName, guardId))
            if slept == -1:
                raise Exception("Guard {} woke up for the second time at {}".format(currentShift[1], timestamp))
            sleepTime(currentShift, slept, minutes)
            slept = -1
    if currentShift is not None:
        if slept != -1:
            sleepTime(currentShift, slept)
        shifts.append(currentShift)
    return shifts

def findSleepiestGuard(shifts):
    sleepHoursByGuard = defaultdict(int)
    for monthDay, guardId, bitmap in shifts:
        sleepHoursByGuard[str(guardId)] += sum(map(lambda x: 1 if x else 0, bitmap))
    maxGuard = None
    maxHours = 0
    for guardId, sleepHours in sleepHoursByGuard.iteritems():
        if sleepHours > maxHours:
            maxHours = sleepHours
            maxGuard = int(guardId)
    return maxGuard

def getMinuteSleepSumariesByGuard(shifts):
    sleepSummariesByGuard = dict()
    for monthDay, guardId, bitmap in shifts:
        if str(guardId) not in sleepSummariesByGuard:
            sleepSummariesByGuard[str(guardId)] = [0] * 60
        for i in range(60):
            if bitmap[i]:
                sleepSummariesByGuard[str(guardId)][i] += 1
    return sleepSummariesByGuard

def printDataPoints(dataPoints):
    print("Datapoints:")
    for dataPoint in dataPoints:
        print("  {}".format(dataPoint))

def printShifts(shifts):
    print("Shifts:")
    for shift in shifts:
        bitmap = "".join(map(lambda x: "#" if x else ".", shift[2]))
        count = sum(map(lambda x: 1 if x else 0, shift[2]))
        print("  {} {} {} {}".format(shift[0], shift[1], bitmap, count))

# Read the events
with open("input.txt", "r") as inputFile:
    dataPoints = []
    for line in inputFile:
        dataPoints.append(readLine(line))

# Sort by date
dataPoints.sort(key=lambda x: x[0])

# Compact into shifts
shifts = collapse(dataPoints)

# Coallate by guard
sleepSummariesByGuard = getMinuteSleepSumariesByGuard(shifts)

# Find sleepiest guard
sleepiestGuardId = findSleepiestGuard(shifts)
maxSleepCount = 0
maxSleepTime = 0
for i in range(60):
    if sleepSummariesByGuard[str(sleepiestGuardId)][i] > maxSleepCount:
        maxSleepCount = sleepSummariesByGuard[str(sleepiestGuardId)][i]
        maxSleepTime = i
print("Guard {} slept the most on minute {}".format(sleepiestGuardId, maxSleepTime))
print("Part 1 answer {}".format(sleepiestGuardId * maxSleepTime))

# Find guard who slept the most on a single minute
bestChoice = (0, 0, 0)
for guardIdStr, bitmap in sleepSummariesByGuard.iteritems():
    for i in range(60):
        if bitmap[i] > bestChoice[2]:
            bestChoice = (int(guardIdStr), i, bitmap[i])
print("Guard {} slept on minute {} for {}".format(*bestChoice))
print("Part 2 answer {}".format(bestChoice[0] * bestChoice[1]))

#printDataPoints(dataPoints[:10])
#printShifts(shifts[:5])
