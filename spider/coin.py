#encoding:UTF-8
from bs4 import BeautifulSoup
import urllib2

def create_header():
    return """
    <table>
        <tbody>
            <tr>
                <th>h1</th>
                <th>h2</th>
                <th>h3</th>
                <th>h4</th>
                <th>h5</th>
                <th>h6</th>
                <th>h7</th>
                <th>h8</th>
            </tr>
    """

def create_footer():
    return """
        </tbody>
    </table>
    """


def getPage(url):
    request = urllib2.Request(url)
    request.add_header('User-Agent','Mozilla/4.0 (compatible;MSIE 5.5; Windows NT)')
    response=urllib2.urlopen(request)
    return response.read()


url = "http://www.jinse.com/coin"

result = getPage(url)

bs=BeautifulSoup(result, "html.parser")

[style.extract() for style in bs.findAll('style')]

bs.prettify()
[s.extract() for s in bs(['span', 'new'])]

txt='./coins.html'
f = open(txt, "w")
f.write(create_header())

# TODO: Header Summary
# for k in bs.find_all('div',class_='wrap bsummary'):
#     print(k)
#     f.write(str(k))

for k in bs.find_all('div',class_='link'):
    for ul in k.find_all('ul'):
        del ul['class']
        ul.name = "tr"

        for li in ul.find_all('li'):
            del li['class']
            li.name = "td"

    f.write(str(k))



f.write(create_footer())
