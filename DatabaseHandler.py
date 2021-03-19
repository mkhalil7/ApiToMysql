import mysql.connector

host= "localhost"
user =" "
password = ""
database= ""




def connect_to_db(host,user,password):
    mydb = mysql.connector.connect(host=host,user=user,password=password)



