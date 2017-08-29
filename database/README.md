
# Dragon Chain

# Postgres notes
https://wiki.postgresql.org/wiki/Using_psycopg2_with_PostgreSQL
https://wiki.postgresql.org/wiki/Psycopg2_Tutorial
http://initd.org/psycopg/docs/index.html
http://initd.org/psycopg/docs/connection.html
http://initd.org/psycopg/docs/cursor.html
https://github.com/psycopg/psycopg2/tree/master/examples

import psycopg2
import sys
import pprint
from sqlobject import *


= scheme://[user[:password]@]host[:port]/database[?parameters]

connection_string = 'postgres://dougt:dougt@192.168.1.17:5432/dougt'
connection = connectionForURI(connection_string)
sqlhub.processConnection = connection

sqlhub.processConnection = connectionForURI('')

Person.createTable()
Person(firstName="Doug", lastName="Thompson")


