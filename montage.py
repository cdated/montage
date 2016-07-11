#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import pwd
import requests
import datetime
from lxml import html
from lxml import etree

def main(cookie, username, productivity):
    with requests.Session() as s:
        c = open(cookie).readlines()
        cookies = {}
        for line in c:
            key = line[0:line.find('=')]
            value = line[line.find('=')+1:].strip().replace(';','')
            cookies[key] = value

        date = datetime.datetime.now()
        datestr = str(date).split(' ')[0].replace('-0', '-')
        url = 'https://www.rescuetime.com/dashboard/for/the/day/of/' + datestr
        r = s.get(url, cookies=cookies)
        tree = html.fromstring(r.text)
        elem = tree.find_class('productivity-score-chart')
        score = elem[0].get("data-productivity-score")

        if score:
            if int(score) < productivity:
                uid = pwd.getpwnam(username).pw_uid
                selfcontrol = "/Applications/SelfControl.app/Contents/" + \
                        "MacOS/org.eyebeam.SelfControl %s --install" % str(uid)
                os.system(selfcontrol)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        main(cookie=sys.argv[1], username=sys.argv[2])
    elif len(sys.argv) == 4:
        main(cookie=sys.argv[1], username=sys.argv[2], productivity=sys.argv[3])
    else:
        print("Usage: montage.py cookie username [productivity]")
