# Script to find email addresses and mobile numbers from webpages/files/endpoints . 
# The phone number regex might show false positives sometimes and recheck is required or there maybe a better regex for it :)

import requests
import re
import sys


file_url = sys.argv[1]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0'}


if '-h' in sys.argv[1] or '--h' in sys.argv[1] or '--help' in sys.argv[1] or '-help' in sys.argv[1]:
    sys.stdout.write('Usage: python3 emailphone.py <urls or endpoints file>\nexiting..\n')
    sys.exit()

else:
	with open(file_url, 'r') as f:

		for url in f.readlines():
		
			resp = requests.get(url.strip(), headers = headers)

			raw_str = str(resp.content)


			e_matches = re.findall(r'[0-9a-zA-Z+_\-.]+@[0-9a-zA-Z+_.]+[.]+[0-9a-zA-Z+_.]+[a-zA-Z]+', raw_str)

			p_matches = re.findall(r'([0-9+]{13,15}|[0-9+]{1,5} [0-9]{10}|\d{3}-\d{3}-\d{4}|[0-9+]-\d{3}-\d{3}-\d{4}|[0-9+] \d{3} \d{3} \d{4})', raw_str)


			print('\n' + 'URL:' + url + '\n' + 'Emails:::')
			for match in e_matches:
				print(match)


			print('\n' + 'URL:' + url + '\n' + 'Phone:::')
			for pmatch in p_matches:
				print(pmatch)
