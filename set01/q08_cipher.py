#! /usr/bin/python
# -*- coding: utf-8 -*-

def cipher(plaintext):
	ciphertext = ''
	for tok in plaintext:
		if tok.islower():
			ciphertext += chr(219 - ord(tok))
		else:
			ciphertext += tok
	return ciphertext

if __name__ == '__main__':
	print cipher('the quick brown fox jumps over the lazy dog')
	print cipher(cipher('the quick brown fox jumps over the lazy dog'))
