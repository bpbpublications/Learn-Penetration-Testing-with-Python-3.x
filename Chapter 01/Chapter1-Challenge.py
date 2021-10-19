#!/usr/bin/env python3
#Chapter-1 Challenge
#Author Yehia Elghaly

Challenge = {10: 55, 23: 5, 878: 232, 112: 34, 668: 33}
def value_search(v):
	if v in Challenge:
		print('The Value is Exist')
	else:
		print('The Value not Exist')
value_search(878)