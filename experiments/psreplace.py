# A script to replicate tomnomnom's qsreplace tool. I tried this just for fun.
# Usage: python3 psreplace.py urls.txt http://xxx.burpcollaborator.net
# import requests
import sys

try:

	file = sys.argv[1]
	repl_str = sys.argv[2]

except IndexError:
	pass

if '-h' in sys.argv[1] or '--h' in sys.argv[1] or '--help' in sys.argv[1] or '-help' in sys.argv[1]:
    sys.stdout.write('Usage: python3 psreplace.py <urls file> <string to replace param value with>\nexiting..\n')
    sys.exit()

else:

	with open(file, 'r') as f:
		for x in f.readlines():
			# print(x.strip())

			if '=' in x.strip():

				split_url = x.strip().split('?')

				params = split_url[1].split('&')

				e = []
				for item in params:
					param_val = item.split('=')
				
					param_val[1] = f'{repl_str}'
					partial = "=".join(param_val)
					e.append(partial)

			

				tail_join = "&".join(e)
				print(split_url[0] + '?' + tail_join)


			else:
				continue
