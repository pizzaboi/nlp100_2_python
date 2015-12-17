# -*- coding: utf-8 -*-

import re
import sys

if __name__ == '__main__':
	filename = sys.argv[1]
	# (. or ; or : or ? or !) → 空白文字 → 英大文字
	pattern = re.compile(r'[.;:?!] ([A-Z])')
	repl    = r'.\n\1' 

	for line in open(filename):
		line = line.strip('\n')
		## Replace the pattern in line by repl
		## backreference \1 is replaced with the substring matched by group 1
		print re.sub(pattern, repl, line)

