# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 17:38:56 2021

@author: karthikamaravadi
"""

import ipaddress
import os
import socket
import sys, struct, socket

"""
def get_remote_machine_info(ipaddress2):
        remote_host =  ipaddress
        print(remote_host)

        try:
            print ("Hostname of %s: %s" %(remote_host,socket.gethostbyaddr(remote_host)))
            file1 = open("ScanningSubnet1.txt", "a")  # append mode
            file1.write("Hostname of %s: %s" %(remote_host,socket.gethostbyaddr(remote_host))+"\n")
            file1.close()
            
        except socket.error as err_msg:
            print ("%s: %s" %(remote_host, err_msg))
            file1 = open("ScanningSubnet1.txt", "a")  # append mode
            file1.write("%s: %s" %(remote_host, err_msg)+"\n")
            file1.close()

"""

def get_ip_from_subnet(ip_subnet):
    #
     ips= ipaddress.ip_network(ip_subnet)
     for ip in ips:
        ipadd = str(ip)
        file1 = open("IPranges.txt", "a")
        file1.write(ipadd+"\n")
        file1.close()

SCsubnets = open("file.txt",'r')
Lines = SCsubnets.readlines()
for line in Lines:
    ip_subnet = ("{}".format(line.strip()))
    get_ip_from_subnet(ip_subnet)

 

