# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

wiki = input('Enter - https://en.wikipedia.org/wiki/')
url = 'https://en.wikipedia.org/wiki/'+ wiki
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
f = open('links.txt', 'w')
lst = []
colons = ['Category:','File:', 'Help:', 'Portal:',
'Special:', 'Talk:', 'Template:', 'Template_talk:']
# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    link = tag.get('href', None)
    if not link==None:
        if link.startswith("/wiki/"):
            l = link[6:]
            if l not in lst:
                lst.append(l)

for i in lst:
    print(i)
    f.write(i+'\n')
print(len(lst), 'links')
