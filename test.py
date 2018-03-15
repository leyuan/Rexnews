#encoding:UTF-8
from bs4 import BeautifulSoup
import urllib2
import json 
import sys
import re
def getPage(url):
    request= urllib2.Request(url)
    response=urllib2.urlopen(request)
    return response.read()

url="http://36kr.com/newsflashes"

result=getPage(url)
#print result

#title = re.findall('title',result.text,re.S)
#print title


bs=BeautifulSoup(result)

[style.extract() for style in bs.findAll('style')]

bs.prettify()

reg1=re.compile("<[^>]*>")
content=reg1.sub('',bs.prettify())

#m=re.match(r'var .*?location', content)

m = re.search(r'var props.*?,location', content)
#print m.group(0)
if m:
    q=m.group(0)
    q=q[10:-9]
    s=json.loads(q)
    print s["newsflashList|newsflash"]
    #print s.keys()
    
    #print s["newsflashList|newsflash"][1]
    txt='./news.html'
    f = open(txt,"w+")    
    f.write('<html>'+'<meta http-equiv="Content-Type" content="text/html; charset=utf-8">')
    
    for i in range(0,20):
        newTitle=json.dumps(s["newsflashList|newsflash"][i]["title"], ensure_ascii=False,encoding="utf-8",indent=2)
        newDescription=json.dumps(s["newsflashList|newsflash"][i]["description"], ensure_ascii=False,encoding="utf-8",indent=2)
        newUrl=json.dumps(s["newsflashList|newsflash"][i]["news_url"], ensure_ascii=False,encoding="utf-8",indent=2)
        newTitle=newTitle[1:-1]
        newDescription=newDescription[1:-1]
        f.write('<h1>'+newTitle.encode("utf-8")+'<h1>')
        f.write('<h3>'+newDescription.encode("utf-8")+'<h3>') 
        f.write('<a href='+newUrl.encode("utf-8")+'>原文链接</a>'+'<br>')
    
        
    f.write('</html>')    
  
 
    
   
else:
    print 'not search'

