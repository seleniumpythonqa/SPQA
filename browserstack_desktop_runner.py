"""
HOW TO USE THIS SCRIPT
----------------------
1. See browserstack_desktop.py 
   This runner file feeds args from a text file into browserstack_desktop.py. 
   Edit your requirements in browserstack_desktops.txt, then:

	python browserstack_desktop_runner.py
"""

import subprocess

open_data = open('browserstack_desktops.txt', 'r')
count = 0

print "BROWSERSTACK DESKTOP RUNNER START"

for data in open_data:
    item = data
    if not item == "":
        count += 1
        print "Test No: {0}: {1}".format(str(count), item)
        subprocess.call('python browserstack_desktop.py {0}'.format(item), shell=True)

open_data.close()
print "BROWSERSTACK DESKTOP RUNNER END"
