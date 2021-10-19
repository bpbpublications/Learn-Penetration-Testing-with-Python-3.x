#!/usr/bin/env python3
# Payload Encoder With Different Encoders
# Author Yehia Elghaly

import base64
import re
import sys
import string
import binascii
import urllib.parse
from colorama import Fore, Back, Style

print ("Payload Encoders")
print ("")
z = input("Eenter a Payload: ")
print ("")
payload = z
print (Fore.CYAN + " Custom Encode")
print ("")
print (" 1. B64")
print (" 2. Hex")
print (" 3. URL_encode")
print (" 4. HTML Entities")
print (" 5. Hex With Semi Coloumns")
print ("")
choose = input("Choose your Encode ")
choose = int(choose)
if choose > 5:
    print ("Worng Choice!")
    sys.exit()

#Encode Payload use of Base64#
if choose == 1:
    print("")
    encoded = base64.standard_b64encode(payload.encode("utf-8"))
    print (' ################## B64 String #######################')
    print ('')
    en1 = encoded
    print (Fore.YELLOW + str(en1))

#Encdoe Payload use of HEX#
elif choose == 2:
    print ("")
    encoded = binascii.b2a_hex(payload.encode("utf-8"))
    print (' ################## URL String #######################')
    print ('')
    en2 = encoded
    print (Fore.YELLOW + str(en2))
            
#Encode payload use of URLEncode#
elif choose == 3:
    print ("")
    encoded = urllib.parse.quote(payload.encode("utf8"))
    print (' ################## URL String #######################')
    print ('')
    en3 = encoded
    print (Fore.YELLOW + str(en3))
    doublee = input("Double Encoding? y - n ")
    if "y" in doublee:
        ddoub = urllib.parse.quote_plus(en3)
        print (Fore.BLUE + str(ddoub))

#Encode with HexSemi()
elif choose == 5:
    print ("")
    x = ('')
    for i in payload:
        x += "&#x"+hex(ord(i))[2:]+";"
    print (x)
    print (' ################## Hex With Semi #######################')
    print ('')
    en55 = x
    print (Fore.YELLOW + str(en55))
        
#Encode Payload use of HTML Entities#
elif choose == 4:
    print ("")
    print (" 1. ()")
    print (" 2. all")
    print ("")
    go = input(" Choose your Encode ")
    go = int(go)

    #HTML encode single & Double Quotes#
    if go == 1:
        new5 = (payload.replace("(", "&lpar;").replace(")", "&rpar;"))
        get3 = new5
        print (Fore.YELLOW + str(get3))

#HTML encode of <>#
    elif go == 2:
        nn = (payload.replace("<", "&lt;").replace(">", "&gt;").replace("(", "&lpar;").replace(")", "&rpar;").replace('"', '&quot;').replace("'", '&#39;'))
        get4 = nn
        print (Fore.YELLOW + str(get4))

    else:
        print (" Try Again")