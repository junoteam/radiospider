#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- by Alex -*-

from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup
import re

class RadioSpider(object):

    radio_url_genre = 'http://vtuner.com/setupapp/guide/asp/BrowseStations/BrowsePremiumStations.asp?sCategory=Alternative&sBrowseType=Format&sViewBy=&sSortby=&sWhatList=&sNiceLang=&iCurrPage=1'
    radio_url_format = 'http://vtuner.com/setupapp/guide/asp/BrowseStations/StartPage.asp?sBrowseType=Format'

    def genresParser(self):

        genres_array = []
        soup = BeautifulSoup(urlopen(self.radio_url_format).read())
        #raw_html = soup.prettify()[0:1000000]

        genre_rows = soup.find('table', id='table10').findAll('tr')
        for row in genre_rows:
            d = row.findAll('td')
            for row_2 in d:
                t = row_2.findAll('a')
                for row_3 in t:
                    z = row_3.getText()
                    matchObj = re.sub('\s\([\d]*\)\s?', '', z)
                    genres_array.append(matchObj)

        return genres_array

    def radioParser(self, genre):
        pass

