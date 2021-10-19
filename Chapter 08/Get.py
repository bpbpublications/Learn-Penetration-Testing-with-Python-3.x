#!/usr/bin/env python3
# Send Get Request
#Author Yehia Elghaly

import urllib.request
import urllib.parse

link = 'http://192.168.0.102/xampp/'
get = urllib.request.urlopen(link)
print(get.read().decode('utf-8'))