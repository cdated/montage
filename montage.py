import os
import sys
import pwd
import requests
from lxml import html

def main(username, productivity):
    with requests.Session() as s:
        c = open('cookie').readlines()
        cookies = {}
        for line in c:
            key = line[0:line.find('=')]
            value = line[line.find('=')+1:].strip().replace(';','')
            cookies[key] = value

        r = s.get('https://www.rescuetime.com/browse/productivity/by/rank', cookies=cookies)
        tree = html.fromstring(r.text)
        score = tree.xpath('//h2[@class="efficiency-score"]/text()')

        if score:
            score = score[0]

        if int(score) < productivity:
            uid = pwd.getpwnam(username).pw_uid
            selfcontrol = "/Applications/SelfControl.app/Contents/MacOS/org.eyebeam.SelfControl " + str(uid) + " --install"
            os.system(selfcontrol)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(username=sys.argv[1])
    elif len(sys.argv) == 3:
        main(username=sys.argv[1], productivity=sys.argv[2])
    else:
        print("Usage: montage.py username [productivity]")
