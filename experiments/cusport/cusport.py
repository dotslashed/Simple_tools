# Portscanner using custom ports file, scan domains and IP addresses, usage: python3 cusport.py <domain/IP(or file with targets/IPs)> <ports file> <max-workers>
# ports file can be found here: https://gist.githubusercontent.com/s0md3v/3e953e8e15afebc1879a2245e74fc90f/raw/1e20288e9bef43b60f7306b6f7e23044dabd9b8c/shodan_ports.txt [by @s0md3v]

import socket
import threading
import concurrent.futures
import sys
import time
import os
from colorama import Fore


print(Fore.WHITE + '=' * 100)
print(Fore.GREEN + '\t' *4 + 'Port Scanner using Custom ports file')
print(Fore.WHITE + '=' * 100 + '\n')

try:

	target_file = sys.argv[1]
	ports_file = sys.argv[2]
	workers = int(sys.argv[3])
	start = time.time()

	def scan(target, port):

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)          # creating a socket to communicate.

		try:

			s.settimeout(3)

			s.connect((target, port))

			s.close()

			with threading.Lock():                                   # prevents printing extra and prints on lines
				print(f'port {port} is' + Fore.GREEN + ' open' + Fore.WHITE  + f' {target}:{port}')

		except:
			pass													# if any execptions occur pass it and continue scan


	def single_target():                           # scan single target
		with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:        # putting the long object into a variable executor
			with open(ports_file, 'r') as f:
				for port in f.readlines():
					executor.submit(scan, target_file, int(port.strip()))


	def file_target():	                           # scan targets from list
		with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
			with open(ports_file, 'r') as f1, open(target_file, 'r') as f2:
				port_line = f1.readlines()
				target_line = f2.readlines()
			for targ in target_line:
				for por in port_line:
					executor.submit(scan, targ.strip(), int(por.strip()))

	if os.path.isfile(target_file):
		file_target()
	else:
		single_target()


	end = time.time()
	print('\n===Completed in {0:.3f} seconds==='.format(end - start))

except IndexError:
	print('Usage: python3 cusport.py <target> <custom ports file> <max-workers int>')

