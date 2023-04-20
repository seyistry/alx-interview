#!/usr/bin/python3
from math import factorial

def pascal_triangle(n):
	outer_list = []
	if n <= 0:
		return outer_list
	for i in range( 1, n + 1):
		inner_list = []
		for j in range(i + 1):
			inner_list.append(int(factorial(i)/(factorial(j) * factorial(i - j))))
		outer_list.append(inner_list)
	return outer_list
