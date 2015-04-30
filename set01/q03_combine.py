#! /usr/bin/python
# -*- coding: utf-8 -*-

def combine(str1, str2):
	combined = ''
	for x, y in zip(str1, str2):
		combined += x + y
	return combined

if __name__ == '__main__':
	print combine(u'パトカー', u'タクシー')
