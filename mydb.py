import mysql.connector

database = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="root",
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE crmdb")

print("All Done!")
