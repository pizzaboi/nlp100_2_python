#! /usr/bin/python
# -*- coding: utf-8 -*-

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
	print word_ngram('I am an NLPer', 2)
	print char_ngram('I am an NLPer', 3)