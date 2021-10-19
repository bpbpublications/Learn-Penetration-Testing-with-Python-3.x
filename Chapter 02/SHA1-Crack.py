#!/usr/bin/env python3
#Crack SHA1 using wordlists
#Author Yehia Elghaly

from urllib.request import urlopen
import hashlib

hashsha1 = input("Enter your Hash .\n>")
wordlist = input("Enter your wordlist url: ")
allw = str(urlopen(wordlist).read(), 'utf-8')

for crack in allw.split('\n'):
    hashcrack = hashlib.sha1(bytes(crack, 'utf-8')).hexdigest()
    if hashcrack == hashsha1:
        print("Password Found ", str(crack))
        quit()
    elif hashcrack != hashsha1:
        print("Password crack ",str(crack)," not found ")
print("Please Choose another wordlist and try again.")