# -*- coding:utf-8 -*-

import MySQLdb
import xlrd
# from .modify_data import modify_data
# from .modify_data import modify_header
from .createtable import createtable


def insertdb(table, db, cursor, _headers, __table__, __hours__):
    rows = table.nrows
    print "%d records founds, start to insert to table.\n" % (rows - 1)
    col = ""
    he = ', '.join(_headers)
    i = 1
    while i < rows:
        row_datas = table.row_values(i)
        for _header in _headers:
            if _header == __hours__:
                if row_datas[_headers.index(_header)] != '':
                    col = col + \
                        "%d, " % int(row_datas[_headers.index(_header)])
                else:
                    col = col + "%d, " % 0
            else:
                col = col + '"%s", ' % row_datas[_headers.index(_header)]
        # col = modify_data(col)
        col = col.replace('.0', '')
        sql_insert = "insert into %s (%s) values (%s)" % (
            __table__, he, col[:-2])
        try:
            cursor.execute(sql_insert)
            db.commit()
        except Exception, e:
            print 'error', sql_insert, '\n'
            raise e
            db.rollback()
        col = ""
        if i % 500 == 0:
            print "%d records has been inserted..." % i
        i += 1
    print "%d records have been inserted..." % (i - 1)


def insert(file, table, sheet, keywords, init):
    data = xlrd.open_workbook('source/%s' % file)
    sheet_data = data.sheets()[sheet]
    headers = []
    headers.extend(sheet_data.row_values(0))
    # headers = modify_header(_headers)
    if init == 1:
        print "Initialize the table for the first import...\n"
        createtable(table, headers, keywords)
    else:
        print "Add data to table %s \n" % table
    db = MySQLdb.connect("localhost", "root", "root", "Data")
    cursor = db.cursor()
    insertdb(sheet_data, db, cursor, headers, table, keywords)
    db.close()
