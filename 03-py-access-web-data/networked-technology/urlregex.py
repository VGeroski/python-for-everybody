import urllib.request, urllib.parse, urllib.error
import re

html = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm').read()

links = re.findall(b'href="(http[s]?://.*?)"', html)

for link in links:
    print(link.decode())
