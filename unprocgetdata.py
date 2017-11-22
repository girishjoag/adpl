#!/usr/bin/python
# import the MySQLdb and sys modules
import MySQLdb
#import pymysql
import sys
# open a database connection
# be sure to change the host IP address, username, password and database name to match your own
connection = MySQLdb.connect (host = "192.168.100.121", port = 3306, user = "root", passwd = "root", db = "bankaccounts")
# prepare a cursor object using cursor() method
cursor = connection.cursor ()
# execute the SQL query using execute() method.
cursor.execute ("select * from accounts,users where accounts.ssn=users.ssn and accounts.status=\"active\"")
# fetch all of the rows from the query
data = cursor.fetchall ();
# print the rows
for row in data :
    print (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9] );
# close the cursor object
cursor.close ()
# close the connection
connection.close ()
# exit the program
sys.exit()
