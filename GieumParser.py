# clien_market_parser.py
import requests
from bs4 import BeautifulSoup
import os

url = 'http://gall.dcinside.com/board/lists/?id=food'
header = {'User-Agent': ''}

def parse_Gall():
	req = requests.get(url, headers = header)
	html = req.text
	soup = BeautifulSoup(html, "html.parser")

	'''titles = soup.select('tbody > tr > td > a.icon_pic_n')'''

	posts_n = soup.find_all(attrs={"class": "t_notice"})
	posts_t = soup.find_all(attrs={"class": "t_subject"})

	return posts_n, posts_t

for n, t in zip(parse_Gall()):
	try:
		print(int(n.text))
		print(t.text)
	except:
		pass

'''	try:
		yield int(postNum.text), title, link

	except:
		pass

for n, t, l in parse_Gall():
	print(n,t,l)

postNums = soup.select('tbody > tr > td.t_notice')

for n in postNums:

	try:
		print(int(n.text))

	except:
		pass'''