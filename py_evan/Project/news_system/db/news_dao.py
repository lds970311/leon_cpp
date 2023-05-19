# coding:utf-8
# time: 2023/5/17
# author: evan
from ...news_system.db.mysql_pool import pool


class NewsDao:
    def search_unreview_list(self, page):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = '''       
                    select n.id,
                       n.title,
                       t.type_name,
                       u.username
                from t_news n
                         join t_type t on n.type_id = t.id
                         join t_user u on n.editor_id = u.id
                where n.state = %s
                order by n.create_time desc
                limit %s,%s
            '''
            cursor.execute(sql, ('待审批', (page - 1) * 5, 5))
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    def search_unreview_count_page(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "select ceil(count(1)/5) from t_news where state=%s"
            cursor.execute(sql, ['待审批'])
            role = cursor.fetchone()[0]
            return role
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    def update_unreview_news(self, news_id):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            con.start_transaction()
            sql = "update t_news set state='已审批' where id=%s"
            cursor.execute(sql, [news_id])
            con.commit()
        except Exception as e:
            con.rollback()
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    # 查询新闻列表
    def search_list(self, page):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT n.id,n.title,t.type_name,u.username " \
                  "FROM t_news n JOIN t_type t ON n.type_id=t.id " \
                  "JOIN t_user u ON n.editor_id=u.id " \
                  "ORDER BY n.create_time DESC " \
                  "LIMIT %s,%s"
            cursor.execute(sql, ((page - 1) * 10, 10))
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 查询新闻总页数
    def search_count_page(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT CEIL(COUNT(*)/10) FROM t_news"
            cursor.execute(sql)
            count_page = cursor.fetchone()[0]
            return count_page
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 删除新闻
    def delete_by_id(self, id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "DELETE FROM t_news WHERE id=%s"
            cursor.execute(sql, [id])
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()