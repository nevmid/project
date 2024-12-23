import pymysql
from pymysql import Error
from config import db_config

class Database:
    def __init__(self):
        self.connection = None

    def connect(self):

            try:
                self.connection = pymysql.connect(
                    host=db_config['mysql']['host'],  # Замените на ваш хост
                    user=db_config['mysql']['user'],  # Замените на ваше имя пользователя
                    password=db_config['mysql']['pass'],  # Замените на ваш пароль
                    database='project'  # Замените на имя вашей базы данных
                )

            except Error as e:
                self.connection = None




    def close_connection(self):
            self.connection.close()



    def get_connection(self):
        return self.connection


    def fetch_all_records(self, table_name):
        try:
            cursor = self.connection.cursor()
            query = f"SELECT * FROM {table_name}"
            cursor.execute(query)
            records = cursor.fetchall()

            return records

        except Error as e:
            print(f"Ошибка выполнения запроса: {e}")
            return None
        finally:
            self.close_connection()

    def fetch_records_from_products(self):
        try:
            cursor = self.connection.cursor()
            query = f"SELECT c.name_cat, p.name_prod, p.price, p.quantity FROM products p JOIN categories c ON p.category = c.id_category"
            cursor.execute(query)
            records = cursor.fetchall()

            return records

        except Error as e:
            print(f"Ошибка выполнения запроса: {e}")
            return None
        finally:
            self.close_connection()

    def insert_row_into_clients(self, row_data):
        try:
            cursor = self.connection.cursor()
            query = f'''INSERT INTO clients (name, surname, patronymic, phone) VALUES (%s, %s, %s, %s')'''
            cursor.execute(query, tuple(row_data))

            self.connection.commit()
        except Error as e:
            print('Error')
        finally:
            self.close_connection()

    def get_categories(self):
        try:
            cursor = self.connection.cursor()
            query = f"""SELECT name_cat FROM categories"""
            cursor.execute(query)
            result = cursor.fetchall()
            result = [item for sub_tuple in result for item in sub_tuple]
            return result
        except Error as e:
            print(e)
        finally:
            self.close_connection()


