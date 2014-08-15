#!/usr/bin/python

import os
import sys
import subprocess

print len(sys.argv)
if len(sys.argv) >= 2:
    print "It seems we have a file to analyze"
    filename = sys.argv[1]
else:
    print("usage: gnugo_analyzer my_file.sgf")
    exit()

my_sgf_file = open(sys.argv[1], 'r')

# How many moves are in the game?
numlines = 0
foundWhite = 0
foundBlack = 0
for line in my_sgf_file:
    numlines += 1
    foundBlack += line.count(';B')
    foundWhite += line.count(';W')
     
print foundWhite
print foundBlack

for move in range(max(foundBlack, foundWhite)):
#    command = 'gnugo' + ' -l ' + str(my_sgf_file.name) + ' -L ' + str(move) + ' -T ' + ' -t ' + ' --level ' + '10'
    command = ['gnugo', '-l ', str(my_sgf_file.name), '-L' , str(move), '-T',  '-t', '--level', '10']
#    print command
#    print os.devnull
#    output = subprocess.Popen(command, stdout=subprocess.PIPE, shell = True)
#    (out, err) = output.communicate()
    p = subprocess.Popen(['gnugo', '-l ', str(my_sgf_file.name), '-L' , str(move), '-T',  '-t', '--level', '10'], stdout=subprocess.PIPE)
    output, err = p.communicate()
#    print output
#    output = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()
#    output = subprocess.Popen(command, stdout=open(os.devnull, 'w'))
#    output = subprocess.call(command, shell=True)
#    output = os.popen(command)
#    output = subprocess.call(command)
#    output = subprocess.Popen(command, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
#    output = subprocess.Popen((command), stdout = open(os.devnull, 'w'), shell = True)
#    output = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell = True)
