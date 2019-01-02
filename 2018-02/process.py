#!/usr/local/bin/python

from collections import defaultdict

def increase(acc, x):
    acc[x] += 1
    return acc

def freqMap(line):
    return reduce(increase, line, defaultdict(int))

doubles = 0
triples = 0
length = None
seenNgrams = set()
with open("input.txt", "r") as inputFile:
    for line in inputFile:
        double = False
        triple = False
        for letter, count in freqMap(line).iteritems():
            if count == 2:
                double = True
            if count == 3:
                triple = True
        if double:
            doubles += 1
        if triple:
            triples += 1

        if length is None:
            length = len(line)
        assert length == len(line)

        for i in range(len(line)):
            tuple = line[:i] + '_' + line[i+1:]
            assert len(line) == len(tuple)
            if tuple in seenNgrams:
                print "Part 2: {}{}".format(line[:i], line[i+1:])
            seenNgrams.add(tuple)

print "Part 1: {}".format(doubles * triples)
