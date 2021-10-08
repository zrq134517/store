# 增，删，改
import pymysql
host="localhost"
user="root"
password="root"
database="bank"

def update(sql,param):
    # 连接
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()  # 控制台
    cursor.execute(sql,param)
    # 数据库提交到数据库里
    con.commit()
    # 关闭资源
    cursor.close()
    con.close()

def select(sql,param,mode="all",size=1):
    # 连接
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()  # 控制台
    cursor.execute(sql,param)
    if mode == "all":
        return cursor.fetchall()
    elif mode == "one":
        return cursor.fetchone()
    elif mode == "many":
        return cursor.fetchmany(size)
    # 数据库提交到数据库里
    con.commit()
    # 关闭资源
    cursor.close()
    con.close()