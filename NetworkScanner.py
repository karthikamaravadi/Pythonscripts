# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 10:37:09 2021

@author: karthikamaravadi   

"""

#import subprocess
#import time
#import os
import socket
#import sys   

def get_remote_machine_info(ipaddress):
        remote_host =  ipaddress
        try:
            print ("Hostname of %s: %s" %(remote_host,socket.gethostbyaddr(remote_host)))
            file1 = open("scanoutput.txt", "a")  # append mode
            file1.write("Hostname of %s: %s" %(remote_host,socket.gethostbyaddr(remote_host))+"\n")
            file1.close()
            
        except socket.error as err_msg:
            print ("%s: %s" %(remote_host, err_msg))
            file1 = open("scanoutput.txt", "a")  # append mode
            file1.write("%s: %s" %(remote_host, err_msg)+"\n")
            file1.close()
            
def ping_ip_a():
    for octet4 in range(1,256):
        for octet3 in range(1,256):
            for octet2 in range(1,256):
                address = "10."+str(octet4)+"."+str(octet3)+"."+str(octet2)
                get_remote_machine_info(address)
                
def ping_ip_b():
    for octet4 in range(19,32): 
       for octet3 in range(128,256):
            for octet2 in range(1,256):
                address1= "172."+str(octet4)+"."+str(octet3)+"."+str(octet2)
                get_remote_machine_info(address1)
                    
def ping_ip_c():
    for octet3 in range(1,256):
        for octet2 in range(1,256):
            address2="192.168."+str(octet3)+"."+str(octet2)
            get_remote_machine_info(address2)
            

if __name__ == "__main__":
    #ping_ip_a()
    ping_ip_b()        
    #ping_ip_c()
