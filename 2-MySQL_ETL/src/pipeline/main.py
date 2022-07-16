from util import database_connection, color_codes

try:
    connection = database_connection.databaseConnect()
    print(f"{color_codes.SUCCESS}[+] Connected to database ! {color_codes.END}")
    with connection:
        with connection.cursor() as cursor:
            sql = "SHOW databases;DROP DATABASE IF EXISTS `sql_invoicing`;CREATE DATABASE `sql_invoicing`;USE `sql_invoicing`;"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
        connection.commit()


except:
    print(f"{color_codes.FAILURE}[-] Cannot connect to Database !")
