# Parses xml from AWS s3 and all and gives the complete file urls from the xml. Helps in quickly knowing what's inside the xml in the url.
# usage: python3 xparse.py <url which leads to xml data>
import requests
import sys
import xmltodict
import urllib3
urllib3.disable_warnings()

try:

	url = sys.argv[1]
	resp = requests.get(url)
	data = resp.content
	parsed = xmltodict.parse(data)
	list_el = parsed['ListBucketResult']['Contents']

	for item in list_el:
		print(url + '/' + item['Key'])
except IndexError:
	print('Usage: python3 xparse.py <your url>\nUrl does not contain scheme.')
