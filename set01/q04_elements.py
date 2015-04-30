#! /usr/bin/python
#-*- coding: utf-8 -*-

def element(sentence):
	D = {}
	for i, w in enumerate(sentence.split(' ')):
		N = i + 1
		if N in (1, 5, 6, 7, 8, 9, 15, 16, 19):
			D[N] = w[0]
		else:
			D[N] = w[0:2]
	return D

if __name__ == '__main__':
	D = element("Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.")
	for k, v in D.iteritems():
		print k, v