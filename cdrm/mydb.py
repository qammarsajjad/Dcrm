import  mysql.connector


dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '001122',
)

cursorObject = dataBase.cursor()


cursorObject.execute(' CREATE DATABASE cdrm')

print('All Done!')

