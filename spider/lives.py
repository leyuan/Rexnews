#encoding:UTF-8
from bs4 import BeautifulSoup
import urllib2
import urllib
import json 
import sys
import time
import re

def getPage(url):
    request = urllib2.Request(url)
    request.add_header('User-Agent','Mozilla/4.0 (compatible;MSIE 5.5; Windows NT)')
    response=urllib2.urlopen(request)
    return response.read()

url="http://www.bishijie.com/api/newsv17/index?size=100&client=pc"

result=getPage(url)

temp = json.loads(result)
j=0
txt='./lives.html'
f = open(txt,"w+")  
f.write('<html>'+'<meta http-equiv="Content-Type" content="text/html; charset=utf-8">')

for q in range (0, len(temp['data'])):
    for i in range(0, len(temp['data'][q]['buttom'])):
        f.write("<div class='news'>")
        f.write("<div class='index'>")
        f.write(str(j))
        f.write("</div>")
        f.write("<br>") 
        f.write("<div class='title'>")
        f.write(temp['data'][q]['buttom'][i]['title'].encode('utf-8'))
        f.write("</div>")
        f.write("<br>")        
        f.write("<div class='content'>")
        f.write(temp['data'][q]['buttom'][i]['content'].encode('utf-8'))
        f.write("</div>")
        f.write("<br>")       
        time_local = time.localtime(int(temp['data'][q]['buttom'][i]['issue_time']))
        dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
        f.write("<div class='time'>")
        f.write(dt)
        f.write("</div>")
        f.write("</div>")
        f.write("<br>")
        #print ""
        j=j+1
        if(j==50):
            break
    if(j==50):
        break    
      

f.write("</html>")

#print j
#print temp['data'][q]['buttom'][i]['title']
#print temp['data'][q]['buttom'][i]['content']
 #print dt
#title = re.findall('title',result.text,re.S)
#print title


#bs=BeautifulSoup(result)

#[style.extract() for style in bs.findAll('style')]

#bs.prettify()
#[s.extract() for s in bs(['span', 'new'])]

#m=re.match(r'var .*?location', content)
#print bs

#for k in bs.find_all('div',class_='live-info'):
#    print(k)
#    f.write(str(k))
#    f.write("<br>")

    

#f.write('</html>')    
