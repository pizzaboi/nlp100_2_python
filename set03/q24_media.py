#! /usr/bin/python
#-*- coding: utf-8 -*-

"""
USAGE: python q20_readjson.py < jawiki-country.json.gz | python q24_media.py
"""

import re
import sys

def ext_media():
	for line in sys.stdin:
		for m in re.finditer(r'([fF]ile|ファイル):(.+?)\|', line):
			print m.group(2)

if __name__ == '__main__':
	ext_media()