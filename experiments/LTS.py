# simple script to find Content-length, type and server from response from a file of urls
import requests
import sys




file_txt = sys.argv[1]

def run():

		with open(file_txt, 'r') as f:
			
			for line in f.readlines():

				resp = requests.get(line.strip(), allow_redirects = False)

				if 'Content-Length' not in resp.headers or 'Content-Type' not in resp.headers or 'Server' not in resp.headers:

					print("[{}] [{}]  [] [] []".format(resp.status_code, line.strip()))

				else:
					print("[{}] [{}]  [Server:{}] [Length:{}] [Type:{}]".format(resp.status_code, line.strip(), resp.headers['Server'], resp.headers['Content-Length'], resp.headers['Content-Type']))



if '-h' in sys.argv[1] or '--h' in sys.argv[1] or '--help' in sys.argv[1]:
	sys.stdout.write('[Usage]: python3 scc.py <urls.txt>\nexiting..\n')
	sys.exit()

else:

	run()
