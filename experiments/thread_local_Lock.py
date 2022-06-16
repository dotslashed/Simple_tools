# Test script to learn threading Local and threading Lock object and how to make fast http requests and to learn the concurrent.futures objects

import requests
from requests import Session
import threading
from concurrent.futures import ThreadPoolExecutor
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


# Same execution of the above code using threading.Lock and executor.submit and using for loop to read file.
'''
import requests
import threading
import concurrent.futures
import sys
import time

file = sys.argv[1]
start = time.time()
def gather_response(url):
	
		try:
			
			response = requests.get(url, headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0'}, allow_redirects = False, verify = False)
			if 'Content-Length' not in response.headers or 'Content-Type' not in response.headers or 'Server' not in response.headers:
				with threading.Lock():		
					print("[{}] [{}]  [] [] []".format(response.status_code, url))

			else:
						
				with threading.Lock():
					print("[{}] [{}]  [Server:{}] [Length:{}] [Type:{}]".format(response.status_code, url, response.headers['Server'], response.headers['Content-Length'], response.headers['Content-Type']))
		except requests.exceptions.SSLError:
			print('Error!', url)


with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
	with open(file, 'r') as f:
		for line in f.readlines():
			executor.submit(gather_response, line.strip())

end = time.time()


print(end-start)

'''





