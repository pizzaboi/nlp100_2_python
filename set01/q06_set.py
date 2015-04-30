#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
extended version of q05_ngram.py
"""

def word_ngram(string, N):
	words = string.split(' ')
	ngram = []
	for i in xrange(len(words) - N + 1):
		ngram.append(words[i:i + N])
	return ngram

def char_ngram(string, N):
	chars = string.replace(' ', '')
	ngram = []
	for i in xrange(len(chars) - N + 1):
		ngram.append(chars[i:i + N])
	return ngram

if __name__ == '__main__':
	X = set(char_ngram("paraparaparadise", 2))
	Y = set(char_ngram("paragraph", 2))

	print X | Y #和集合
	print X & Y #積集合	
	print X - Y #差集合
	print Y - X #差集合

	print 'se' in X
	print 'se' in Y


