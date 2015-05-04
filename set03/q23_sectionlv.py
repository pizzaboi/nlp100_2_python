#! /usr/bin/python
#-*- coding: utf-8 -*-

"""
USAGE: python q20_readjson.py < jawiki-country.json.gz | python q23_sectionlv.py
"""

import re
import sys

def section_lv():
	for line in sys.stdin:
		if line.startswith('=='):
			print line.strip('= \n'), (line.count('=') / 2) - 1

if __name__ == '__main__':
	section_lv()