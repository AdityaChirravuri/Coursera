import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

link = input('Enter location: ')
html = urllib.request.urlopen(link).read().decode()
print('Retrieving', link)
print('Retrieved', len(html), 'characters')

cn = 0
sm = 0
data = ET.fromstring(html)
tags = data.findall('comments/comment')

for tag in tags:
    cn += 1
    sm += int(tag.find('count').text)

print('Count:', cn)
print('Sum:', sm)
