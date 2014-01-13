#!/usr/bin/env python
# encdoing: utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep


REMOTE_SERVER = "http://localhost:4444/wd/hub"
driver = webdriver.Remote(
            command_executor=REMOTE_SERVER,
            desired_capabilities=DesiredCapabilities.FIREFOX
         )
import re

_re_IP_PORT=re.compile(r"^((?:\d|[01]?\d\d|2[0-4]\d|25[0-5])\.(?:\d|[01]?\d\d|2[0-4]\d|25[0-5])\.(?:\d|[01]?\d\d|2[0-4]\d|25[0-5])\.(?:\d|[01]?\d\d|2[0-4]\d|25[0-5])):(\d+)$")

ip_ports=set()

urls = ["http://www.cnproxy.com/proxy%(num)d.html" % {"num":i+1} for i in range(10)]
for url in urls:
    driver.get(url)
    tds = driver.find_elements_by_tag_name("td")
    for td in tds:
        if _re_IP_PORT.match(td.text):
            print td.text
            ip_ports.add(td.text)

urls = ["http://www.cybersyndrome.net/pl%(st)s.html" % {"st":st} for st in ["a5","r5","d5"]]
for url in urls:
    driver.get(url)
    aS = driver.find_elements_by_xpath("//html/body/ol/li/a")
    for a in aS:
        print a.text
        ip_ports.add(a.text)

urls=["http://www.my-proxy.com/free-proxy-list-%(num)d.html" % {"num":i+1} for i in range(10)]

for url in urls:
    driver.get(url)
    try:
        lines=driver.find_elements_by_xpath("//div[@class='content']/p[4]")[0].text.split("\n")
    except:
        continue
    for line in lines:
        if len(line) > 3 and line[-3] == "#":
            print line[:-3]
            ip_ports.add(line[:-3])

url="http://www.proxylists.net/http_highanon.txt"

driver.get(url)
for line in driver.page_source.split():
    if _re_IP_PORT.match(line):
        print line
        ip_ports.add(line)

urls = ["http://proxylist.sakura.ne.jp/index.htm?pages=%(num)d" % {"num":i} for i in range(4)]
for url in urls:
    driver.get(url)
    aS = driver.find_elements_by_xpath("//td[@id='address']")
    for a in aS:
        if _re_IP_PORT.match(a.text):
            print a.text
            ip_ports.add(a.text)
with open("proxies.lst","w") as f:
    f.write("\n".join(sorted(ip_ports)))
