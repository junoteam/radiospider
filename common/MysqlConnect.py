#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- by Alex -*-

import MySQLdb

class MysqlConnect(object):

    def __init__(self):
        self.mysql_connect()

    database = None

    def mysql_connect(self):
        if self.database is None:
            try:
                self.database = MySQLdb.connect(host="172.25.60.76",
                                                user="root",
                                                passwd="password",
                                                charset='utf8',
                                                db="upods")
                print "Connected to database..."
            except MySQLdb.Error, e:
                print "Error %d: %s" % (e.args[0], e.args[1])
        else:
            print "Already connected"

    def get_cursor(self):
        db = self.database
        cursor = db.cursor()
        return cursor

    def make_insert(self, sql_query):
        db = self.database
        print "Current DB: %s" % db
        cursor = self.get_cursor()
        insertedId = -1
        try:
            cursor.execute(sql_query)
            db.commit()
            insertedId = cursor.lastrowid
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
            print '====== WRONG SQL QUERY ======'
            print sql_query
            db.rollback()
        cursor.close()
        return insertedId

    def make_select(self, sql_query):
        cursor = self.get_cursor()
        try:
            data = cursor.execute(sql_query)
            data = cursor.fetchall()
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
            print '====== WRONG SQL QUERY ======'
            print sql_query
        return data

    def close_database(self):
        self.database.close()
