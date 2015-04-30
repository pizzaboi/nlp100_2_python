#! /usr/bin/python
# -*- coding: utf-8 -*-

def template(x, y, z):
	return '{}時の{}は{}'.format(x, y, z)

if __name__ == '__main__':
	print template(12, '気温', 22.4)