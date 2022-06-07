# Small Script to find subdomains from alienvault otx api
import requests
import sys
import json


host_name = sys.argv[1]


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0'}

if '-h' in sys.argv[1] or '--h' in sys.argv[1] or '--help' in sys.argv[1] or '-help' in sys.argv[1]:
    sys.stdout.write('Usage: python3 otxdom.py <domain_name_here>\nexiting..\n')
    sys.exit()

else:
	resp = requests.get(f'https://otx.alienvault.com/api/v1/indicators/domain/{host_name}/passive_dns', headers = headers)


	resp_json = json.loads(resp.content)

	passive_list = resp_json['passive_dns']

	doms = set()


	for item in passive_list:
		doms.add(item['hostname'])

	for dom in doms:
		print(dom)
