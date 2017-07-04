# parser.py
import requests
from bs4 import BeautifulSoup
import json

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WebSaver.settings")
import django
django.setup()

from parsed_data.models import BlogData

def parse_blog():
	# HTTP GET Request
	req = requests.get('https://nakxxblog.wordpress.com/')
	# HTML 소스 가져오기
	html = req.text

	soup = BeautifulSoup(html, 'html.parser')

	my_titles = soup.select(
		'div.post-header > h2 > a'
		)

	data = {}

	for title in my_titles:
	    data[title.text] = title.get('href')
	return data

if __name__=='__main__':
    blog_data_dict = parse_blog()
    for t, l in blog_data_dict.items():
        BlogData(title=t, link=l).save()
