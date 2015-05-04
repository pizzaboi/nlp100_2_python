#! /usr/bin/python
#-*- coding: utf-8 -*-

"""
improved version of q27_rm_markup.py
USAGE: python q20_readjson.py < jawiki-country.json.gz | python q28_rm_markup.py
"""

import re
import sys

def remove_markup(text):
	markups = {
		r"('{5}|'{3}|'{2})": "", #emphases
		r"\[\[.*?([^|]+?)\]\]": r"\1", #hyperlinks

		#this regex should be reviewed
		r"<ref.+": "",

		r"\*.*<br.*?>": "", #medialink B
		r"\{\{.*?([^|]+?)\}\}": r"\1" #medialink C
		}
		
	for k, v in markups.iteritems():
		text = re.sub(k, v, text)
	return text

def get_template():
	D = {}
	isBaseInfo = False
	for line in sys.stdin:
		if line.startswith('{{基礎情報'):
			isBaseInfo = True
		elif isBaseInfo and line.startswith('}}'):
			isBaseInfo = False
		elif isBaseInfo:
			if line.startswith('|'):
				k, v = line[1:].strip('\n').split(' = ')
				D[k] = remove_markup(v)
			else:
				D[k] += remove_markup(line.strip('\n'))
		elif not isBaseInfo:
			pass
			
	return D

if __name__ == '__main__':
	D = get_template()
	for k, v in D.iteritems():
		print k, v