import requests
from bs4 import BeautifulSoup as bs

with requests.Session() as s:

	payload = {
		'login_user_id' : 'username',
		'login_password' : 'password',
		'next' : '/'
	}

	login_req = s.post("https://www.acmicpc.net/signin", data=payload)
	resp = s.get("https://www.acmicpc.net/")

	soup = bs(resp.content, 'html.parser')
	menu_user_name = soup.select_one('body > div.wrapper > div.header.no-print > div.topbar > div > ul > li > a')

	print(menu_user_name.text)