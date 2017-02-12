# coding=utf8

import util
import time
import json
from urlparse import urlparse
def geturl():
    f = open('urlTest.txt','r')
    urls = f.readlines()
    f.close()
    for i in range(0,len(urls)):
        test_url = urls[i].strip().split(',')
        hostname = urlparse(test_url[0]).netloc
        path = urlparse(test_url[0]).path + '?' + urlparse(test_url[0]).query
        res = util.fetch(hostname, path)
        
        if not(util.assertEqual(res.status, int(test_url[1]))):
            # util.reportEmail('http status error:' + status)
            print 'failed', test_url[0]
        else:
            print 'success', test_url[0]


def run():
    geturl()
    

count = 0
while True:
    count += 1
    print 'start:', count
    run()
    print 'end:', count
    time.sleep(1)