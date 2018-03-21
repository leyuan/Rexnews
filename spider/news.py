#encoding:UTF-8
from bs4 import BeautifulSoup
import urllib2

from helper import SpiderHelper

helper = SpiderHelper()

def getPage(url):
    request = urllib2.Request(url)
    request.add_header('User-Agent','Mozilla/4.0 (compatible;MSIE 5.5; Windows NT)')
    response=urllib2.urlopen(request)
    return response.read()

url = "http://www.jinse.com/news"

result = getPage(url)
bs = BeautifulSoup(result, "html.parser")
bs.prettify()

news_html = '../news.html'
f = open(news_html, "w")

f.write(helper.create_header())

for entry in bs.find_all('div', class_='list'):
    entry['class'] = 'entry entry-small'

    [image_div, message_div] = entry.find_all('div', recursive=False)
    image_div['class'] = 'thumbnail-attachment'
    message_div['class'] = 'entry-body'

    del image_div.a['class']
    del image_div.img['height']
    del image_div.img['border']
    image_div.img['width'] = '400'

    [m_title, m_body, m_tips] = message_div.find_all('div', recursive=False)
    m_title['class'] = 'entry-title'
    m_body.name = 'p'
    del m_body['class']
    del m_tips['class']

    f.write(str(entry))

f.write(helper.create_footer())
