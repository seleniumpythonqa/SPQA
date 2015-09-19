# -*- coding: utf-8 -*-

"""
HOW TO USE THIS SCRIPT

1. Connect device(s) to your machine. Ensure the device is connected by running `adb devices`
   from a terminal. You should see something like this:
   * daemon not running. starting it now on port 5037 *
   * daemon started successfully *
   List of devices attached
   ABCD0123456789    device

2. Fire up chromedriver; if you don't already have the up-to-date binary, download it here:
   https://sites.google.com/a/chromium.org/chromedriver/downloads

   In a new terminal window, go to the directory where the chromedriver executable lives:
   ./chromedriver
   You should then see something like:
   Starting ChromeDriver 2.15.322455 (ae8db840dac8d0c453355d3d922c91adfb61df8f) on port 9515
   Only local connections are allowed.

3. In another terminal window, navigate to directory where this file lives and execute it.
        python chromedriver.py
   Make sure the device screen is unlocked, else the test won't start.

4. If required, this script can be used with chromedriver_runner.py
"""

import sys
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest

import util

class Chromedriver(unittest.TestCase):
    '''Run Selenium test on Chromedriver'''

    def setUp(self):
        print "SELENIUM CHROMEDRIVER START"

        util.create_screens_dir(mobile=True)

        capabilities = {'chromeOptions': {'androidPackage': 'com.android.chrome'}}
        capabilities['deviceOrientation'] = 'portrait'
        capabilities['rotatable'] = True
        self.driver = webdriver.Remote("http://localhost:9515", capabilities)

        user_agent = self.driver.execute_script("return navigator.userAgent;")
        op_sys = user_agent.split(";")[1]
        op_sys = "".join(op_sys.split(" "))+"_"
        device = user_agent.split(";")[2].split(" ")[1]+"_"

        self.platform_info = "CHROMEDRIVER_"+op_sys+device
        self.browser_info = self.driver.capabilities['browserName']+"_"
        self.browser_info += self.driver.capabilities['version']+"_"
        self.browser_info += capabilities['deviceOrientation']+"_"
        self.all_info = self.platform_info+self.browser_info

        self.wait = WebDriverWait(self.driver, 20)


    def tearDown(self):
        self.driver.quit()
        print "SELENIUM END\n\n\n"


    def test_something(self):
        """App-specific code goes here"""

        url = "http://seleniumpythonqa.blogspot.com"
        self.driver.get(url)
        time.sleep(5)
        util.mobile_screenshot(self.driver, "test_{0}".format(self.all_info))


if __name__ == "__main__":
    unittest.main(argv=[sys.argv[0]])

