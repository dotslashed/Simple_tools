# Script to find the non-common line of words/domains from two files. Calculates the uncommon ones
# python3 dupiboy.py old_file new_file
# First file is a normal file, second file is the file with more items or from which we need to find the present/unpresent

import sys


try:
	file_with_less_items = sys.argv[1]

	file_with_more_items = sys.argv[2]

	with open(file_with_less_items, 'r') as f1:
		f1_list = [x.strip() for x in f1.readlines()]

	with open(file_with_more_items, 'r') as f2:
		for y in f2.readlines():
			y2 = y.strip()
			if y2 not in f1_list:
				print(y2) 


except IndexError:
	print("Usage: python3 dupiboy.py <normal_file> <file_to_compare_with(larger one)>")
