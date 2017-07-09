# parser.py
import requests
from bs4 import BeautifulSoup
import json

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WebSaver.settings")
import django
django.setup()

from treeGallParse.models import PostData

def parse_Gall():
	
	url = 'http://gall.dcinside.com/board/lists/?id=tree'
	header = {'User-Agent': ''}


	req = requests.get(url, headers = header)
	html = req.text
	soup = BeautifulSoup(html, 'html.parser')

	posts = soup.select('tbody > tr')

	# select class = "tb"

	for post in posts: # for post in "tb":
		                 # title link PostNum
	    link = title.get('href')

	    yield title, link, PostNum

if __name__=='__main__':
	gall_data_dict, PostNum = parse_Gall()

	for t, l in gall_data_dict.items():
		PostData(title=t, link='http://gall.dcinside.com/' + l)

	for n in PostNum:
		try:
			PostData(PostNum = int(n.text)).save()
		except:
			pass