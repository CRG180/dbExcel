import os
from dotenv import load_dotenv
from DBConnect import mysql_connection
from openpyxl import Workbook


load_dotenv()
config = {
'user': os.getenv('USERNAME'),
'password': os.getenv('PASSWORD'),
'host': os.getenv('HOST'),
'database': os.getenv('DATABASE')
 }


with mysql_connection(**config) as conn:
    with conn.cursor() as cursor:

        cursor.execute("SHOW TABLES;")
        tables = {i[0]:[] for i in cursor }

        for table in tables:
            cursor.execute(f"SHOW columns FROM {table}")
            tables[table] = [column[0] for column in cursor.fetchall()]


# create excel workbook
wb = Workbook()

for table  in tables.keys():
    _sheet = wb.create_sheet(title=table)
    _sheet.append(tables[table])


del wb['Sheet']
wb.save(filename="test.xlsx")
