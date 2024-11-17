#!/usr/bin/env python

with open("input.txt", "r") as inputFile:
    input = [int(x) for x in inputFile.read().strip().split(" ")]

def parseIntoNode(stream, startPosition):
    children = []
    currentPosition = startPosition + 2
    for childIndex in range(stream[startPosition]):
        child, currentPosition = parseIntoNode(stream, currentPosition)
        children.append(child)

    metadataCount = stream[startPosition + 1]
    metadata = stream[currentPosition:currentPosition + metadataCount]

    return (children, metadata), currentPosition + metadataCount

def printSumOfAllMetadata(input):
    rootNode, nextPosition = parseIntoNode(input, 0)

    def recursiveMetadataSum(node):
        return sum(node[1]) + sum([recursiveMetadataSum(child) for child in node[0]])

    totalMetadata = recursiveMetadataSum(rootNode)
    print("Sum of all metadata is {}".format(totalMetadata)) # 42798

printSumOfAllMetadata(input)

def printSumOfAllNodeValues(input):
    rootNode, nextPosition = parseIntoNode(input, 0)

    def nodeValue(node):
        if len(node[0]) == 0:
            return sum(node[1])
        value = 0
        for childIndex in node[1]:
            if childIndex == 0 or childIndex > len(node[0]):
                continue
            value += nodeValue(node[0][childIndex - 1])
        return value

    print("Value of root node is {}".format(nodeValue(rootNode))) # 23798

printSumOfAllNodeValues(input)
