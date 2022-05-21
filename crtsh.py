import requests
import sys


target_name = sys.argv[1]

if '.' not in sys.argv[1] or '-h' in sys.argv[1] or '--help' in sys.argv[0] :

	sys.stdout.write("Usage: python3 crtsh.py [domain.name]\nExiting..\n")

	sys.exit()

else:
	resp = requests.get(f"https://crt.sh/?q={target_name}&output=json")

	data_dict = resp.json()
	new = []
	[new.append(line['common_name']) for line in data_dict if line['common_name'] not in new]


	for item in new:
		no_star = item.replace('*.', '')
		if f"{target_name}" in no_star:
			print(no_star)
			
