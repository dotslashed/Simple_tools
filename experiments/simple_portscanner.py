# Simple script for port scanning. limited threads can be run.
# Usage: python3 simple_portscanner.py <target> <IP Range (eg: 50-100)>

import socket
import sys
import threading


try:
	try:

		target = socket.gethostbyname(sys.argv[1])      # try to resolve host

	except socket.gaierror:
		print('Host Seems down or Not Resolving\nexiting..\n')
		sys.exit()

	ip_range = sys.argv[2]


	start_port = int(ip_range.split('-')[0])  # splitting across - and printing the 0th item from the list

	end_port = int(ip_range.split('-')[1])	  # splitting across - and printing the 1st item from the list


	def port_scan(port):					  # defining function

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         #creating socket
		s.settimeout(3)													#leaves connection in 3 secs
		conn = s.connect_ex((target, port))

		if not conn:
			print(f'[+]Port {port} is OPEN')

		s.close()

	for port in range(start_port, end_port + 1):

		thread = threading.Thread(target = port_scan, args = (port,))         #defining the thread and on which function to use
		thread.start()                                                        # start the multi-threading

	


except IndexError:
	print('Usage: python3 simple_portscanner.py <target> <IP range>')
	sys.exit()

