# clien_market_parser.py
import requests
from bs4 import BeautifulSoup
import os
import time


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


while True:
	req = requests.get('https://www.clien.net/service/board/sold')
	req.encoding = 'utf-8'

	html = req.text
	soup = BeautifulSoup(html, 'html.parser')
	posts = soup.select('body > div.nav-container > div > div.content > div.card-grid > div > div > div > div.list-title > a')

	latest_list = posts[0].text.split()

	post_type = latest_list[0].strip()
	title = ' '.join(latest_list[1:]).strip()

	latest_post_info = str(latest_list[0]) + '\n' + ' '.join(latest_list[1:])

	print(latest_post_info)

	with open(os.path.join(BASE_DIR, 'latest.txt'), 'r+') as f_read:
	    before = f_read.read()
	    if before != latest_post_info:

	with open(os.path.join(BASE_DIR, 'latest.txt'), 'w+') as f_write:
	    f_write.write(latest_post_info)

	time.sleep(60)