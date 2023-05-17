# coding:utf-8
# time: 2023/5/17
# author: evan
from .mysql_pool import pool


class RoleDao:
    def search_list(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "select id,role_name from t_role"
            cursor.execute(sql)
            roles = cursor.fetchall()
            return roles
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()


if __name__ == '__main__':
    role_dao = RoleDao()
    print(role_dao.search_list())
