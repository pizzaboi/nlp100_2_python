#! /usr/bin/python
#-*- coding: utf-8 -*-

"""
improved version of q21_category.py
USAGE: python q20_readjson.py < jawiki-country.json.gz | python q22_category.py
"""

import re
import sys

def extract_category():
	p = re.compile(r'\[\[Category:(.+?)[|\]]')
	for line in sys.stdin:
		if line.startswith('[[Category:'):
			print p.match(line).group(1)

if __name__ == '__main__':
	extract_category()