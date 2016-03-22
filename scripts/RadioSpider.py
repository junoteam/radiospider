#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- by Alex -*-

import lxml.html
from lxml import etree
from io import StringIO, BytesIO
from common.MysqlConnect import MysqlConnect
from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

class RadioSpider(object):

    def RadioParser(self):

        radio_url_genre = 'http://vtuner.com/setupapp/guide/asp/BrowseStations/BrowsePremiumStations.asp?sCategory=Alternative&sBrowseType=Format&sViewBy=&sSortby=&sWhatList=&sNiceLang=&iCurrPage=1'
        radio_url_format = 'http://vtuner.com/setupapp/guide/asp/BrowseStations/StartPage.asp?sBrowseType=Format'
        soup = BeautifulSoup(urlopen(radio_url_format).read())

        #raw_html = soup.prettify()[0:1000000]
        #print raw_html

        genre_rows = soup.find('table', id='table10').findAll('tr')
        for row in genre_rows:
            d = row.findAll('td')
            for row_2 in d:
                t = row_2.findAll('a')
                print t


