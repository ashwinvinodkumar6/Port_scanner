#!/bin/python3

import re
import sys
import socket
import threading
import argparse

 
#cmd line parser
parser = argparse.ArgumentParser()
parser.add_argument("ip",help="Enter the ip range")
args = parser.parse_args()

#regex
host = re.split("1/",args.ip)
for i in range(1,254):
	target = str(host[0]) + str(i)
	#print(target)
	for port in range(20,100):
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		if result ==0:
			print("Port {}".format(port)+ " is open on {} ".format(target))
		s.close()
		
	
	
