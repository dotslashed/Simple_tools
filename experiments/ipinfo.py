# Simple script to find details regarding an IP Address.  API used: ipapi.co

import requests
import sys

ip_add = sys.argv[1]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0'}

if '-h' in sys.argv[1] or '--h' in sys.argv[1] or '--help' in sys.argv[1] or '-help' in sys.argv[1]:
    sys.stdout.write('Usage: python3 ipinfo.py <ip_address_here>\nexiting..\n')
    sys.exit()

else:

    loc = requests.get(f'https://ipapi.co/{ip_add}/json/', headers = headers)

    loc_dict = loc.json()

    for k, v in loc_dict.items():
        print('[+]' + str(k) + ': ' + str(v))


    for key, val in loc_dict.items():
        print('[+]View in Google Maps: ' + 'https://www.google.com/maps/place/' + str(val), end = ',') if key == 'latitude' else False or print(val) if key == 'longitude' else False
        
