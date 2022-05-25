import sys
import mysql.connector
myHostDB="bjzshlsgcs3weqpucwnr-mysql.services.clever-cloud.com"
myUserDB="ux6vc7gmthyechl1"
myPasswordDb="MDpdyq2rxSnN6JToffVB"
myDataBaseDb="bjzshlsgcs3weqpucwnr"
mydb=mysql.connector.connect(host =myHostDB,user=myUserDB,passwd=myPasswordDb,database=myDataBaseDb)

mycursor=mydb.cursor()
# sql="create table tb (bedno varchar(25),room_no varchar(20));"

# mycursor.execute(sql)
# t=mycursor.fetchall()
# print(t)
sql="insert into values('"