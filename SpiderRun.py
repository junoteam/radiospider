#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- by Alex -*-

# Necessary imports
from common.MysqlConnector import MysqlConnector
from scripts.RadioSpider import RadioSpider
from utils.Utils import Utils

class SpiderRun(object):

    def app_run(self):

        print "get started"

        """test query"""
        testQuery = 'SELECT * from stations;'
        mysqlRun = MysqlConnector()
        result = mysqlRun.get_select(testQuery)
        print "Result of select: %s:" % result

if "__name__" == '__main__':

    appRun = SpiderRun()
    appRun.app_run()





