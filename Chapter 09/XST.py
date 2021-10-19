#!/usr/bin/env python3
# Cross Site Trace (XST)
# Author Yehia Elghaly

import urllib.request
from urllib.error import URLError
from colorama import Fore, Back, Style

def trace():
	try:
		print ("Cross Site Trace - XST Check")
		print ("")
		target = input("Enter Target Website: ")
		req = urllib.request.Request(url=target ,method='TRACE', headers={"User-Agent": "Chrome"})
		f = urllib.request.urlopen(req)
		if f:
			print(f.status)
			print(f.reason)
			print ("")
			print (Fore.RED + "Website is Vulnerable to XST")
	except urllib.error.HTTPError as e:
		print (Fore.GREEN + "[-] Not Vulnerable (XST) ", e)

print (trace())