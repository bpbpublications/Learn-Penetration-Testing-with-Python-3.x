#!/usr/bin/env python3
# Enumrate Shodan 
# Author Yehia Elghaly

import shodan

def host():
	SHODAN_API_KEY = "in8"
	api = shodan.Shodan(SHODAN_API_KEY)

	target = api.host('45.55.99.72')
	print("""
		IP: {}
		Company: {}
		Operating System: {}
		""".format(target['ip_str'], target.get('com', 'n/a'), target.get('os', 'n/a')))

    # print all banners
	for item in target['data']:
		print("""
			Port: {}
			Banner: {}
			""".format(item['port'], item['data']))

print (host())