#! /usr/bin/python
#-*- coding: utf-8 -*-

import json
import gzip
import sys

def reader():
	for line in gzip.GzipFile(fileobj=sys.stdin):
		article = json.loads(line)
		if article['title'] == u'イギリス':
			print article['text'].encode('utf-8')

if __name__ == '__main__':
	reader()