#! /usr/bin/python
#-*- coding: utf-8 -*-

import random

def typoglycemia(sentence):
	ret = []
	for w in sentence.split(' '):
		if len(w) < 4:
			ret.append(w)
		else:
			inner = list(w[1:-1])
			random.shuffle(inner)
			ret.append(w[0] + ''.join(inner) + w[-1])
	return ret


if __name__ == '__main__':
	example = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
	print example
	print ' '.join(typoglycemia(example))


