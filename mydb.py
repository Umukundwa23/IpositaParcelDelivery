import pymysql
dataBase = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'MP@trick14'
)
# prepare a cursor object
cursorObject = dataBase.cursor()
# create a database
cursorObject.execute("CREATE DATABASE ipositaDB"
)
print("All Done!")
