# -*- coding: utf-8 -*-

"""
HOW TO USE THIS SCRIPT
----------------------

1. In a terminal, navigate to where this script lives, then execute:
	python desktop.py
"""

import sys

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest

import util

class Desktop(unittest.TestCase):
    """  Walkthrough script for use with desktop browsers """

    def setUp(self):
        print "\nSELENIUM START {0}".format(sys.argv[0])

	#Create screenshot directory in current root if it doesn't exist
        util.create_screens_dir()

        self.driver = webdriver.Firefox()
        #self.driver = webdriver.Chrome()
        #self.driver = webdriver.Ie()
        #self.driver = webdriver.Safari()

	# Maximise the screen
        if not self.driver.capabilities['browserName'] == 'Ie':
            screen_width = self.driver.execute_script("return window.screen.availWidth;")
            screen_height = self.driver.execute_script("return window.screen.availHeight;")
            self.driver.set_window_size(screen_width, screen_height)
        else:
            self.driver.maximize_window()

        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()
        print("SELENIUM END\n\n\n")


    def test_something(self):
        """App-specific code goes here"""

        url = "http://seleniumpythonqa.blogspot.com"
        self.driver.get(url)
        util.desktop_screenshot(self.driver, "test")


if __name__ == "__main__":
    unittest.main(argv=[sys.argv[0]])

