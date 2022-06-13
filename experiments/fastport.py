# Script to scan ports in a fast way; Learning to use the socket, threading and concurrent.futures object
# Usage: python3 fastport.py <target> <port range,eg:1-1000> <max-workers int>

import socket
import threading
import concurrent.futures
import sys



try:

	target = sys.argv[1]

	ip_range = sys.argv[2]

	workers = int(sys.argv[3])

	start_port = int(ip_range.split('-')[0])  # splitting across - and printing the 0th item from the list

	end_port = int(ip_range.split('-')[1])	  # splitting across - and printing the 1st item from the list


	def scan(port):

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)          # creating a socket to communicate.

		try:

			s.settimeout(3)

			s.connect((target, port))

			s.close()                                                # if connection happens close the connection and print the below

			with threading.Lock():                                   # prevents printing extra and prints on lines
				print(f'port {port} is open')

		except:
			pass													                           # if any execptions occur pass it and continue scan


	with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:        # putting the long object into a variable executor
		for port in range(start_port, end_port + 1):
			executor.submit(scan, port)


except IndexError:
	print('Usage: python3 fastport.py <target> <port range,eg:1-1000> <max-workers int>')


