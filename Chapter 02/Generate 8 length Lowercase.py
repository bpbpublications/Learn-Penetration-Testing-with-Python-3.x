#!/usr/bin/env python3
#Generate 8 length Lowercase
#Author Yehia Elghaly

import random
import string
import os.path

def passwordGenerate(PasswordLength=8):
	password = string.ascii_lowercase
	return ''.join(random.choice(password) for i in range(PasswordLength))

passy = (passwordGenerate(8) )
print (passy)

path = '/root/Desktop' 
name = input("File Name: ")
filename = os.path.join(path, name+".txt")         
with open(filename, "w") as file1:
    file1.write (str(passy))