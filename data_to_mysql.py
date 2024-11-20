import pymysql
from datetime import datetime
import mysql.connector


def save_to_mysql(data,database):#将数据data存入到database数据库中
    stock = pymysql.connect(
        host='localhost',
        user='root',
        password='Wqz20050213',
        database=database,
    )
    # 建立到数据库的链接

    cursor = database.cursor()#连接到数据库当中
    cursor.execute('DROP TABLE IF EXISTS SAILISI')#如果已存在，则先删除
    cursor.execute("""
     CREATE TABLE IF NOT EXISTS SAILISI(
     timesamp bigint not null,
        volume int not null,
        open decimal(8,4) not null,
        high decimal(8,4) not null,
        low decimal(8,4) not null,
        close decimal(8,4) not null,
        chg decimal(8,4) not null,
        percent decimal(8,4) not null,
        turnoverrate decimal(8,4) not null,
        amount decimal(12,1) not null)
    """) # 创建名为sailisi的表，因为本实验爬取的是塞力斯的股票数据
    cursor.execute("TRUNCATE TABLE SAILISI")
    cursor = database.cursor()
    print("开始向数据库插入数据")
    for item in data:
        sql = f"insert into SAILISI values({item[0]}, {item[1]}, {item[2]}, {item[3]}, {item[4]}, {item[5]}, {item[6]}, {item[7]}, {item[8]}, {item[9]})"
        cursor.execute(sql)
    stock.commit()
    stock.close()
    print(f"插入数据成功，总计{len(data)}")