'''
HOW TO USE THIS SCRIPT
---------------------
This script is a runner file for chromedriver.python
Please follow the instructions in chromedriver.py for individual executions
of said file.
'''

from subprocess  import Popen

processes = []

#Add extra/comment out as appropriate;
#if you've only got 2 devices plugged in, you only need 2 scripts to execute
processes.append(Popen('python chromedriver.py', shell=True))
processes.append(Popen('python chromedriver.py', shell=True))

for P in processes:
    P.wait()
