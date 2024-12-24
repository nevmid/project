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

    def get_id_clients(self):
        try:
            cursor = self.connection.cursor()
            query = f"""SELECT id_client FROM clients"""
            cursor.execute(query)
            result = cursor.fetchall()
            result = [item for sub_tuple in result for item in sub_tuple]
            return result
        except Error as e:
            print(e)
        finally:
            self.close_connection()

    def get_id_products(self):
        try:
            cursor = self.connection.cursor()
            query = f"""SELECT id_product FROM products"""
            cursor.execute(query)
            result = cursor.fetchall()
            result = [item for sub_tuple in result for item in sub_tuple]
            return result
        except Error as e:
            print(e)
        finally:
            self.close_connection()

    def save_to_db_categories(self, item):
        try:
            cursor = self.connection.cursor()
            query = f'''INSERT INTO categories (name_cat) VALUES (%s)'''
            cursor.execute(query, item)
            self.connection.commit()
        except Error as e:
            print(e)
        finally:
            self.close_connection()

    def save_to_db_clients(self, item):
        try:
            cursor = self.connection.cursor()
            query = f'''INSERT INTO clients (name, surname, patronymic, phone) VALUES (%s, %s, %s, %s)'''
            cursor.execute(query, item)
            self.connection.commit()
        except Error as e:
            print(e)
        finally:
            self.close_connection()

    def get_id_categories(self):
        try:
            cursor = self.connection.cursor()
            query = f"""SELECT id_category FROM categories"""
            cursor.execute(query)
            result = cursor.fetchall()
            result = [item for sub_tuple in result for item in sub_tuple]
            return result
        except Error as e:
            print(e)
        finally:
            self.close_connection()

    def save_to_db_clients(self, item):
        try:
            cursor = self.connection.cursor()
            query = f'''INSERT INTO clients (name, surname, patronymic, phone) VALUES (%s, %s, %s, %s)'''
            cursor.execute(query, item)
            self.connection.commit()
        except Error as e:
            print(e)
        finally:
            self.close_connection()

    def get_id_by_name(self, item):
        try:
            cursor = self.connection.cursor()
            query = f'''SELECT id_category FROM categories WHERE name_cat = %s'''
            cursor.execute(query, item)
            return cursor.fetchall()
        except Error as e:
            print(e)
        finally:
            self.close_connection()

    def save_to_db_products(self, row_values):
        try:
            cursor = self.connection.cursor()
            query = f'''INSERT INTO products (category, name_prod, price, quantity) VALUES (%s, %s, %s, %s)'''
            cursor.execute(query, row_values)
            self.connection.commit()
        except Error as e:
            print(e)
        finally:
            self.close_connection()

    def save_to_db_sales(self, item):
        try:
            cursor = self.connection.cursor()
            query = f'''INSERT INTO sales (client, date, product, quantity, amount) VALUES (%s, %s, %s, %s, %s)'''
            cursor.execute(query, item)
            self.connection.commit()
        except Error as e:
            print(e)
        finally:
            self.close_connection()

    def update_categories(self, item, old_value):
        try:
            cursor = self.connection.cursor()
            query = f'''UPDATE categories SET name_cat = %s WHERE name_cat = %s'''
            cursor.execute(query, (item, old_value))
            self.connection.commit()
        except Error as e:
            print(e)
        finally:
            self.close_connection()

    def update_clients(self, id_client, column, new_value):
        try:
            cursor = self.connection.cursor()
            query = f'''UPDATE clients SET {column} = %s WHERE id_client = %s'''
            cursor.execute(query, (new_value, id_client))
            self.connection.commit()
        except Error as e:
            print(e)
        finally:
            self.close_connection()

    def update_products(self, id_pruduct, column, new_value):
        try:
            cursor = self.connection.cursor()
            query = f'''UPDATE products SET {column} = %s WHERE id_product = %s'''
            cursor.execute(query, (new_value, id_pruduct))
            self.connection.commit()
        except Error as e:
            print(e)
        finally:
            self.close_connection()

    def update_sales(self, id_sale, column, new_value):
        try:
            cursor = self.connection.cursor()
            query = f'''UPDATE sales SET {column} = %s WHERE id_sale = %s'''
            cursor.execute(query, (new_value, id_sale))
            self.connection.commit()
        except Error as e:
            print(e)
        finally:
            self.close_connection()

    def delete_record(self, rec_id, table, column):
        try:
            cursor = self.connection.cursor()
            query = f"DELETE FROM {table} WHERE {column} = %s"
            cursor.execute(query, (rec_id))
            self.connection.commit()
            return True
        except Error as e:
            return False
        finally:
            self.close_connection()

    def get_sales_data(self, date):
        try:
            cursor = self.connection.cursor()
            query = f"SELECT SUM(quantity), SUM(amount) FROM sales WHERE date = %s"
            cursor.execute(query, date)
            result = cursor.fetchall()
            result = [item for sub_tuple in result for item in sub_tuple]
            return result
        except Error as e:
            print(e)
            return None
        finally:
            self.close_connection()