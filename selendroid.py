"""
HOW TO USE THIS SCRIPT
----------------------

1. Connect device to your machine.
   Ensure the device is connected by running `> adb devices` from a terminal.
   You should see something like this:
   * daemon not running. starting it now on port 5037 *
   * daemon started successfully *
   List of devices attached
   ADCD0123456789    device

2. In a terminal, navigate to the location of your selendroid server and start it up:
   > java -jar selendroid-standalone-0.16.0-with-dependencies.jar

3. In another terminal, navigate to this script and execute it.
   > python selendroid.py
   Make sure the device screen is unlocked, else the test won't start.
"""

import subprocess
import sys
import time
import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

import util

class Selendroid(unittest.TestCase):
    """Run Selenium/Selendroid test on Default Android Browser"""

    def setUp(self):
        print "SELENIUM/SELENDROID START"

        util.create_screens_dir(mobile=True)

        os_version = "A"
        proc = 'adb shell getprop ro.build.version.release'
        os_version_to_stdout = subprocess.Popen(proc, shell=True, stdout=subprocess.PIPE,)
        os_version += os_version_to_stdout.communicate()[0].strip()
        proc = 'adb shell getprop ro.product.model'
        device_to_stdout = subprocess.Popen(proc, shell=True, stdout=subprocess.PIPE,)
        device = device_to_stdout.communicate()[0].replace(" ", "").strip()

        self.dcs = {'platform': 'ANDROID', 'browserName': 'android', 'version':''}
        self.driver = webdriver.Remote(desired_capabilities=self.dcs)

        self.platform_info = "SELENDROID_"+os_version+"_"+device+"_"

        self.wait = WebDriverWait(self.driver, 20)


    def tearDown(self):
        self.driver.quit()
        print "SELENIUM/SELENDROID END\n\n\n"


    def test_something(self):
        '''App-specific code goes here'''

        url = "http://seleniumpythonqa.blogspot.com"
        self.driver.get(url)

        time.sleep(5)
        util.mobile_screenshot(self.driver, "test_{0}".format(self.platform_info))


if __name__ == '__main__':
    unittest.main(argv=[sys.argv[0]])
