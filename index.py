# coding=utf8

import util
import time
import json

def test1():
    res = util.fetch('jingyan.baidu.com', '/asyncreq?method=getRecommend&next=0&type=1')
    status = res.status

    if not(util.assertEqual(status, 200)):
        util.reportEmail('http status error:' + status)
        return

    data = json.loads(res.read())

    if util.assertEqual(data['errno'], 0):
        util.reportFile('http content error')
        return
        # util.reportEmail('http content error')

def run():
    print 'start'
    test1()
    print 'end'

count = 1   
while True:
    if count == 1:
        run()
        count = 0
        time.sleep(1)
    else:
        count += 1
        time.sleep(1)
        print count
