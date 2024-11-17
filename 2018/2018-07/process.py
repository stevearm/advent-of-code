#!/usr/bin/env python

from collections import defaultdict
import re
import string

input = []
with open("input.txt", "r") as inputFile:
    regex = re.compile("Step ([A-Z]) must be finished before step ([A-Z]) can begin.")
    for line in inputFile:
        result = regex.match(line)
        if not result:
            raise Exception("Something wrong with input: {}. Got result {}".format(line, result))
        input.append((result.group(1), result.group(2)))

def createDag(input):
    dag = {}
    for prereq, step in input:
        if step not in dag:
            dag[step] = set()
        dag[step].add(prereq)
        if prereq not in dag:
            dag[prereq] = set()
    return dag

def runnable(dag, finished):
    options = set()
    finished = set(finished)
    for step, prereqs in dag.iteritems():
        if step in finished:
            continue
        if len(prereqs - finished):
            # More remaining unfinished steps
            continue
        options.add(step)
    return options

def onePersonOrder(input):
    dag = createDag(input)
    order = ""
    while len(order) < len(dag):
        order += sorted(runnable(dag, order))[0]

    print("{} rules for {} steps".format(len(input), len(dag.keys())))
    print("Basic order: {}".format(order)) # ACHOQRXSEKUGMYIWDZLNBFTJVP

onePersonOrder(input)

def multiPersonOrder(input):
    baseTime = 60
    workerCount = 5

    secondsPerJob = dict([(string.ascii_uppercase[i], baseTime+i+1) for i in range(len(string.ascii_uppercase))])
    dag = createDag(input)

    finished = ""
    workers = []
    seconds = 0
    lastPrint = None
    while len(finished) < len(dag):
        # Start workers
        while len(workers) < workerCount:
            runnableJobs = runnable(dag, finished)
            unclaimedRunnable = set(runnableJobs) - set([worker[0] for worker in workers])
            if len(unclaimedRunnable) == 0:
                break # No more unassigned runnable jobs
            nextJob = sorted("".join(unclaimedRunnable))[0]
            jobEnd = seconds + secondsPerJob[nextJob]
            workers.append((nextJob, jobEnd))

        newPrint = "Finished {} and in play {}".format(finished, workers)
        if lastPrint != newPrint:
            print("{}: {}".format(seconds, newPrint))
            lastPrint = newPrint

        seconds += 1

        # Finish workers
        finished += "".join([worker[0] for worker in workers if worker[1] <= seconds])
        workers = [worker for worker in workers if seconds < worker[1]]

    print("Run for {} seconds in order {}".format(seconds, finished)) # Run for 419 seconds in order ACHOQREXSKGIUMYDWLZNBFTJVP

multiPersonOrder(input)
