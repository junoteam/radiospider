#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- by Alex -*-

from common.MysqlConnect import MysqlConnect
from scripts.RadioSpider import RadioSpider
from scripts.ParserCountries import ParseCountry

class SpiderRun(object):

    def app_run(self):

        """test query"""
        testQuery = 'SELECT * from radio_stations LIMIT 5;'
        mysqlRun = MysqlConnect()
        result = mysqlRun.make_select(testQuery)
        for row in result:
            print row[0], row[1], row[2], row[3], row[4]

if __name__ == '__main__':

    #parserObj = RadioSpider()
    #parserObj.radioParser()

    loc = "Vanuatu"

    parserCountries = ParseCountry()
    parserCountries.get_country(loc)
