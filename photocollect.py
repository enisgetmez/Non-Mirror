import urllib.request
import requests
import re
import sys
from bs4 import BeautifulSoup

def download(username):
	url = "https://www.instagram.com/{}/?__a=1".format(username)
	r = requests.get(url)
	if r.ok:
		data = r.json()
		return data['graphql']['user']['profile_pic_url_hd']


def main(username):
	file_url = download(username)
	fname = username + ".jpg"
	r = requests.get(file_url, stream=True)
	if r.ok:
		with open("photos/" + fname, 'wb') as f:
			f.write(r.content)
