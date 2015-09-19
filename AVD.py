"""
HOW TO USE THIS SCRIPT
----------------------

Terminal 1:
> android

Terminal 2:
> cd sdk/tools
> emulator -avd INSERT_AVD_NAME_HERE
Allow emaultor to boot up. Be patient.
When it does boot up, ensure the screen is unlocked.

Terminal 3 - Start Selenium server in present directory, eg:
> java -jar selendroid-standalone-0.16.0-with-dependencies.jar -deviceScreenshot
If a newer version of selendroid causes problems, have a look here:
https://github.com/selendroid/selendroid/issues/646
Don't omit the -deviceScreenshot flag

Terminal 4:
Run AVD.py (this directory)

Repeat steps 2 & 4 for successive emulators.
Edit AVD.py, including the [emaultor_identifier] as 'avdName' in the following line:
self.DC = {'platform': 'ANDROID',
	   'browserName': 'android',
           'version':'',
	   'emulator':True,
	   'avdName':'INSERT_AVD_NAME_HERE'}

If execution is brittle, a complete restart (steps 1-4) may be required from time to time.

"""

import subprocess
import sys
import time
import unittest

from selenium import webdriver

import util

class AVD(unittest.TestCase):
    '''Run Selenium test on an Android Virtual Device
    '''

    def setUp(self):
        print "SELENIUM AVD START"

        util.create_screens_dir(mobile=True)

        os_version = "A"
        proc = 'adb shell getprop ro.build.version.release'
        os_version_to_stdout = subprocess.Popen(proc, shell=True, stdout=subprocess.PIPE,)
        os_version += os_version_to_stdout.communicate()[0].strip()
        print "OS_version:", os_version
        proc = 'adb shell getprop ro.product.model'
        device_to_stdout = subprocess.Popen(proc, shell=True, stdout=subprocess.PIPE,)
        device = device_to_stdout.communicate()[0].replace(" ", "").strip()
        print "device:", device

        self.dcs = {'platform': 'ANDROID',
		   'browserName': 'android',
		   'version':'',
		   'emulator':True,
		   'avdName':'INSERT_AVD_NAME_HERE'}
        self.driver = webdriver.Remote(desired_capabilities=self.dcs)
        self.platform_info = "AVD_"+os_version+"_"
        self.browser_info = self.driver.capabilities['browserName']+"_"
        self.browser_info += self.driver.capabilities['avdName']
        self.device_info = self.platform_info+self.driver.capabilities['avdName']

    def tearDown(self):
        self.driver.quit()
        print "SELENIUM AVD END\n\n\n"


    def test_something(self):
        '''App-specific code goes here'''

        url = "http://seleniumpythonqa.blogspot.com"
        self.driver.get(url)

        time.sleep(5)
        util.mobile_screenshot(self.driver, "test_{0}_".format(self.device_info))
        time.sleep(2)


if __name__ == '__main__':
    unittest.main(argv=[sys.argv[0]])

