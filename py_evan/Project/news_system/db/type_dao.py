# coding:utf-8
# time: 2023/5/19
# author: evan

from .mysql_pool import pool


class TypeDao:
    def search_list(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "select id,type_name from t_type order by id asc"
            cursor.execute(sql)
            return cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()
