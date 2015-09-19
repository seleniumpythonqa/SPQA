# -*- coding: utf-8 -*-

"""
HOW TO USE THIS SCRIPT
----------------------

1. If testing on localhost, set ['browserstack.local' = True] in our Desired Capabilities.
   See Browserstack.dcs, at the end of this file.
   If not testing on localhost, proceed to step 3.

2. Start up BrowserStackLocal; see https://www.browserstack.com/local-testing#configuration
   If you don't already have the binary, download and unzip it.
   In a terminal, navigate to the directory where the unzipped binary lives.
   ./BrowserStackLocal YOUR_ACCESS_HERE

3. In another terminal, navigate to the directory where this file lives and execute:
   python browserstack.py A B C

   where:
   A is the required OS
   B the device
   C the browser
   Again, see Browserstack.DC, at the end of this file.

   Examples:
   python browserstack_mobile.py 'Android' 'Samsung Galaxy S5' 'android'
   python browserstack_mobile.py  'Mac' 'iPhone 5C' 'iPhone'

   See https://www.browserstack.com/automate/python for the various OS/browser combinations.

4. This file is configured for use with browserstack_mobile_runner.py

"""

import sys
import time
from time import strftime

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

import util

class BrowserstackMobile(unittest.TestCase):
    """Run Selenium test on www.browserstack.com, see above."""

    def setUp(self):
        print "SELENIUM BROWSERSTACK MOBILE START"

        util.create_screens_dir(mobile=True)

        cex = "http://USERNAME:ACCESS_KEY@hub.browserstack.com:80/wd/hub"
        self.driver = webdriver.Remote(command_executor=cex, desired_capabilities=self.dcs)

        op_sys = sys.argv[1]
        if op_sys == 'Mac':
            op_sys = 'iOS'
        self.platform_info = "BROWSERSTACK_MOBILE_"+op_sys+"_"+sys.argv[2]+"_"
        self.browser_info = ""
        if sys.argv[1] == "Mac":
            self.browser_info = "safari_"
        else:
            self.browser_info = "default_or_chrome_"
        self.all_info = self.platform_info+self.browser_info

        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()
        print "SELENIUM BROWSERSTACK MOBILE END\n\n\n"


    def test_something(self):
        """App-specific code goes here"""

        url = "http://seleniumpythonqa.blogspot.com"
        self.driver.get(url)
        time.sleep(5)
        util.browserstack_screenshot(self.driver, "test_{0}".format(self.all_info), mobile=True)


if __name__ == '__main__':
    NICE_DATE = strftime("%d%m%y")
    BrowserstackMobile.dcs = {
                          'platform' : sys.argv[1],
                          'device' : sys.argv[2],
                          'browserName' : sys.argv[3],
                          'deviceOrientation' : 'portrait',
	                  'build': 'Build Name Here - Mobile, {0}'.format(NICE_DATE),
                          'project': 'Project Name Goes Here',
                          'name': '{0} {1} {2}'.format(sys.argv[1], sys.argv[2], sys.argv[3])

                          # Additional Caps
                          #'browserstack.local' : True
                          #'browserstack.debug' : 'true'
    }
unittest.main(argv=[sys.argv[0]])

