#!/usr/bin/env python

import re
import time

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

def getHighestScore(players, lastMarble):
    playerScores = [0 for i in range(players)]
    currentPlayer = 0

    field = [0]
    currentMarbleIndex = 0
    marbleValue = 1
    while marbleValue <= lastMarble:
        field, currentMarbleIndex, capturedValue = takeTurn(field, currentMarbleIndex, marbleValue)
        marbleValue += 1

        playerScores[currentPlayer] += capturedValue
        currentPlayer = (currentPlayer + 1) % players
    return max(playerScores)

def printHighestScore(players, lastMarble):
    highestScore = getHighestScore(players, lastMarble)
    print("High score for {} players after {} marble: {}".format(players, lastMarble, highestScore))
    return highestScore

# Part 1
# printHighestScore(462, 71938) # 398371

# Part 2
# printHighestScore(462, 7193800)

def speedTest(players, lastMarble):
    start = time.time()
    highestScore = getHighestScore(players, lastMarble)
    end = time.time()
    print("For {} took {}s".format(lastMarble, end - start))

speedTest(30, 15000)

def checkLogic():
    knownGoodResults = [(10, 1618, 8317),
                        (13, 7999, 146373),
                        (17, 1104, 2764),
                        (21, 6111, 54718),
                        (30, 5807, 37305)]
    for players, lastMarble, highestScoreExpected in knownGoodResults:
        highestScore = getHighestScore(players, lastMarble)
        if highestScore != highestScoreExpected:
            print("Failed. For {}/{} got {} but expected {}".format(players, lastMarble, highestScore, highestScoreExpected))
checkLogic()
