import mysql.connector

try:
    bd = mysql.connector.connect(
    user='root',
    password='unifeob@123',
    host='127.0.0.1',
    database='bancopi_funilaria')
    cursor = bd.cursor()

except mysql.connector.Error as err:
    print("Erro ao conectar no bando de dados")
    print(err)