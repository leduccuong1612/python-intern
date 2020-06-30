import csv
import MySQLdb
mydb = MySQLdb.connect(host='localhost',user='root',password='z123x456',db='leduccuong')
cursor = mydb.cursor()
csv_data = csv.reader(open('/home/leduccuong/PycharmProjects/h/venv/Dev Training1/customer.csv'))
cursor.execute('CREATE TABLE IF NOT EXISTS customer(customerid INT PRIMARY KEY,firstname VARCHAR(255),lastname VARCHAR(255),companyname VARCHAR(255),billingaddress1 VARCHAR(255),billingaddress2 VARCHAR(255),city VARCHAR(255),state VARCHAR(255),postalcode VARCHAR(255),country VARCHAR(255),phonenumber VARCHAR(255),emailaddress VARCHAR(255),createddate VARCHAR(255))')
next(csv_data)
for row in csv_data:
    cursor.execute('INSERT INTO customer(customerid,firstname,lastname,companyname,billingaddress1,billingaddress2,city,state,postalcode,country,phonenumber,emailaddress,createddate)VALUES(%s, "%s", "%s","%s", "%s", "%s","%s", "%s", "%s","%s", "%s", "%s","%s")',row)
mydb.commit()
cursor.close()
print ("Done")