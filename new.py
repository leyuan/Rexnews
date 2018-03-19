#encoding:UTF-8
from bs4 import BeautifulSoup
import urllib2
import urllib
import json
import sys
import re
def getPage(url):
    request = urllib2.Request(url)
    request.add_header('User-Agent','Mozilla/4.0 (compatible;MSIE 5.5; Windows NT)')
    response=urllib2.urlopen(request)
    return response.read()

url = "http://www.jinse.com/news"

result = getPage(url)
bs = BeautifulSoup(result)

# [style.extract() for style in bs.findAll('style')]

bs.prettify()
[s.extract() for s in bs(['span', 'new'])]

#m=re.match(r'var .*?location', content)
#print bs
txt = './news.html'
f = open(txt,"w+")
f.write('<html>'+'<meta http-equiv="Content-Type" content="text/html; charset=utf-8">')

for k in bs.find_all('div',class_='news'):
    print(k)
    f.write(str(k))

f.write('</html>')