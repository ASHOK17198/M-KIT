from bs4 import BeautifulSoup
import urllib.request
import re
import time
import subprocess
import os
from collections import OrderedDict
import sys


#XLAR8

def open(links):
      p = subprocess.Popen(["chromium-browser"]+links)
     #p = subprocess.Popen(["xyz","http://www.xyz.com"])
      print("################################### ¯\_(ツ)_/¯##########################   ")
      print(links)
      time.sleep(6)
      os.system('pkill chromium $')
      p.kill()


     #os.sytem('chromium-browser '+firefox.com +ubuntu.com +duckduckgo.com )

url = input("enter the URL") 

try:

    html_page = urllib.request.urlopen(url)                             #OPEN 

except:

    print("something wrong")                                              

soup = BeautifulSoup(html_page)                                          #OBJECT     
links = []
 
for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
    links.append(link.get('href'))

print(len(links))
OrderedDict( (x,1) for x in links ).keys()
    
print(links)
print(len(links))
ulinks = []
                                                                                  
for l in links: 
    if l not in ulinks:                                                       #eleminate duplicate links
        ulinks.append(l)
print(len(ulinks))       
for i in range(0,len(ulinks),5):                                              # TO REDUCE RAM LOAD 
      chunk=[ulinks[i] ,ulinks[i+1],ulinks[i+2],ulinks[i+3],ulinks[i+4]]
      open(chunk)
     #os.system('chromium-browser  '+links[i] )
     #os.system('chromium-browser  '+links[i+1] )
     #os.system('chromium-browser  '+links[i+2] )
     #os.system('chromium-browser  '+links[i+3] )
    # os.system('chromium-browser  '+links[i+4]+'ctrl+c' )
      #time.sleep(6)
      #os.system('pkill chromium')
     



p = os.system('chromium-browser chrome://history/ ')                            #screenshot (processing...)
os.system("gnome-screenshot --file=c4c.png")
     
