import sys
import mysql.connector                 # ---> used to connect with database server

"""
Author : Manisha Kumari
Date : 30-05-2022
Place : Kolkata

devName :- Mydev
devPassword :- Prodev
"""
devName = "Mydev"
devPassword = "Prodev"

myHostDB="bjzshlsgcs3weqpucwnr-mysql.services.clever-cloud.com"
myUserDB="ux6vc7gmthyechl1"
myPasswordDb="MDpdyq2rxSnN6JToffVB"
myDataBaseDb="bjzshlsgcs3weqpucwnr"
mydb=mysql.connector.connect(host =myHostDB,user=myUserDB,passwd=myPasswordDb,database=myDataBaseDb)    #establishing the connection

mycursor=mydb.cursor()            # cursor is an object helps to execute the query and fetch records from the database.

class Developer:
    def defineDB(self):
        sql="DROP TABLE IF EXISTS hospital;"
        mycursor.execute(sql)
        sql="CREATE TABLE hospital(reg_no VARCHAR(20) PRIMARY KEY,hosp_name VARCHAR(20) NOT NULL,password VARCHAR(20),loc VARCHAR(20) NOT NULL,pincode VARCHAR(20) NOT NULL,contact_no VARCHAR(20),bed_no VARCHAR(20));"
        mycursor.execute(sql)
        mydb.commit()
    def viewDB(self):
        sql="SELECT * FROM hospital;"
        mycursor.execute(sql)
        fp=mycursor.fetchall()
        print("{:<10} {:<20} {:13} {:<15} {:<10} {:<10} {:<10}".format("Reg.No", "Name", "Password", "Location", "Pincode", "Contact No", "Bed_No"))
        for i in fp:
            # print(i)
            print("{:<10} {:<20} {:13} {:<15} {:<10} {:<10} {:<10}".format(i[0],i[1],i[2], i[3], i[4], i[5], i[6]))
    def control(self):
        print()
        print("**Welcome Admin**")
        while True:
            print("1 -> DEFINE DATABASE")
            print("2 -> VIEW DATABASE")
            print("0 -> EXIT")
            ch=int(input("Enter the choice: "))
            if ch==0:
                exit(0)
            elif ch==1:
                self.defineDB()
            elif ch==2:
                self.viewDB()
            else:
                print("Invalid Choice")


class User:
    def viewPincodeWise(self):
        pincode=input("Enter the pincode: ")
        sql = "SELECT * FROM hospital WHERE pincode=" + pincode + ";"
        mycursor.execute(sql)
        fp=mycursor.fetchall()
        print("{:<20} {:<15} {:<10} {:<10} {:<10}".format('Name', 'Location','Pincode','Mobile_No','Bed_Number'))
        for i in fp:
            print("{:<20} {:<15} {:<10} {:<10} {:<10}".format(i[1], i[3], i[4], i[5], i[6]))
    def viewHospitalNameWise(self):
        name=input("Enter hospital name: ").upper()
        sql = "SELECT * FROM hospital WHERE hosp_name LIKE '%" + name + "%' ;"
        mycursor.execute(sql)
        fp = mycursor.fetchall()
        print("{:<20} {:<15} {:<10} {:<10} {:<10}".format('Name', 'Location', 'Pincode', 'Mobile_No', 'Bed_Number'))
        for i in fp:
            print("{:<20} {:<15} {:<10} {:<10} {:<10}".format(i[1], i[3], i[4], i[5], i[6]))
    def control(self):
        print("1 -> CHECK HOSPITAL PINCODE WISE")
        print("2 -> CHECK HOSPITAL NAME WISE")
        ch=int(input("Enter the choice: "))
        if ch==1:
            self.viewPincodeWise()
        elif ch==2:
            self.viewHospitalNameWise()
        else:
            print("Invalid Choice")


class Hospital:
    def registration(self):
        reg_no=input("Enter your registration number: ")
        name=input("Enter your Hospital name: ")
        password=input("Enter a suitable password: ")
        reconfirmed_password=input("Enter the password again: ")
        if password==reconfirmed_password:
            loc=input("Enter your location: ").upper()
            pin=input("Enter your pincode: ")
            mobile = input("Enter 10 digit contact number of your hospital:: ")
            while True:
                if len(mobile) != 10:
                    print("Invalid Contact No. ..... Please re-enter")
                else:
                    break
            sql="INSERT INTO hospital(reg_no,hosp_name,password,loc,pincode,contact_no,bed_no) VALUES(%s,%s,%s,%s,%s,%s,%s);"
            val=(reg_no,name,password,loc,pin,mobile,0)
        mycursor.execute(sql,val)
        mydb.commit()
    def changeBedNumber(self):
        reg_no = input("Enter your registration number: ")
        password = input("Enter your password: ")
        sql="SELECT password FROM hospital WHERE reg_no="+reg_no+";"
        mycursor.execute(sql)
        fp=mycursor.fetchall()
        if fp[0][0]==password:
            no_of_bed=input("Enter number of bed: ")
            sql="UPDATE hospital SET bed_no='"+no_of_bed+"' WHERE reg_no='"+reg_no+"' ;"
            # print(sql)
            mycursor.execute(sql)
            mydb.commit()
    def control(self):
        print("1 REGISTRATION: ")
        print("2 CHANGE BED NUMBER: ")
        ch=int(input("Enter the choice: "))
        if ch==1:
            self.registration()
        elif ch==2:
            self.changeBedNumber()
        else:
            print("Invalid Choice")

def main():
    print("1 -> FOR DEVELOPER")
    print("2 -> FOR HOSPITAL AUTHORITY")
    print("3 -> FOR USER")
    ch=int(input("Enter the choice: "))
    if ch==1:
        name=input("Enter the Name: ")
        password_=input("Enter password: ")
        if name==devName and password_==devPassword:
            dev=Developer()
            dev.control()
        else:
            print(" You have entered wrong name or password")
    elif ch==2:
        hosp=Hospital()
        hosp.control()
    elif ch==3:
        user=User()  
        user.control()

if __name__=="__main__":
    main()