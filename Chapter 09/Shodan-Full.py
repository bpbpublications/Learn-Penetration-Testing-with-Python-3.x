#!/usr/bin/env python3
# Full Enumration from Shodan
# Author Yehia Elghaly

import shodan
from colorama import Fore, Back, Style

print (Fore.GREEN + "******************************************************")
print ("SHODAN ITERFACE For Hackers")
print ("Query IP's and Domains")
print ("******************************************************")
print ("")
print (Fore.YELLOW + "1- Query a Company ")
print ("2- Query an IP ")

def host():
	ip = input("Enter IP: ")
	SHODAN_API_KEY = "in8zF"
	api = shodan.Shodan(SHODAN_API_KEY)

	target = api.host(ip)
	print("""
		IP: {}
		Company: {}
		Operating System: {}
		""".format(target['ip_str'], target.get('com', 'n/a'), target.get('os', 'n/a')))

	for item in target['data']:
		print("""
			Port: {}
			Banner: {}
			""".format(item['port'], item['data']))

def sho():
	SHODAN_API_KEY = "in8"
	api = shodan.Shodan(SHODAN_API_KEY)

	try:
		keyw = input("Enter Keyword: ")
		results = api.search(keyw)
		# Show the results
		print('Results found: {}'.format(results['total']))
		for result in results['matches']:
			print('IP Address: {}'.format(result['ip_str']))
			print(result['data'])
			print('')
	except shodan.APIError + e:
		print('Fault: {}'.format(e))

print ("")
choice = input('Enter your choice [1-2] : ')
choice = int(choice)

if choice == 1:
	print (sho())

if choice == 2: 
	print (host())

else:
	print ("Try Again" + choice)