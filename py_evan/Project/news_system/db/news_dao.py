# coding:utf-8
# time: 2023/5/17
# author: evan
from .mysql_pool import pool


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

    def insert(self, title, editor_id, type_id, content_id, is_top):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            con.start_transaction()
            sql = "insert into t_news(title, editor_id, type_id, content_id, is_top, create_time, update_time, state)  " \
                  "values(%s,%s,%s,%s,%s,now(),now(),'待审批')"
            cursor.execute(sql, (title, editor_id, type_id, content_id, is_top))
            con.commit()

        except Exception as e:
            con.rollback()
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    def search_cache(self, news_id):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "select n.title,u.username,t.type_name,n.content_id,n.is_top,n.create_time  from t_news n  " \
                  "join t_type t on n.type_id=t.id " \
                  "join t_user u on n.editor_id=u.id " \
                  "where n.id = %s"
            cursor.execute(sql, [news_id])
            role = cursor.fetchone()
            return role
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    def search_by_id(self, news_id):
        """
        根据id查找新闻
        :param news_id:
        :return:
        """

        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = '''       
                    select n.id,
                       n.title,
                       t.type_name,
                       n.is_top
                from t_news n
                         join t_type t on n.type_id = t.id
                where n.id=%s
            '''
            cursor.execute(sql, [news_id])
            result = cursor.fetchone()
            return result
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    def update_news(self, news_id, new_title, type_id, content_id, new_is_top):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            con.start_transaction()
            sql = "update t_news set title=%s,type_id=%s,content_id=%s,is_top=%s,update_time=now(),state='待审批' where id=%s"
            cursor.execute(sql, (new_title, type_id, content_id, new_is_top, news_id))
            con.commit()
        except Exception as e:
            con.rollback()
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    def search_content_id(self, id):
        """
        根据新闻id查找content_id
        :param id:
        :return:
        """
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = '''       
                    select  content_id from t_news  where id=%s
            '''
            cursor.execute(sql, [id])
            result = cursor.fetchone()[0]
            return result
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()
