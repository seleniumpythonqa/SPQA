# -*- coding: utf-8 -*-

"""
HOW TO USE THIS SCRIPT

1. Open XCODE on your Mac.

2. Open the Appium App and launch it in iOS mode.
   (It's recommended that you use the Appium DMG and install it in your Applications folder.
   https://bitbucket.org/appium/appium.app/downloads/
   It's more user-friendly than using the terminal.)

3. In a terminal, navigate to this script's location and execute it.
   python appium.py A B C

   where
   A is the required version of OS
   B the device
   C the device orientation

   Here's a real example.
   python appium.py 8.4 "iPad Air" portrait

NOTE: Appium can be slow on initial start up and the first few tests.
"""

import sys
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest

import util

class Appium(unittest.TestCase):
    '''Run Selenium test on an Appium iOS Simulator'''

    def setUp(self):
        print "SELENIUM APPIUM START"

        util.create_screens_dir(mobile=True)

        #Desired Capabilities
        self.dcs = {
            'platformName' : 'iOS',
            'platformVersion' : sys.argv[1],
            'deviceName' : sys.argv[2],
            'browserName' : 'Safari',
            'deviceOrientation': sys.argv[3]
        }

        cex = 'http://127.0.0.1:4723/wd/hub'
        self.driver = webdriver.Remote(command_executor=cex, desired_capabilities=self.dcs)
        self.platform_info = "APPIUM_"
        self.browser_info = self.dcs['platformName']+"_"+self.dcs['platformVersion']+"_"
        self.browser_info += self.dcs['deviceName']+"_"
        self.browser_info += self.dcs['browserName']+"_"+self.dcs['deviceOrientation']+"_"
        self.all_info = self.platform_info + self.browser_info

        self.wait = WebDriverWait(self.driver, 20)


    def tearDown(self):
        self.driver.quit()
        print "SELENIUM APPIUM END\n\n\n"


    def test_something(self):
        """ Add your tests here """

        url = "http://seleniumpythonqa.blogspot.com"
        self.driver.get(url)
        util.mobile_screenshot(self.driver, "test_{0}".format(self.all_info))
        time.sleep(2)


if __name__ == "__main__":
    unittest.main(argv=[sys.argv[0]])
