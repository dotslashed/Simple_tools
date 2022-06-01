#simple script to check cnames for a number of hosts within a file
import dns.resolver
import sys

file = sys.argv[1]

def main():											                #declaring function

	with open(file, 'r') as f:                  	# opens file in read mode
		for items in f.readlines():
			domains = items.strip()					          # removing extra spaces

			try:									                    # try to do this
				result = dns.resolver.resolve(domains, 'CNAME')
				for val in result:
					res = val.to_text()
					print('[{}] CNAME: {}\n'.format(domains, res.rstrip(res[-1])))                                    # removing the extra dot

			except dns.resolver.NoAnswer:			        # if any exceptions happens dont stop the program and run next
				print('[{}] CNAME: Not Found!\n'.format(domains))


if '-h' in sys.argv[1] or '--h' in sys.argv[1] or '-help' in sys.argv[1] or '--help' in sys.argv[1]:
	sys.stdout.write('Usage: python3 cname_check.py <hosts file>\nexiting..\n')                                # prints to stdout
	sys.exit()

else:
  
	main()											                                                                               # function call
