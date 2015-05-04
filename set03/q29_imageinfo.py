#! /usr/bin/python
#-*- coding: utf-8 -*-

"""
USAGE: python q20_readjson.py < jawiki-country.json.gz | python q29_imageinfo.py
"""

import httplib2
import re
import sys
import json

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

def get_imageinfo():
	D = get_template()
	q = httplib2.urllib.urlencode({
		'format': 'json',
		'action': 'query',
		'prop': 'imageinfo',
		'iiprop': 'url',
		'titles': 'Image:%s' % D['国旗画像'],
		})
	h = httplib2.Http('.cache')
	res, content, = h.request(
		'http://en.wikipedia.org/w/api.php?%s' % q)

	for page in json.loads(content)['query']['pages'].itervalues():
		print page['imageinfo'][0]['url']

if __name__ == '__main__':
	get_imageinfo()