#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 11:59:55 2021

@author: karthikamaravadi
"""

import os
import re
from scapy.layers.l2 import Ether,ARP
from scapy.sendrecv import srp


pattern='\w\w:\w\w:\w\w:\w\w:\w\w:\w\w'		# \ w Matching letters or numbers or underscore or Chinese characters equivalent to '[^ A-ZA-Z0-9_]'.
UNKNOWN_MAC='ff:ff:ff:ff:ff:ff'


def get_mac_address(network):
    temp = os.popen('ifconfig '+network)  #ifconfig must have spaces, actually equivalent to command ifconfig ens33
    result=temp.readlines()
    for item in result:
        condition=re.search(pattern,item)	# Select MAC address by regular matching filter
        if condition:
            return condition.group(0)


def get_ip_list(ip):
    ip_list=[]
    temp=str(ip).split('.')
    for i in range(1,255):	# This assumes that within the same local area network, the first three segments of IP are the same, from 1-254
        ip_list.append(temp[0]+'.'+temp[1]+'.'+temp[2]+'.'+str(i))
    return ip_list


def arp_scan(local_ip,network='ens33'):		# Most important part, incoming local IP address and NIC name
    mac=get_mac_address(network)
    ip_list=get_ip_list(local_ip)
	
	# Send the ARP request package, OP = 1 is the request, OP = 2 is a response
    temp=srp(Ether(src=mac,dst=UNKNOWN_MAC)/
             ARP(op=1,hwsrc=mac,hwdst=UNKNOWN_MAC,psrc=local_ip,pdst=ip_list),
             iface=network,timeout=1,verbose=False)
    result=temp[0].res
    result_list=[]
    number=len(result)
    for i in range(number):
        result_ip=result[i][1].getlayer(ARP).fields['psrc']		#             because the second package is an IS-AT package, result [i] [0] is the who HAS package, is the package we sent
        result_mac=result[i][1].getlayer(ARP).fields['hwsrc']
        result_list.append((result_ip,result_mac))
    return(result_list)


if __name__ == '__main__':
    ip=raw_input('input the local ip:')
    network=raw_input('input the network:')
    result=arp_scan(ip,network)
    for item in result:
        print('%-20s%-20s'%(item[0],item[1]))