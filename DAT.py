# -*- coding:utf-8 -*-

import getopt
import sys
from dat.insert_data import insert
from dat.output import output, write
from dat.modify_table import modify

help = 'Usage: python DAT.py [OPTION]...\n\n'
help += '''Operation Mode options:
-i                                  Import mode
-o                                  Output mode
-h | --help                         Print help and exit.
\n'''
help += '''Import options: (with '-i' option)
-f | --file                     File to be imported
-t | --table                    Table to be imported to
-a | --init                     Whether create table, only used when the first time of import operation for each table
\n'''
help += '''Output options: (with '-o' option)
-r | --report                   Templates which will be included in the report, if more than one template,use ',' to seperate.
                                e.g: '-r 1000,1001,1002'
                                If all the templates need to be included use '-r ALL'
\n'''


def get_para(argv):
    para = {'__table__': '',
            '__file__': '',
            '__init__': 0,
            '__mode__': 0,
            '__report__': ''}
    try:
        opts, args = getopt.getopt(
            argv, "hioaf:t:k:s:r:",
            ['help', 'file', 'table', 'report', 'init'])
    except getopt.GetoptError:
        print "try 'DAT.py --help' or 'DAT.py -h' for more options"
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print 'python DAT.py -i -f <file> -t <table> [-a]'
            print 'python DAT.py -o -r <report>'
            print help
            sys.exit()
        elif opt in ("-i", ):
            para['__mode__'] = 1
        elif opt in ("-o",):
            para['__mode__'] = 2
        elif opt in ("-a", "--init"):
            para['__init__'] = 1
        elif opt in ("-r", "--report"):
            para['__report__'] = arg
        elif opt in ("-f", "--file"):
            para['__file__'] = arg
        elif opt in ("-t", "--table"):
            para['__table__'] = arg
    return para


def main(para):
    if para['__mode__'] == 1:
        modify(para['__file__'])
        print "Start to import data to table %s ...\n" % para['__table__']
        insert(para['__file__'], para['__table__'],
               para['__init__'])
    elif para['__mode__'] == 2:
        write(output(para['__report__']))


if __name__ == '__main__':
    para = get_para(sys.argv[1:])
    main(para)
