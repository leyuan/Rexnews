#encoding:UTF-8
from bs4 import BeautifulSoup
import urllib2

def create_header():
    return """
    <!doctype html>
        <html lang="en">

        <!-- Google Web Fonts
            ================================================== -->

        <link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,600,700%7CSource+Sans+Pro:200,300,400,500,600,700,900"
            rel="stylesheet">

        <!-- Basic Page Needs
            ================================================== -->

        <title>Сryptex</title>

        <!--meta info-->
        <meta charset="utf-8">
        <meta name="author" content="">
        <meta name="keywords" content="">
        <meta name="description" content="">

        <!-- Mobile Specific Metas
            ================================================== -->
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">

        <!-- Vendor CSS
            ============================================ -->

        <link rel="stylesheet" href="font/demo-files/demo.css">

        <!-- CSS theme files
            ============================================ -->
        <link rel="stylesheet" href="css/bootstrap-grid.min.css">
        <link rel="stylesheet" href="css/fontello.css">
        <link rel="stylesheet" href="css/owl.carousel.css">
        <link rel="stylesheet" href="css/style.css">
        <link rel="stylesheet" href="css/responsive.css">

        </head>

        <body>

            <div id="wrapper" class="wrapper-container">
                <header id="header" class="header sticky-header">

                    <!-- searchform -->

                    <div class="searchform-wrap">
                        <div class="vc-child h-inherit">

                            <form class="search-form">
                                <button type="submit" class="search-button"></button>
                                <div class="wrapper">
                                    <input type="text" name="search" placeholder="Start typing...">
                                </div>
                            </form>

                            <button class="close-search-form"></button>

                        </div>
                    </div>

                    <!-- pre-header -->

                    <div class="pre-header">

                        <div class="container">

                            <div class="row justify-content-between">

                                <div class="col">

                                    <div class="date">
                                        Wednesday, March 19, 2018
                                    </div>

                                </div>

                                <div class="col align-right">

                                    <div class="lang-area">

                                        <a href="#">Login</a>
                                        &nbsp;|&nbsp;
                                        <a href="#">Register</a>

                                    </div>

                                    <div class="lang-button">

                                        <a href="#">English</a>
                                        <ul class="dropdown-list">
                                            <li>
                                                <a href="#">English</a>
                                            </li>
                                            <li>
                                                <a href="#">German</a>
                                            </li>
                                            <li>
                                                <a href="#">Spanish</a>
                                            </li>
                                        </ul>

                                    </div>

                                </div>

                            </div>

                        </div>

                    </div>

                    <!-- top-header -->

                    <div class="top-header">

                        <div class="container">

                            <div class="row justify-content-between align-items-center">

                                <div class="col">

                                    <!-- Socials -->

                                    <ul class="social-icons">

                                        <li>
                                            <a href="#">
                                                <i class="icon-facebook"></i>
                                            </a>
                                        </li>
                                        <li>
                                            <a href="#">
                                                <i class="icon-twitter"></i>
                                            </a>
                                        </li>
                                        <li>
                                            <a href="#">
                                                <i class="icon-rss"></i>
                                            </a>
                                        </li>
                                        <li>
                                            <a href="#">
                                                <i class="icon-hash"></i>
                                            </a>
                                        </li>

                                    </ul>

                                </div>

                                <div class="col">

                                    <!-- logo -->

                                    <div class="logo-wrap">

                                        <a href="index.html" class="logo">
                                            <img src="images/logo.png" alt="">
                                        </a>

                                    </div>

                                </div>

                                <div class="col align-right">

                                    <a href="#" class="btn btn-style-4 btn-big">
                                        <i class="licon-mailbox-full"></i>Subscribe</a>

                                </div>

                            </div>

                        </div>

                    </div>

                </header>

                <div id="content" class="page-content-wrap">
                    <div class="container">
                    <div class="content-element3">

                    <h3 class="title">Events For December 2018</h3>

                    <a href="#" class="info-btn prev-btn type2">Previous Events</a>

                    </div>

                    <div class="entry-box style-2 list-type">
    """

def create_footer():
    return """
                    </div>
                </div>
            </div>
        </div>
        <!-- JS Libs & Plugins
    ============================================ -->
        <script src="js/libs/jquery.modernizr.js"></script>
        <script src="js/libs/jquery-2.2.4.min.js"></script>
        <script src="js/libs/jquery-ui.min.js"></script>
        <script src="js/libs/retina.min.js"></script>
        <script src="plugins/jquery.queryloader2.min.js"></script>
        <script src="plugins/owl.carousel.min.js"></script>

        <!-- JS theme files
    ============================================ -->
        <script src="js/plugins.js"></script>
        <script src="js/script.js"></script>

    </body>

    </html>
    """

def getPage(url):
    request = urllib2.Request(url)
    request.add_header('User-Agent','Mozilla/4.0 (compatible;MSIE 5.5; Windows NT)')
    response=urllib2.urlopen(request)
    return response.read()

url = "http://www.jinse.com/news"

result = getPage(url)
bs = BeautifulSoup(result, "html.parser")
bs.prettify()

lol = './lol.html'
f = open(lol, "w")
f.write(create_header())

for entry in bs.find_all('div', class_='list'):
    entry['class'] = 'entry entry-small'

    [image_div, message_div] = entry.find_all('div', recursive=False)
    image_div['class'] = 'thumbnail-attachment'
    message_div['class'] = 'entry-body'

    del image_div.a['class']
    del image_div.img['height']
    del image_div.img['border']
    image_div.img['width'] = '350'

    [m_title, m_body, m_tips] = message_div.find_all('div', recursive=False)
    m_title['class'] = 'entry-title'
    m_body.name = 'p'
    del m_body['class']
    del m_tips['class']
    m_tips.a['class'] = 'btn btn-small'
    m_tips.a.string = 'Read More'
    m_tips.ol.extract()

    f.write(str(entry))

f.write(create_footer())
