import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

def get_html(url):
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    html = urllib.request.urlopen(url, context=ctx).read()
    return BeautifulSoup(html, 'html.parser')


url = input('Enter URL:') # http://py4e-data.dr-chuck.net/known_by_Lori.html
count = input('Enter count:')
position = input('Enter position:')

icount = int(count)
for i in range(icount):
    html = get_html(url) 

    # Retrieve all of the anchor tags
    tags = html('a')
    links = list()
    counter = 0
    ipos = int(position)
    for tag in tags:
        counter = counter + 1
        if ipos != counter: continue
        url = tag.get('href', None)
        print('Retrieving:', url)
        break
