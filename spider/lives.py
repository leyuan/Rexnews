#encoding:UTF-8
from bs4 import BeautifulSoup
import urllib2

def create_header():
    return """
    <!doctype html>
        <html lang="en">
        <head>
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
        <style>
            .page-content-wrap {
                padding: 0;
                padding-top: 60px;
            }

            .entry {
                margin-bottom: 10px;
            }

            footer {
                margin-top: 60px;
            }
        </style>

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

                    <h2 class="title">Live Feed</h2>

                    <div class="content-element">
                        <div class="entry-box style-2">



    """

def create_footer():
    return """
        </div>
            </div>

            </div>

            <!-- - - - - - - - - - - - - end Content - - - - - - - - - - - - - - - -->

            <!-- - - - - - - - - - - - - - Footer - - - - - - - - - - - - - - - - -->

            <footer id="footer" class="footer">

            <!-- top footer -->
            <div class="top-footer">

                <div class="container">

                <div class="row align-items-center">
                    <div class="col-lg-3 col-md-12">

                    <a href="index.html" class="logo"><img src="images/logo2.png" alt=""></a>

                    </div>
                    <div class="col-lg-6 col-md-12 align-center">

                    <ul class="menu-list">

                        <li><a href="#">Write for Us</a></li>
                        <li><a href="#">Terms & Conditions</a></li>
                        <li><a href="#">Privacy Policy</a></li>
                        <li><a href="#">Contact</a></li>
                        <li><a href="#">Register</a></li>

                    </ul>

                    </div>
                    <div class="col-lg-3 col-md-12 align-right">

                    <ul class="social-icons">

                        <li><a href="#"><i class="icon-facebook"></i></a></li>
                        <li><a href="#"><i class="icon-twitter"></i></a></li>
                        <li><a href="#"><i class="icon-rss"></i></a></li>
                        <li><a href="#"><i class="icon-hash"></i></a></li>

                    </ul>

                    </div>
                </div>

                </div>

            </div>

            <!-- main footer -->
            <div class="main-footer">

                <div class="container">

                <div class="row">

                    <div class="col-lg-3 col-md-6 col-sm-12">

                    <div class="widget">

                        <h6 class="widget-title">About</h6>

                        <p>Nemo enim ipsam voluptatem quia voluptas aut fugit, sed quia consequuntur magni dolores eos qui ratione.</p>
                        <p>Est, qui dolorem ipsum quia dolor sit amet, nsectetur, sed quia non numquam eius modi tempora incidunt ut labore. </p>

                    </div>

                    </div>
                    <div class="col-lg-3 col-md-6 col-sm-12">

                    <div class="widget">

                        <h6 class="widget-title">Live Charts</h6>

                        <ul class="chart-list">

                        <li><a href="#">Bitcoin Price</a></li>
                        <li><a href="#">Bitcoin Cash Price</a></li>
                        <li><a href="#">Bitcoin Gold Price</a></li>
                        <li><a href="#">Ethereum Price</a></li>
                        <li><a href="#">Ethereum Classic Price</a></li>
                        <li><a href="#">Litecoin Price</a></li>

                        </ul>

                    </div>

                    </div>
                    <div class="col-lg-3 col-md-6 col-sm-12">

                    <div class="widget">

                        <h6 class="widget-title">Newsletter Sign Up</h6>

                        <p>Subscribe now and get exclusive news, interviews and stories.</p>
                        <form id="newsletter" class="newsletter">
                        <input type="email" name="newsletter-email" placeholder="Enter your email address">
                        <button type="submit" data-type="submit" class="btn btn-style-4"><i class="licon-mailbox-full"></i>Subscribe</button>
                        </form>

                    </div>

                    </div>
                    <div class="col-lg-3 col-md-6 col-sm-12">

                    <div class="widget">

                        <div class="banner-title">Advertisement</div>

                        <a href="#" class="banner"><img src="images/300x250_banner.jpg" alt=""></a>

                    </div>

                    </div>

                </div>

                </div>

            </div>

            <div class="copyright">

                <p>Copyright © 2018 Cryptex. All Rights Reserved.</p>

            </div>

            </footer>

            <!-- - - - - - - - - - - - - end Footer - - - - - - - - - - - - - - - -->

        </div>

        <!-- - - - - - - - - - - - end Wrapper - - - - - - - - - - - - - - -->

        <!-- JS Libs & Plugins
        ============================================ -->
        <script src="js/libs/jquery.modernizr.js"></script>
        <script src="js/libs/jquery-2.2.4.min.js"></script>
        <script src="js/libs/jquery-ui.min.js"></script>
        <script src="js/libs/retina.min.js"></script>
        <script src="plugins/instafeed.min.js"></script>
        <script src="plugins/fancybox/jquery.fancybox.min.js"></script>
        <script src="plugins/twitter/jquery.tweet.js"></script>
        <script src="plugins/jquery.queryloader2.min.js"></script>
        <script src="plugins/owl.carousel.min.js"></script>

        <!-- JS theme files
        ============================================ -->
        <script src="js/plugins.js"></script>
        <script src="js/script.js"></script>

        </body>
        </html>
    """

def create_grid():
    return """
        <div class="col-12">
            <div class="entry entry-small">
                <div class="entry-body">
                    <h5 class="entry-title"><a href="#"></a></h5>
                    <p class="entry-body"></p>
                    <a href="#" target="_blank" class="btn btn-small">Read More</a>
                </div>
            </div>
        </div>
    """

def getPage(url):
    request = urllib2.Request(url)
    request.add_header('User-Agent','Mozilla/4.0 (compatible;MSIE 5.5; Windows NT)')
    response=urllib2.urlopen(request)
    return response.read()

url = "http://www.jinse.com/lives"

result=getPage(url)
bs=BeautifulSoup(result, "html.parser")

[style.extract() for style in bs.findAll('style')]

bs.prettify()
[s.extract() for s in bs(['span', 'new'])]

txt = 'lives.html'
f = open(txt, "w")
f.write(create_header())

for entry in bs.find_all('div',class_='live-info'):

    text = entry.a.string
    text = text.split(u'\u3011') # u'\3011' = 】 use to locate the title

    title = text[0][1:]
    message = text[1]

    grid = BeautifulSoup(create_grid(), "html.parser")
    a_s = grid.find_all('a')

    for link in a_s:
        link["target"] = "_blank"
        link["href"] = "http://www.jinse.com" + entry.a["href"]

    grid.h5.a.string = title
    grid.p.string = message
    f.write(str(grid))


f.write(create_footer())
