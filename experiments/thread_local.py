#Testing script for Thread's local object with requests for faster http requests. Backup_stuff

import requests
from requests import Session
import threading
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
from threading import Thread,local

with open('domains.txt', 'r') as f:
	mass_urls = [line.strip() for line in f.readlines()]

thread_local = threading.local()

def get_session():
	if not hasattr(thread_local,'session'):
		thread_local.session = requests.Session()
	return thread_local.session


def gather_response(url):
	session = get_session()
	with session.get(url) as response:
		try:

			if 'Content-Length' not in response.headers or 'Content-Type' not in response.headers or 'Server' not in response.headers:
						
				print("[{}] [{}]  [] [] []".format(response.status_code, url))

			else:
						

				print("[{}] [{}]  [Server:{}] [Length:{}] [Type:{}]".format(response.status_code, url, response.headers['Server'], response.headers['Content-Length'], response.headers['Content-Type']))
		except requests.exceptions.SSLError:
			print('Error!', url)

def main(urls):
	with ThreadPoolExecutor(max_workers=10) as executor:
		executor.map(gather_response,mass_urls)

main(mass_urls)
