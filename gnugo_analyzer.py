#!/usr/bin/python

import os
import sys
import subprocess

def convertSgf2Move(move):    
    # Takes a sgf move like v.g."pd" and returns a human one "Q16"
    
    # Clean the move
    move = move.replace('W[', '')
    move = move.replace('B[', '')
    move = move.replace(']', '')
    
    firstChar = move[0]
    secondChar = move[1]
    
    # Convert fist char to the capital case
    # If the char is "larger" than h we have to take into account
    # the removed character in the "human" notation
    if ord(firstChar) <= ord('h'):
        firstChar = firstChar.capitalize()
    else:
        firstChar = chr(ord(firstChar)+1)
        firstChar = firstChar.capitalize()
    
    # Convert the second char to a number from 1 to 19
    secondChar = 19 - (ord(secondChar) - 97)
    
    return firstChar + str(secondChar)
    
    

if len(sys.argv) >= 2:
    filename = sys.argv[1]
else:
    print("usage: gnugo_analyzer my_file.sgf")
    exit()

sgfFile = open(sys.argv[1], 'r')
sgfContent = sgfFile.read().replace('\n', '')
#for line in sgfFile.readlines():
##        if ";B" in line:
#        print line
print sgfFile.name

# Load file contento into a list
sgfName = sgfFile.name
sgfFile.close()

# How many moves are in the game?
foundWhite = 0
foundBlack = 0
foundBlack += sgfContent.count(';B')
foundWhite += sgfContent.count(';W')
numMoves = max(foundWhite, foundBlack)
    
print numMoves

# Cleaing the moves played in the game
sgfContent = sgfContent.split(";")
onlyMoves = []
for field in sgfContent:
#    print field
    if 'W[' in field[0:5] or 'B[' in field[0:5]:
        onlyMoves.append(field[0:5])
print sgfContent
print '************************'
print onlyMoves
print onlyMoves[0]
print convertSgf2Move(onlyMoves[0])
print onlyMoves[1]
print convertSgf2Move(onlyMoves[1])
print len(onlyMoves)

#exit()

# Analyzing the game
for move in range(numMoves):
#for move in range(2):
    print
    command = 'gnugo' + ' -l ' + sgfName + ' -L ' + str(move+1) + ' -T ' + ' -w ' + ' -t ' + ' --level ' + '15'
    print command
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
    yourMove = convertSgf2Move(onlyMoves[move])
    print 'Your move was:', yourMove
    for comment in commentsList:
                if yourMove in comment:
                    print comment
    
    
    

