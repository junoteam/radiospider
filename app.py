#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- by Alex Berber -*-

# Necessary imports
from common.MysqlConnector import MysqlConnector
from scripts.RadioSpider import RadioSpider
from utils.Utils import Utils

class App(object):

    def app_run(self):

        """test query"""

        testQuery = 'SELECT * from stations;'
        mysqlRun = MysqlConnector()
        mysqlRun.get_select(testQuery)

if "__name__" == '__main__':

    appRun = App()
    appRun.app_run()





