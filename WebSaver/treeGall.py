# parser.py
import requests
from bs4 import BeautifulSoup
import json

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WebSaver.settings")
import django
import time
django.setup()

from treeGallParse.models import PostData

def parse_Gall():

    url = 'http://gall.dcinside.com/board/lists/?id=tree'
    header = {'User-Agent': ''}


    req = requests.get(url, headers = header)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    numS = soup.find_all("td", {"class": "t_notice"})
    titleS = soup.find_all("td", {"class": "t_subject"})

    a = 0
    for num in numS:
        try:
            int(num.text)
        except:
            numS[a] = None
        a += 1

    a = 0
    for t in titleS:
        if 'b>' in str(t):
            titleS[a] = None
        a +=1

    titleS = list(filter(None, titleS))
    numS = list(filter(None, numS))  # remove blank Elements

    n = numS[0].text
    t = titleS[0].text
    l = 'http://gall.dcinside.com/board/view/?id=tree&no=' + n

    return n, t, l

if __name__=='__main__':
    while True:
        n, t, l = parse_Gall()
        latest = PostData.objects.order_by('-PostNum')[0]
        print(latest.PostNum)
        if(int(n) != latest.PostNum):
            PostData(title = t, link = l, PostNum = n).save()
            print("새 게시글이 업데이트 되었습니다! 글 제목: ", t)
        else:
            print("업데이트된 게시글이 없습니다", latest, t)

        time.sleep(10)