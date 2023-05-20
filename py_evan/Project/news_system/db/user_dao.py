# coding:utf-8
# time: 2023/5/17
# author: evan
from .mysql_pool import pool


class UserDao:
    def login(self, username: str, password: str):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "select count(1) from t_user where username=%s and aes_decrypt((unhex(password)),'leon')=%s"
            cursor.execute(sql, (username, password))
            count = cursor.fetchone()[0]
            return True if count == 1 else False
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    def search_user_role(self, username: str):
        """
        查询用户角色
        :param username:
        :return:
        """
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "select tr.role_name  from t_user join t_role tr on t_user.role_id = tr.id " \
                  "where t_user.username=%s"
            cursor.execute(sql, (username,))
            role = cursor.fetchone()[0]
            return role
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    def insert_user(self, username, password, email, role_id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "insert into t_user(username, password, email, role_id) values(%s, hex(aes_encrypt(%s,'leon')),%s,%s)"
            cursor.execute(sql, (username, password, email, role_id))
            con.commit()
        except Exception as e:
            print(e)
            con.rollback()
        finally:
            if 'con' in dir():
                con.close()

    def search_count_page(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "select ceil(count(1)/5) from  t_user"
            cursor.execute(sql)
            return cursor.fetchone()[0]

        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    def search_list(self, page):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "select u.id,u.username, t.role_name from t_user u join t_role t on u.role_id=t.id limit %s,%s"
            cursor.execute(sql, ((page - 1) * 5, 5))
            return cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    def delete_by_id(self, user_id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "delete from t_user where id=%s"
            cursor.execute(sql, [user_id])
            con.commit()
        except Exception as e:
            print(e)
            con.commit()
        finally:
            if 'con' in dir():
                con.close()

    def update(self, user_id, username, password, email, role_id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "update t_user set username=%s,password=hex(aes_encrypt(%s,'leon')),email=%s,role_id=%s where id=%s"
            cursor.execute(sql, [username, password, email, role_id, user_id])
            con.commit()
        except Exception as e:
            print(e)
            con.commit()
        finally:
            if 'con' in dir():
                con.close()

    def search_userid(self, username):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "select id from t_user where username=%s"
            cursor.execute(sql, [username])
            return cursor.fetchone()[0]
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()


if __name__ == '__main__':
    user_dao = UserDao()
    print(user_dao.search_userid('evan'))
