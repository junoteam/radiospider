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
import datetime

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
                            station_url = ''
                            station_name = ''
                            station_location = ''
                            station_genre = ''
                            station_quality = ''
                            station_updated = datetime.datetime.now()
                            alTds = tr.findAll('td')

                            if len(alTds) < 5:
                                continue
                            if len(alTds) > 0:
                                allTdLinks = alTds[0].findAll('a')
                                if len(allTdLinks) > 0:
                                    station_url = m3u_url + allTdLinks[0]['href']
                                    station_url = station_url.replace('../', '')
                                    print '--- Radio block starts here ---'
                                    print "URL of Radio :" + station_url
                            if len(alTds) > 1:
                                allTdLinks = alTds[1].findAll('a')
                                if len(allTdLinks) > 0:
                                    station_name = allTdLinks[0].getText()
                                    print "Name of Radio: " + station_name
                            if len(alTds) > 2:
                                station_location = alTds[2].getText()
                                print "Location of Radio: " + station_location
                            if len(alTds) > 3:
                                allTdLinks = alTds[3].findAll('a')
                                if len(allTdLinks) > 0:
                                    station_genre = allTdLinks[0].getText()
                                    print "Genre of Radio: " + station_genre
                            if len(alTds) > 4:
                                    station_quality = alTds[4].getText()
                                    print "Quality of Radio: " + station_quality
                                    print '--- Radio block ends here ---'
                                    print "\n"
                            
                            #TODO inserts here
                            query_radio = "INSERT INTO `radio_stations`(`name`, `country`, `updated`) VALUES ('" + station_name + "'," + "'" + station_location + "'," + "'" + str(station_updated) + "');"

                            insert_id = self.mysql_obj.make_insert(query_radio)
                            print "making insert"
                            if insert_id != -1:
                                station_quality = re.sub("\D", "", station_quality)
                                query_url_and_bitrate = "INSERT INTO `radio_station_stream_urls`(`station_id`, `url`, `bitrate`) VALUES('" + str(insert_id) + "'," + "'" + station_url + "'," + "'" + station_quality + "');"
                                self.mysql_obj.make_insert(query_url_and_bitrate)
                            sys.exit(1)

















