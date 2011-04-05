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

#crashReport = open(str(sys.argv[1]) + "_crash", 'r')

#appName = ""

# find the app name
#for line in crashReport:
#    m = re.search( '^Identifier:', line)
#    if (m != None):
#        appName = line.replace('Identifier:', '')
#        appName = appName.replace(' ', '')
#        appName = appName.rstrip()
#        break

# give crash report more meaningful name
#crashReportName = appName + "_" + str(time.localtime().tm_mon) + "_" + str(time.localtime().tm_mday)

#command = 'mv ' + str(sys.argv[1]) + "_crash " + crashReportName

#print command

#subprocess.call(command)

# clean up files
#subprocess.Popen( 'rm ' + str(sys.argv[1]) + '_hex ' + str(sys.argv[1]) + '_binary', shell=True )