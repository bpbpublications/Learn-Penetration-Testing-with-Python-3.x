#!/usr/bin/env python3
# Crack Zip Files using wordlists
#Author Yehia Elghaly

import zipfile
import colorama
from colorama import Fore, Back, Style
from threading import Thread

print ("Zip Brute Force Attack")

def zip_crack(zipsec, password):
        try:
                password = bytes(password.encode('utf-8'))
                zipsec.extractall(pwd=password)
                print (Fore.GREEN + "[*] Password Found: ", str(password))
        except:
                pass

def Main():
        zipname = input("Name of Hash file: ")
        pname = input("Name of Password file: ")
        if (zipname == None) | (pname == None):
                print (Fore.Red + "Wrong File Name")
                exit(0)
        else:
        	pass

        zipsec = zipfile.ZipFile(zipname)
        passFile = open(pname)

        for line in passFile.readlines():
            password = line.strip('\n')
            thr = Thread(target=zip_crack, args=(zipsec, password))
            thr.start()

if __name__ == '__main__':
        Main()