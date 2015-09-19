"""
CDME == Chrome Devtools Mobile Emulator

HOW TO USE THIS SCRIPT
----------------------
1. In a terminal, start selenium server by navigating to the directory where it
   lives and executing something like the following:
   java -jar selenium-server-standalone-2.47.1.jar

2. In another terminal, navigate to this script's location and execute it.
   python CDME.py A

   where A is the emulated device which will go into the DesiredCapabilities.

   Here's a real example:
   python CDME.py 'Samsung Galaxy S4'

   Consult Chromedevtools for further emulation possibilities.

3. This file is configured for use with CDME_runner.py
"""

import sys
import unittest
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import util


class CDME(unittest.TestCase):
    '''Run Selenium test on a Chrome Dev Tools Mobile Emulator '''	

    def setUp(self):
        print "SELENIUM CHROMEDRIVER MOBILE EMULATOR START"

        util.create_screens_dir(mobile=True)

        mobile_emulation = {
          "deviceName": sys.argv[1]
        }
        
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        dcs = chrome_options.to_capabilities()

        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
                         desired_capabilities=dcs)
        self.platform_info = "CHROMEDRIVER_MOBILE_EMULATOR_"+mobile_emulation['deviceName']+"_"

        self.wait = WebDriverWait(self.driver, 20)


    def tearDown(self):
        self.driver.quit()
        print "SELENIUM CHROMEDRIVER MOBILE EMULATOR END\n\n\n"


    def test_something(self):
        """App-specific code goes here"""

        url = "http://seleniumpythonqa.blogspot.com"
        self.driver.get(url)
        time.sleep(5)
        util.mobile_screenshot(self.driver, "test_{0}".format(self.platform_info))


if __name__ == "__main__":
    unittest.main(argv=[sys.argv[0]])
