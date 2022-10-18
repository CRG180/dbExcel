import os
from DBConnect import mysql_connection
from openpyxl import Workbook


class exportExcel:
    def __init__(self, config) -> None:
        self.config = {
    'user': os.getenv('USERNAME'),
    'password': os.getenv('PASSWORD'),
    'host': os.getenv('HOST'),
    'database': os.getenv('DATABASE')
    }

    def exportToExcelWorkbook(self, filepath = "."):
            
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
        print(config['database'])
        wb.save(filename=f"{filepath}/{config['database']}.xlsx")


if __name__ == "__main__":

    from dotenv import load_dotenv
    load_dotenv()
    config = {
        'user': os.getenv('USERNAME'),
        'password': os.getenv('PASSWORD'),
        'host': os.getenv('HOST'),
        'database': os.getenv('DATABASE')
        }
    db = exportExcel(config)
    db.exportToExcelWorkbook()