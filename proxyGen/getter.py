#!/usr/bin/enb python
# encoding: utf-8

import urllib2
import time
import os

PROXIES_LIST="proxies.lst"

def getHttpProxyHandlers():
    with open( PROXIES_LIST ) as f:
        for line in f:
            yield urllib2.ProxyHandler( {"http":line.strip()} )

def getOpeners():
    for httpProxyHandler in getHttpProxyHandlers():
        opener = urllib2.build_opener(httpProxyHandler)
        opener.addheaders= [("User-agent","Mozilla/5.0 (iPhone; CPU iPhone OS 5_1_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B206 Safari/7534.48.3"),
                        ("Referer","http://jkpc.gl-inc.jp/?page_id=261&event_id=10003&card_id=1030"),
                        ("X-Requested-With","XMLHttpRequest"),
                        ("Content-Type","application/x-www-form-urlencoded; charset=UTF-8")
                        ]
        yield opener

def getter(opener, url, timeout):
    return opener.open(url,timeout=timeout)

def poster(opener, url, body, timeout):
    return op.open(url,data=body,timeout=timeout)

import threading

for opener in getOpeners():
    print opener
    url="http://www.firefly.kutc.kansai-u.ac.jp/~k843966/"
    try:
        getter(opener, url,timeout=10)
    except:
        pass
