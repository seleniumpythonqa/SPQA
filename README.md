# SPQA
This mini-framework contains a number of helper files for Selenium automation with Python.              
Instructions for use are included at the top of each file.

## Assumptions, Notes, Caveats
All requisite PY libs installed (any that aren't will be flagged)

The following are up-to-date, installed and on your path:
- Chromedriver 
- Selenium Server
- IE driver

You will also have up-to-date versions of
- Selendroid
- Chrome

You have the following installed:
- Selenium IDE for Firefox
- Android SDK (operable via command line), and required emaultors (AVDs)

###Appium 
Code was tested on OSX10.10, XCODE 6.4 and Appium 1.4.8  
Appium DMG available here:
https://bitbucket.org/appium/appium.app/downloads/  
You will have the required simulators installed.

###Browserstack  
See www.browserstack.com          
You will require (or already have) an account whose plan includes automation, and an associated username and access key

###Safari   
For tips on using Safari with Selenium, please see:
http://elementalselenium.com/tips/69-safari   
**NB** Your `SELENIUM_SERVER_JAR` env var and the Safari extension will have to tally.
For example, if the latest version of the extension is 2.45, you'll need to [temporarily] set your `SELENIUM_SERVER_JAR` to `selenium-server-standalone-2.45.0.jar`

###Linting  
To ensure maximum pylint compliance, the scripts in this repo are 'bare bones'; 
please add whatever imports are required as your app code grows.

The imports area of a complete script might look something like this:
```
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.touch_actions import TouchActions
```
 
**util.py**  
This utility file contains a number of functions used throughout the mini-framework.

###Comments & Suggestions  
Feedback most welcome. 

