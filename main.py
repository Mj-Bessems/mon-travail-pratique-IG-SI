import mysql.connector 

mabdd = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123password"
)

mycursor = mabdd.cursor()

mycursor.execute("CREATE DATABASE Bank")