'''
@author: Abdelrahman Moez - aka Hydra
@script: webinv.py
@description: Website investigator
@python version: 2.7
'''
import socket
import sys
import os
import urlparse
import urllib2
from colorama import Fore, Back, Style, init
import httplib
import time
try:
	from bs4 import BeautifulSoup as bs
except:
	from BeautifulSoup import BeautifulSoup as bs
#
init(autoreset=True) # from colorama
def banner():
	banner = """
			 {0}__      __      ___.   .___             
			/  \    /  \ ____\_ |__ |   | _______  __
			\   \/\/   // __ \| __ \|   |/    \  \/ /
			 \        /\  ___/| \_\ \   |   |  \   / 
			  \__/\  /  \___  >___  /___|___|  /\_/  
			       \/       \/    \/         \/ 
			       {1}Description: Website investigator
			       Version: 1.0
			       Coded by: Abdelrahman Moez - aka Hydra

	""".format(Style.BRIGHT+Fore.RED, Fore.YELLOW)
	print banner
def cls():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

def initiate(website):
	dir_name = urlparse.urlparse(website).netloc
	if os.path.exists(dir_name) != True:
		os.mkdir(dir_name)
	os.chdir(dir_name)

def report_writer(report_name,report):
	f = open(report_name, 'w')
	f.write(str(report))
	f.close()

def abs_http(link):
	http_link = link
	if http_link.startswith("www."):
		http_link = http_link[4:]
		http_link = "".join(("http://",http_link))
	if http_link.startswith("http://www."):
		http_link = http_link[11:]
		http_link = "".join(("http://",http_link))
	if not http_link.startswith("http://"):
		http_link = "".join(("http://",http_link))
	return http_link

def status(website):
	website = "".join(('www.', urlparse.urlparse(website).netloc))
	con = httplib.HTTPConnection(website, 80)
	con.request('GET', '/')
	res = con.getresponse()
	return res.status, res.reason
	
def ip(website):
	website = "".join(('www.', urlparse.urlparse(website).netloc))
	ip = socket.gethostbyname(website)
	return ip

def banner_grabber(website):
	website = "".join(('www.', urlparse.urlparse(website).netloc))
	con = httplib.HTTPConnection(website, 80)
	con.request('GET', '/')
	res = con.getresponse()
	msg = res.msg
	report_writer('banner_grabber.txt', msg)

def geo_ip(ip):
	try:
		result = {}
		formated_result = ''
		link = 'http://whatismyipaddress.com/ip/'+ip
		opener = urllib2.build_opener()
		opener.addheaders = [('User-agent', 'Mozilla/5.0')]
		reader = opener.open(link).read()
		soup = bs(reader)
		for tag in soup.findAll('tr'):
			if not tag.find('th').text == 'Blacklist':
				try:
					result [tag.find('th').text.strip(':')] = tag.find('td').text.strip(" ")
				except: pass
		for x, y in result.items():
			formated_result += "".join((x+': ',y,'\n'))
		report = formated_result
	except Exception, e:
		report = e
	report_writer('geo_ip.txt', report)

def whois(ip):
	whois_link = urlparse.urljoin("http://whois.net/ip-address-lookup/", ip)
	source = urllib2.urlopen(whois_link).read()
	soup = bs(source)
	full_whois_result = ''
	for tag in soup.findAll('pre'):
		whois_result = tag.text
		whois_result = whois_result.splitlines()
		full_whois_result += "\n".join(whois_result)
	report = full_whois_result
	report_writer('whois.txt', report)
# -------------------------------------- #
cls()
banner()
website = abs_http(sys.argv[1])
stime = time.time()
initiate(website)
#
print Style.BRIGHT+Fore.CYAN+'[>] Investigating [%s] \n' %website
#
ip = ip(website)
print '{0}[+] IP: {1}%s'.format(Style.BRIGHT+Fore.RED, Fore.WHITE) %ip
#
print '{0}[+] Status: {1}%s | %s \n'.format(Style.BRIGHT+Fore.RED, Fore.WHITE) %(status(website)[0], status(website)[1])
#
print '{0}[*] Grabbing Banner ...'.format(Style.BRIGHT+Fore.GREEN)
banner_grabber(website)
#
print '{0}[*] Getting Geolocation IP info ...'.format(Style.BRIGHT+Fore.GREEN)
geo_ip(ip)
#
print '{0}[*] Performing WHOIS query ...'.format(Style.BRIGHT+Fore.GREEN)
whois(ip)
#
print '\n{0}> Time taken: {1}%f (sec)'.format(Style.BRIGHT+Fore.MAGENTA, Fore.WHITE) %(time.time()-stime)
