# Small script to gather urls from waybackmachine api
import requests
import sys




domain_name = sys.argv[1]

def enumerate(domain):
	resp = requests.get(f'http://web.archive.org/cdx/search/cdx?url=*.{domain}/*&output=json&fl=original&collapse=urlkey')

	url_list = resp.json()

	sub_list = [y for x in url_list for y in x]

	sub_list.remove('original')

	set_urls = set()

	for url in sub_list:
		set_urls.add(url)

	for urls in set_urls:
		print(urls)

if '-h' in sys.argv[1] or '--h' in sys.argv[1] or '--help' in sys.argv[1] or '-help' in sys.argv[1]:
    sys.stdout.write('Usage: python3 wayback.py <domainName>\nexiting..\n')
    sys.exit()

else:

	enumerate(domain_name)

