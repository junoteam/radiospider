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

        radio_url = 'http://vtuner.com/setupapp/guide/asp/BrowseStations/BrowsePremiumStations.asp?sCategory=Hard%20Rock&sBrowseType=Format&sNiceLOFO=Hard%20Rock'
        soup = BeautifulSoup(urlopen(radio_url).read())

        #raw_html = soup.prettify()[0:1000000]
        #print raw_html

        section = soup.find('table', id='table2')
        print section

        href = section.find('option')
        print href.text

        #h3 = section.find('h3')
        #print h3.text


        #doc = lxml.html.parse(self.radio_url)
        #doc.xpath()

        # for section in doc.xpath('//section[starts-with(@id, "rankings")]'):
        #     print section.xpath('h1[1]/text()')[0]
        #     print section.xpath('h3[1]/text()')[0]
        #     for row in section.xpath('table/tbody/tr'):
        #         cols = row.xpath('td/b/text()')
        #         print '  ', cols[0].ljust(25), ' '.join(cols[1:])
        #     print


