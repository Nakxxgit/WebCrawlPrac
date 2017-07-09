# clien_market_parser.py
import requests
from bs4 import BeautifulSoup
import os
import time
import datetime

import telegram

secret = open('token.txt', 'r')
token = secret.readline()

bot = telegram.Bot(token = token)
chat_id = bot.getUpdates()[-1].message.chat.id

url = 'http://gall.dcinside.com/board/lists/?id=tree'
header = {'User-Agent': ''}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print(bot)

while True:
	now = datetime.datetime.now()
	now = now.strftime('%Y-%m-%d %H:%M:%S')

	req = requests.get(url, headers = header)
	html = req.text
	soup = BeautifulSoup(html, 'html.parser')
	posts = soup.select('tbody > tr > td.t_subject')
	a = 0
	for post in posts:

		post = str(post)
		if ('</b>' in post) :
			posts[a] = None
		a += 1

	posts = list(filter(None, posts)) # fastest

	latest_title = posts[0].text
	latest_title = latest_title[:latest_title.find('[')]
				
	print(now + ' ' +  latest_title)

	with open(os.path.join(BASE_DIR, 'latest.txt'), 'r+') as f_read:
	    before = f_read.read()
	    if before != latest_title:
	    	bot.sendMessage(chat_id=chat_id, text="새 글이 올라왔어요!\n'" + latest_title + "'\n" + now)

	with open(os.path.join(BASE_DIR, 'latest.txt'), 'w+') as f_write:
	    f_write.write(latest_title)

	time.sleep(10)