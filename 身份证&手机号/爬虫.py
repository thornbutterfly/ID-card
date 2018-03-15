#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import urllib
import requests
import sys
from bs4 import BeautifulSoup


url = 'http://www.360doc.com/content/16/0124/00/27067706_530132052.shtml'
url1 = 'https://www.mi.com/'
req = urllib.request.Request(url1)
response = urllib.requset.urlopen(req)
html = response.read()
type = sys.getfilesystemencoding()
# response = urllib.request.urlopen(url1)
# print(response.read().decode('UTF-8'))
print(html.decode(type))
