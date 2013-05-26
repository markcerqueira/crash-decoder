#!/usr/bin/python

import sys
import subprocess
import time
import re

# check command-line arguments
if len(sys.argv) != 2:
    sys.exit("usage: crashDecoder inputFile")
    
# remove all spaces from crash report
inputFile = open(sys.argv[1], 'r')
spacelessFile = open(sys.argv[1] + "_hex", 'w')

for line in inputFile:
    line = line.replace(' ', '')
    spacelessFile.write(line)

spacelessFile.close()

# convert from hex to binary
subprocess.call( './HexToBinary ' + str(sys.argv[1]) + '_hex ' + str(sys.argv[1]) + '_binary', shell=True )

# process crash report
subprocess.call('./plcrashutil convert --format=iphone ' + str(sys.argv[1]) + '_binary > ' + str(sys.argv[1]) + "_crash" , shell=True )
