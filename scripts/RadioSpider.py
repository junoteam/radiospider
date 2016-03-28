#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- by Alex -*-

from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup
from common.MysqlConnect import MysqlConnect
import re
import urllib
import sys
from string import replace

class RadioSpider(object):

    mysql_obj = MysqlConnect()
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
                    matchObj = re.sub('[;]?\s\([\d]*\)\s?', '', z)
                    if matchObj == 'R&B':
                        matchObj = matchObj.replace('&', '%26')
                    genres_array.append(matchObj)
        return genres_array

    def radioParser(self):

        pages_array = []
        all_genres = self.genresParser()

        for item in range(len(all_genres)):
            radio_url_genres = 'http://vtuner.com/setupapp/guide/asp/BrowseStations/BrowsePremiumStations.asp?sCategory=' + all_genres[item] + '&sBrowseType=Format&sViewBy=&sSortby=&sWhatList=&sNiceLang=&iCurrPage=1'
            url_clean = urllib.urlopen(radio_url_genres)

            soup = BeautifulSoup(url_clean)
            pages = soup.findAll('div')
            for row in pages:
                y = row.findAll('a', {"class":"paging"})
                for row_1 in y:
                    k = row_1.findAll('b')
                    for row_2 in k:
                        l = row_2.getText()
                        pages_array.append(l)

            for number in range(len(pages_array)):
                radio_urls = 'http://vtuner.com/setupapp/guide/asp/BrowseStations/BrowsePremiumStations.asp?sCategory=' + all_genres[item] + '&sBrowseType=Format&sViewBy=&sSortby=&sWhatList=&sNiceLang=&iCurrPage=' + pages_array[number]
                m3u_url = 'http://vtuner.com/setupapp/guide/asp/'
                
                url_ready = urllib.urlopen(radio_urls)
                soup_radios = BeautifulSoup(url_ready)

                main_table = soup_radios.find('table', id='table1').findAll('tr')
                for tab in main_table:
                    table = tab.findAll('table')
                    for tagz in table:
                        oi = tagz.findAll('tr')
                        for tr in oi:
                            url = ''
                            name = ''
                            location = ''
                            genre = ''
                            quality = ''
                            alTds = tr.findAll('td')
                            if len(alTds) < 5:
                                continue
                            if len(alTds) > 0:
                                allTdLinks = alTds[0].findAll('a')
                                if len(allTdLinks) > 0:
                                    url = m3u_url + allTdLinks[0]['href']
                                    url = url.replace('../', '')
                                    print '--- Radio block starts here ---'
                                    print "URL of Radio :" + url
                            if len(alTds) > 1:
                                allTdLinks = alTds[1].findAll('a')
                                if len(allTdLinks) > 0:
                                    name = allTdLinks[0].getText()
                                    print "Name of Radio: " + name
                            if len(alTds) > 2:
                                location = alTds[2].getText()
                                print "Location of Radio: " + location
                            if len(alTds) > 3:
                                allTdLinks = alTds[3].findAll('a')
                                if len(allTdLinks) > 0:
                                    genre = allTdLinks[0].getText()
                                    print "Genre of Radio: " + genre
                            if len(alTds) > 4:
                                    quality = alTds[4].getText()
                                    print "Quality of Radio: " + quality
                                    print '--- Radio block ends here ---'
                                    print "\n"
                            
                            #TODO inserts here
                            query_radio = "INSERT INTO `radio_stations` (`name`, `description`, `website`, `country`, `lng`, `status`) VALUES ('station name', '', '', 'country', '', '');"
                            MysqlConnect.make_insert(query_radio)

















