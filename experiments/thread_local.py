import requests
from requests import Session
import threading
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
from threading import Thread,local
import urllib3

with open('domains.txt', 'r') as f:
	mass_urls = [line.strip() for line in f.readlines()]

thread_local = threading.local()

def get_session():
	if not hasattr(thread_local,'session'):
		thread_local.session = requests.Session()
	return thread_local.session


def gather_response(url):
	urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
	session = get_session()
	with session.get(url, headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0'}, allow_redirects = False, verify = False) as response:
		try:

			if 'Content-Length' not in response.headers or 'Content-Type' not in response.headers or 'Server' not in response.headers:
						
				print("[{}] [{}]  [] [] []".format(response.status_code, url))

			else:
						

				print("[{}] [{}]  [Server:{}] [Length:{}] [Type:{}]".format(response.status_code, url, response.headers['Server'], response.headers['Content-Length'], response.headers['Content-Type']))
		except requests.exceptions.SSLError:
			print('Error!', url)

def main(urls):
	with ThreadPoolExecutor(max_workers=2) as executor:
		executor.map(gather_response,mass_urls)

main(mass_urls)
