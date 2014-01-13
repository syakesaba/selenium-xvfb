#!/usr/bin/env python
# encoing: utf-8

# included in selenium

import sys

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

REMOTE_SERVER = "http://127.0.0.1:4444/wd/hub"

print "Starting HTMLUNITWITHJS Broser..."
driver = webdriver.Remote(
            command_executor=REMOTE_SERVER,
            desired_capabilities=DesiredCapabilities.HTMLUNITWITHJS
         )
print "Web Browser is now ready."

try:
    import rlcompleter,atexit,os,code
    pyhistfile=os.getenv("HOME")+"/.pyhistory"
    rlcompleter.readline.parse_and_bind("tab: complete")
    rlcompleter.readline.read_history_file(pyhistfile)
    rlcompleter.readline.set_history_length(1000)
    atexit.register(rlcompleter.readline.write_history_file, pyhistfile)
    atexit.register(driver.quit)
    del os,pyhistfile
except:
    pass
sys.ps1 ="\x1B[1m\x1B[31m>\x1B[33m>\x1B[32m>\x1B[0m "
code.interact(banner="driver ENABLED!",local=locals())
