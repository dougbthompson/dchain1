#!/bin/python

# psql -h 192.168.1.17 -U dougt -W dougt
# connection_string = 'postgres:user:password@host:port/database'

import psycopg2
import sys
import pprint

from sqlobject import *

class Person(SQLObject):
    firstName = StringCol()
    middleInitial = StringCol(length=1, default=None)
    lastName = StringCol()

connection_string = 'postgres:dougt:dougt@192.168.1.17:5432/dougt'
connection = connectionForURI(connection_string)
sqlhub.processConnection = connection

Person.createTable()
p1 = Person.get(1)
p1

