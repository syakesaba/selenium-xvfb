#!/usr/bin/env python
# encdoing: utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep


REMOTE_SERVER = "http://127.0.0.1:4444/wd/hub"

print "Starting Web Broser..."
driver = webdriver.Remote(
            command_executor=REMOTE_SERVER,
            desired_capabilities=DesiredCapabilities.FIREFOX
         )
print "Web Browser is now ready. Sleeping 1 seconds..."
sleep(1)
print "Done."


import re

_re_IP_PORT=re.compile(r"^((?:\d|[01]?\d\d|2[0-4]\d|25[0-5])\.(?:\d|[01]?\d\d|2[0-4]\d|25[0-5])\.(?:\d|[01]?\d\d|2[0-4]\d|25[0-5])\.(?:\d|[01]?\d\d|2[0-4]\d|25[0-5])):(\d+)$")

ip_ports=set()

url="http://www.proxylists.net/http_highanon.txt"

driver.get(url)
for line in driver.page_source.split():
    if _re_IP_PORT.match(line):
        print line
        ip_ports.add(line)

print "done"

try:
    import rlcompleter,atexit,os,code
    pyhistfile=os.getenv("HOME")+"/.pyhistory"
    rlcompleter.readline.parse_and_bind("tab: complete")
    rlcompleter.readline.read_history_file(pyhistfile)
    rlcompleter.readline.set_history_length(1000)
    atexit.register(rlcompleter.readline.write_history_file, pyhistfile)
    atexit.register(driver.close)
    del os,pyhistfile
except:
    pass


code.interact(local=locals())
