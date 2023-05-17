# coding:utf-8
# time: 2023/5/16
# author: evan
# python操作mysql

import mysql.connector.pooling

pool = mysql.connector.pooling.MySQLConnectionPool(
    host='192.168.31.192',
    port=3306,
    user='root',
    password='19970311',
    database='news_system',
    pool_size=10
)

con = pool.get_connection()

try:
    # con.start_transaction()
    cursor = con.cursor()
    sql = "select * from t_user where id=1"
    cursor.execute(sql)
    # con.commit()
    result = cursor.fetchall()
    for i in result:
        print(i)
except Exception as e:
    # if "con" in dir():
    #   con.rollback()
    print(e)
finally:
    if "con" in dir():
        con.close()
