x= '*' *80
print (x)
print (x)
print ("""
                =====     ====   ||
                   // = = |  |   ||
                  //  | | | /    ||
                ----- --- | \    ||
                ----             00
                DESCRIPTION:WEBSCRAPPER
                coD3r:zuri
                """)
print (x)
print (x)

import requests
url = input("Enter the url: ")
from sys import argv
(script,url) = argv
print ("the url is %r" %(url))

import BeautifulSoup
r = requests.get(url)
soup = BeautifulSoup(r.content)
print (soup.prettify())
print (x)
#soup.find_all("a")
#print soup.prettify

for link in soup.find_all("a"):
  print (link)
print (x)
print ("\nthe href content is: \n")

for link in soup.find_all("a"):
 link.get("href")
 print (link.get("href"))
