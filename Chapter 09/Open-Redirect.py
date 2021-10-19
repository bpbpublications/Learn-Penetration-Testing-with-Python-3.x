import requests
import os
import sys
from colorama import Fore, Back, Style

Target = input("Enter Target URL: ")
listt = ('payloads.txt')

def openr():
	if not os.path.isfile(listt):
		print('[-] ' + listt + ' File Not Exist!!.')
		sys.exit()
	if not os.access(listt, os.R_OK):
		print('[-] ' + listt + ' Access Denied.')
		sys.exit(0)
	print('Loading Payloads: ' + listt)
	print ("")
	f = open(listt,'r')
	for line in f.readlines():
		payload = line.strip('\n')
		try:
			final = (Target + payload)
			response = requests.get(final)
			for resp in response.history:
				if resp.status_code == 302:
					print(resp.status_code, resp.url + Fore.RED + " [!] Vulnerable to Open Redirect")
				else:
					print(resp.url + Fore.GREEN + '[-]Not Vulnerable')

		except requests.exceptions.RequestException as e:
			print (Fore.CYAN + "Invalid URL")
			sys.exit()
		except IOError:
			print(IOError)
		except KeyboardInterrupt:
			print ("User Exit")
			sys.exit()
		
print (openr())