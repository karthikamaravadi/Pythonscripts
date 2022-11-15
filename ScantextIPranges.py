        # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import socket
import re

def get_remote_machine_info(ipaddress):
        remote_host =  ipaddress
        print(ipaddress,type(ipaddress))
        """
        try:
            print ("Hostname of %s: %s" %(remote_host,socket.gethostbyaddr(remote_host)))
            file1 = open("info.txt", "a")  # append mode
            file1.write("Hostname of %s: %s" %(remote_host,socket.gethostbyaddr(remote_host))+"\n")
            file1.close()
            
        except socket.error as err_msg:
            print ("%s: %s" %(remote_host, err_msg))
            file1 = open("info.txt", "a")  # append mode
            file1.write("%s: %s" %(remote_host, err_msg)+"\n")
            file1.close()
        """

            
with open('gethost.txt') as fh:
   read = fh.readlines()
   for line in read:
       #address = str(line)
     #  print(address)
       get_remote_machine_info(line)
"""
# declaring the regex pattern for IP addresses
pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

# extracting the IP addresses
for line in fstring:
   lst.append(pattern.search(line)[0])
 
# displaying the extracted IP addresses

if __name__ == "__main__":
    with open('gethost.txt') as fh:
        fstring = fh.readlines()
        lst=[]
        # declaring the regex pattern for IP addresses
        pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
        # extracting the IP addresses
        for line in fstring:
            lst.append(pattern.search(line)[0])
            for i in lst:
                get_remote_machine_info(i)
"""