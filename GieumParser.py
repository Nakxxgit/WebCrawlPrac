# clien_market_parser.py
import requests
from bs4 import BeautifulSoup
import os

url = 'http://gall.dcinside.com/board/lists/?id=tree'
header = {'User-Agent': ''}

secret = open('token.txt', 'r')
token = secret.read()

def parse_Gall():


	req = requests.get(url, headers = header)
	html = req.text
	soup = BeautifulSoup(html, 'html.parser')

	'''titles = soup.select('tbody > tr > td > a.icon_pic_n')'''

	posts = soup.select('tbody > tr.tb')

	title = posts. select('td > a.icon_pic_n').text
	link = posts.select('td > a.icon_pic_n').get('href')
	postNum = posts.select(td.t_notice)

	for post in posts:
		post.find()

	try:
		yield int(postNum.text), title, link

	except:
		pass

for n, t, l in parse_Gall():
	print(n,t,l)

'''postNums = soup.select('tbody > tr > td.t_notice')

for n in postNums:

	try:
		print(int(n.text))

	except:
		pass'''