#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- by Alex -*-

# Necessary imports
from common.MysqlConnect import MysqlConnect
from scripts.RadioSpider import RadioSpider
from utils.Utils import Utils

class SpiderRun(object):

    def app_run(self):

        """test query"""
        testQuery = 'SELECT * from stations;'
        mysqlRun = MysqlConnect()
        result = mysqlRun.get_select(testQuery)
        print "Result of select: %s:" % result

if __name__ == '__main__':

    appRun = SpiderRun()
    appRun.app_run()
