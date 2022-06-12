# simple script to find Content-length, type and server from response from a file of urls
import requests
import sys
import threading



file_txt = sys.argv[1]

def run(file_in):

		with open(file_txt, 'r') as f:
			
			for line in f.readlines():
				try:

					resp = requests.get(line.strip(), allow_redirects = False, verify = False, headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0'})

					if 'Content-Length' not in resp.headers or 'Content-Type' not in resp.headers or 'Server' not in resp.headers:

						print("[{}] [{}]  [] [] []".format(resp.status_code, line.strip()))

					else:
						print("[{}] [{}]  [Server:{}] [Length:{}] [Type:{}]".format(resp.status_code, line.strip(), resp.headers['Server'], resp.headers['Content-Length'], resp.headers['Content-Type']))

				except requests.exceptions.SSLError:
					print('[ERR] Check manually', line)


if '-h' in sys.argv[1] or '--h' in sys.argv[1] or '--help' in sys.argv[1]:
	sys.stdout.write('[Usage]: python3 scc.py <urls.txt>\nexiting..\n')
	sys.exit()

run(file_txt)
