from climb import get_climb
from data_to_mysql import save_to_mysql
from gui_mysql import gui_mysql
from k_line import convert_to_float
from k_line import k_line
import sys


def get_save_success():
    items=get_climb()#从网页爬取数据items，由于网站cooik常常更换，所以此处不使用老cooik再爬
    database = 'stock'
    save_to_mysql(database,items)#存入mysql数据库“stock”当中，第一次时已存入，此处无需再次写入




if __name__ == '__main__':
    if len(sys.argv)>0 and sys.argv[1]=='no-rget':
        print("本次不更新数据")
    else:
        get_save_success()

#gui展示数据库中存储的数据
gui_mysql()
#从数据库中读取数据，画出K线图和柱状图
k_line()


