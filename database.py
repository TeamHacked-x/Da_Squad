import sqlite3

sql=sqlite3.connect('Database.db', check_same_thread=False)
sql_cursor=sql.cursor()


# class Employee:
#     def create_emp_table(self):
#         sql_cursor.execute('CREATE TABLE IF NOT EXISTS emp_table(emp_id TEXT,emp_name TEXT, marital_status TEXT, child_nb REAL, hourly_rate TEXT, transp TEXT)')
#
#     def add_emp(self, emp_id, emp_name, marital_status, child_nb, hourly_rate, transp):
#         sql_cursor.execute('INSERT INTO emp_table(emp_id, emp_name, marital_status, child_nb, hourly_rate, transp) VALUES(?,?,?,?,?,?)',(emp_id, emp_name, marital_status, child_nb, hourly_rate, transp))
#         sql.commit()
#
#     def view_emp(self):
#         sql_cursor.execute('SELECT * FROM emp_table')
#         return sql_cursor.fetchall()
#
#     def delete_emp(self, emp_name):
#         sql_cursor.execute('DELETE FROM emp_table WHERE emp_name="{}"'.format(emp_name))
#         sql.commit()
#
#     def edit_emp_data(self, n_emp_id, n_emp_name, n_marital_status, n_child_nb, n_hourly_rate, n_transp, emp_id, emp_name, marital_status, child_nb, hourly_rate, transp):
#         sql_cursor.execute("UPDATE emp_table SET emp_id =?, emp_name =?, marital_status =?, child_nb =?, hourly_rate =?, transp =? WHERE emp_id =? and emp_name =? and marital_status =? and child_nb =? and hourly_rate =? and transp =?",(n_emp_id, n_emp_name, n_marital_status, n_child_nb, n_hourly_rate, n_transp, emp_id, emp_name, marital_status, child_nb, hourly_rate, transp))
#         sql.commit()
#         data = sql_cursor.fetchall()
#         return data


class Login():
    def create_usertable(self):
        sql_cursor.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')

    def delete_users(self, username):
        sql_cursor.execute('DELETE FROM userstable WHERE username="{}"'.format(username))
        sql.commit()

    def add_users(self, username, password):
        sql_cursor.execute('INSERT INTO userstable(username,password) VALUES (?,?)', (username, password))
        sql.commit()

    def login_user(self, username, password):
        sql_cursor.execute('SELECT * FROM userstable WHERE username =? AND password = ?', (username, password))
        return sql_cursor.fetchall()

    def view_all_users(self):
        sql_cursor.execute('SELECT * FROM userstable')
        return sql_cursor.fetchall()
