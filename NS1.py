# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 15:59:58 2021

@author: karthikamaravadi


import os
import socket
import sys   

def get_remote_machine_info(ipaddress):
        remote_host =  ipaddress
        try:
            print ("Hostname of %s: %s" %(remote_host,socket.gethostbyaddr(remote_host)))
            file1 = open("scanoutput1.txt", "a")  # append mode
            file1.write("Hostname of %s: %s" %(remote_host,socket.gethostbyaddr(remote_host))+"\n")
            file1.close()
            
        except socket.error as err_msg:
            print ("%s: %s" %(remote_host, err_msg))
            file1 = open("scanoutput1.txt", "a")  # append mode
            file1.write("%s: %s" %(remote_host, err_msg)+"\n")
            file1.close()
            
def ping_ip_a():
    #for octet4 in range(240,255):
     #   for octet3 in range(1,256):
            for octet2 in range(1,256):
                address = "10.240.3."+str(octet2)
                get_remote_machine_info(address)

def ping_ip_b():
    for octet4 in range(16,32): 
       for octet3 in range(1,256):
            for octet2 in range(1,256):
                address1= "172."+str(octet4)+"."+str(octet3)+"."+str(octet2)
                get_remote_machine_info(address1)

def ping_ip_c():
    for octet3 in range(1,256):
        for octet2 in range(1,256):
            address2="182.37."+str(octet3)+"."+str(octet2)
            get_remote_machine_info(address2)


if __name__ == "__main__":
    ping_ip_a()
   # ping_ip_b()        
   # ping_ip_c()
   """
import socket
from datetime import datetime
net = input("Enter the IP address: ")
net1 = net.split('.')
a = '.'

net2 = net1[0] + a + net1[1] + a + net1[2] + a
st1 = int(input("Enter the Starting Number: "))
en1 = int(input("Enter the Last Number: "))
en1 = en1 + 1
t1 = datetime.now()

def scan(addr):
   s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   socket.setdefaulttimeout(1)
   result = s.connect_ex((addr,135))
   if result == 0:
      return 1
   else :
      return 0

def run1():
   for ip in range(st1,en1):
      addr = net2 + str(ip)
      if (scan(addr)):
         print (addr , "is live")
         
run1()
t2 = datetime.now()
total = t2 - t1
print ("Scanning completed in: " , total)