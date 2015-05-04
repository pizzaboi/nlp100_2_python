#! /usr/bin/python
#-*- coding: utf-8 -*-

"""
USAGE: python q20_readjson.py < jawiki-country.json.gz | python q21_category.py
"""

import sys

def extract_category():
	for line in sys.stdin:
		if line.startswith('[[Category:'):
			print line.strip('\n')

if __name__ == '__main__':
	extract_category()