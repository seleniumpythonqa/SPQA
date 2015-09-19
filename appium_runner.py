"""
HOW TO USE THIS SCRIPT
----------------------
1. appium.py
   This runner file feeds args from a text file into appium.py
   Edit your requirements in appium.txt, then:

	python appium_runner.py
"""

import subprocess

open_data = open('appium.txt', 'r')
count = 0

print "APPIUM RUNNER START"

for item in open_data:
    if not item == "":
        count += 1
        print "Test No: " + str(count)
        subprocess.call('python appium.py {0}'.format(item), shell=True)

open_data.close()
print "APPIUM RUNNER END"
