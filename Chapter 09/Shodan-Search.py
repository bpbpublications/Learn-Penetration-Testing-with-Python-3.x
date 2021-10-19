#!/usr/bin/env python3
# Shodan Search 
# Author Yehia Elghaly

import shodan

def sho():
	SHODAN_API_KEY = "in8z"
	api = shodan.Shodan(SHODAN_API_KEY)

	try:
		results = api.search('nasa')
		# Show the results
		print('Results found: {}'.format(results['total']))
		for result in results['matches']:
			print('IP Address: {}'.format(result['ip_str']))
			print(result['Data'])
			print('')
	except shodan.APIError + e:
		print('Fault: {}'.format(e))

print (sho())