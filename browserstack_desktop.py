# -*- coding: utf-8 -*-

"""
HOW TO USE THIS SCRIPT
----------------------

1. If testing on localhost, set ['browserstack.local' = True]
   in our Desired Capabilities. See Browserstack.dcs at the end of this file.

2. Start up BrowserStackLocal; see https://www.browserstack.com/local-testing#configuration
   If you don't already have the binary, download and unzip it.
   In a terminal, navigate to the directory where the unzipped app lives.
   ./BrowserStackLocal YOUR_ACCESS_KEY_HERE

3. In another terminal, navigate to the directory where this file lives and execute:
   python browserstack.py A B C D

   where:
   A is the required OS
   B the OS version
   C the browser
   D the browser version.
   Again, see Browserstack.DC, at the end of this file.

   Here's a real example:
   python browserstack.py OSX Mavericks Chrome 39

   See https://www.browserstack.com/automate/python for the various OS/browser combinations.

4. If you're not testing via localhost, ignore 1. & 2. above and proceed with 3.

5. This file is configured for use with browserstack_desktop_runner.py

"""

import sys
from time import strftime

import unittest
from selenium import webdriver

import util

class Browserstack(unittest.TestCase):
    """Run Selenium test on www.browserstack.com, see above."""

    def setUp(self):
        print "SELENIUM BROWSERSTACK START"

        util.create_screens_dir()

        cex = "http://USERNAME:ACCESS_KEY@hub.browserstack.com:80/wd/hub"
        self.driver = webdriver.Remote(command_executor=cex, desired_capabilities=self.dcs)

        self.platform_info = "BROWSERSTACK_"+self.dcs['os']+"_"+self.dcs['os_version']+"_"
        self.browser_info = self.driver.capabilities['browserName']+"_"
        self.browser_info += self.driver.capabilities['version']+"_"
        self.all_info = self.platform_info+self.browser_info

    def tearDown(self):
        self.driver.quit()
        print "SELENIUM BROWSERSTACK END\n\n\n"


    def test_something(self):
        """App-specific code goes here"""

        url = "http://seleniumpythonqa.blogspot.com"
        self.driver.get(url)
        util.browserstack_screenshot(self.driver, "test_{0}".format(self.all_info))


if __name__ == '__main__':
    NICE_DATE = strftime("%d%m%y")
    Browserstack.dcs = {
        'os' : sys.argv[1],
        'os_version' : sys.argv[2],
        'browser' : sys.argv[3],
        'browser_version' : sys.argv[4],
        'resolution': '1280x1024',
	'build': 'Build Name Here - Desktops, {0}'.format(NICE_DATE),
        'project': 'Project Name Goes Here',
        'name': '{0} {1} {2} {3}'.format(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

	#Other caps
	#'browserstack.debug' : 'true',
	#'browserstack.local' = True
    }
    unittest.main(argv=[sys.argv[0]])


