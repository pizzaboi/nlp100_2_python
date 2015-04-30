#! /usr/bin/python
# -*- coding: utf-8 -*-

def sent2num(sentence):
	nums = []
	for w in sentence.split(' '):
		nums.append(len(w.strip(',.')))
	return nums

if __name__ == '__main__':
	nums = sent2num("Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.")
	print ''.join([str(n) for n in nums])