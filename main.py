#!/usr/bin/python3
import socket
import time
#from socket import gethostbyname, gaierror
import http.client

def get_status_code(host, path="/"):
    try:
        conn = httplib.HTTPConnection(host)
        conn.request("HEAD", path)
        return conn.getresponse().status
    except Exception:
    	return 'NoWeb'

def getIP(address):
	try:
		addr = socket.gethostbyname(address);
	except socket.gaierror:		
		addr = 'NoIP'
	return addr;
			
def formatLine(line):
	addr = getIP(line)
	if addr != "NoIP":
		print (line,",",addr,",","ip address ",addr," 255.255.255.255 Null0 name SOC_",date,"_Malware_Domains", sep='')
	return;
	
lines = [line.rstrip('\n') for line in open('./tazz_list.csv')]		
array = []
date = time.strftime("%Y%m%d")
for line in lines:
	formatLine(line)
	
