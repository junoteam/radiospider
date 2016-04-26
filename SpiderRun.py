#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- by Alex -*-

from common.MysqlConnect import MysqlConnect
from scripts.RadioSpider import RadioSpider

class SpiderRun(object):

    def app_run(self):

        """test query, nothing to do with it ¯\_(ツ)_/¯ """
        testQuery = 'SELECT * from radio_stations LIMIT 5;'
        mysqlRun = MysqlConnect()
        result = mysqlRun.make_select(testQuery)
        for row in result:
            print row[0], row[1], row[2], row[3], row[4]

if __name__ == '__main__':

    # Main staff run here

    parserObj = RadioSpider()
    parserObj.radioParser()
