"""
HOW TO USE THIS SCRIPT
----------------------
1. See CDME.py 
   This runner file feeds args from a text file into CDME.py. 
   Edit your requirements in CDME.txt, then:

	python CDME_runner.py
"""

import subprocess

open_data = open('CDME.txt', 'r')
count = 0

print "CDME RUNNER START"

for item in open_data:
    if not item == "":
        count += 1
        print "Test No: {0}: {1}".format(str(count), item)
        subprocess.call('python CDME.py {0}'.format(item), shell=True)

open_data.close()
print "CDME RUNNER END"
