import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ss1
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

link = input('ENTER - ' )
html = urlib.request.urlopen(link, context  = ctx).read()
soup = beatifulSoup(html, 'html.parser')

tags = soup('span')
sm =0 
cn = 0
for tag in tags:
    cn += 1
    sm += int(tag.contents[0])

print('count %d' % cn)
print('sum %d' % sm)

#sum = 50 # comments =2439
