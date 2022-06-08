# This script finds domains related to an organization by searching it by the organization's name
# Example:  python3 orgdom.py "google inc" . If details are present it'll output else not. A cross check of the domain registrar is still required sometimes.

import requests
import sys



org_name = sys.argv[1]


def main(org):

	resp = requests.get(f'https://crt.sh/?o={org}&output=json')

	resp_list = resp.json()

	doms = set()

	for element in resp_list:	
		doms.add(element['common_name'])

	for i in doms:
		no_star = i.replace('*.', '')

		print(no_star)



if '-h' in sys.argv[1] or '--h' in sys.argv[1] or '--help' in sys.argv[1] or '-help' in sys.argv[1]:
    sys.stdout.write('Usage: python3 orgdom.py "organization name here in quotes"\nexiting..\n')
    sys.exit()


else:
	main(org_name)
