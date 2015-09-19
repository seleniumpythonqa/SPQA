"""
HOW TO USE THIS SCRIPT
----------------------
1. See browserstack_mobile.py 
   This runner file feeds args from a text file into browserstack_mobile.py. 
   Edit your requirements in browserstack_mobiles.txt, then:

	python browserstack_mobile_runner.py
"""

import subprocess

open_data = open('browserstack_mobiles.txt', 'r')
count = 0

print "BROWSERSTACK MOBILE RUNNER START"

for item in open_data:
    if item is not "":
        count += 1
        print "Test No: {0}: {1}".format(str(count), item)
        subprocess.call('python browserstack_mobile.py {0}'.format(item), shell=True)

open_data.close()
print "BROWSERSTACK MOBILE RUNNER END"
