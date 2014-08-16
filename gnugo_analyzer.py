#!/usr/bin/python

import os
import sys
import subprocess

if len(sys.argv) >= 2:
    filename = sys.argv[1]
else:
    print("usage: gnugo_analyzer my_file.sgf")
    exit()

my_sgf_file = open(sys.argv[1], 'r')

print my_sgf_file.name
#exit()

# How many moves are in the game?
numlines = 0
foundWhite = 0
foundBlack = 0
for line in my_sgf_file:
    numlines += 1
    foundBlack += line.count(';B')
    foundWhite += line.count(';W')
     
for move in range(max(foundBlack, foundWhite)):
    print
    command = 'gnugo' + ' -l ' + str(my_sgf_file.name) + ' -L ' + str(move) + ' -T ' + ' -w ' + ' -t ' + ' --level ' + '10'
    output = os.popen(command + " 2>&1")
    tmpList = []
    commentsList = []
    count = 0
    for line in output.readlines():
        line = line.rstrip()
        tmpList.append(line)
        if "Move at" in line:
            commentsList.append(line)
    for info in tmpList:
        if "Top" in info:
            bestMove = tmpList[count + 1]
            bestMove = bestMove[3:6]
            print "Best move #",str(move+1), " is:", bestMove
            for comment in commentsList:
                if bestMove in comment:
                    print comment
        count+=1
    
    

