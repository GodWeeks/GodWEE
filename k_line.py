import matplotlib.pyplot as plt
import pymysql
import numpy as np
import pandas as pd
import datetime
import matplotlib as mpl
import mplfinance as mpf
import warnings
from mplfinance.original_flavor import candlestick_ohlc
import  matplotlib.dates as mdates

from skimage._shared.utils import convert_to_float

def convert_to_float(data_list):
    try:
        return [float(item) for item in data_list]
    except ValueError as e:
        print(f"转换错误: {e}")
        return None
def k_line():
    # xData=[i for i in range(32)]#画图时可以只选取一个月的数据
    # 这里使用原生字典+列表解析获取到的数据
    yDatas={"timestamp":[],"volume":[],"open":[],"high":[],"low":[],
            "close":[],"chg":[],"percent":[],
            "turnoverrate":[],"amount":[]}
    coon=pymysql.connect(host='localhost',user='root',password='Wqz20050213',db='stock')
    cursor=coon.cursor()
    sql="select * from sailisi"
    cursor.execute(sql)
    data = cursor.fetchall()
    resList = []
    for line in data:
        resList.append(line)
    for line in resList[:32]:
        line = list(line) #将元组转成列表，这样才能执行pop操作

        #xData.append(line.pop(0)/1000)
        yDatas["timestamp"].append(line.pop(0))
        yDatas["volume"].append(line.pop(0))
        yDatas["open"].append(line.pop(0))
        yDatas["high"].append(line.pop(0))
        yDatas["low"].append(line.pop(0))
        yDatas['close'].append(line.pop(0))
        yDatas['chg'].append(line.pop(0))
        yDatas['percent'].append(line.pop(0))
        yDatas['turnoverrate'].append(line.pop(0))
        yDatas['amount'].append(line.pop(0))

    for key in yDatas:
        if key == "timestamp":
            yDatas[key] = pd.to_datetime(yDatas[key], unit='ms')  # 将毫秒级时间戳转换为 datetime 对象
        else:
            yDatas[key] = convert_to_float(yDatas[key])
    #K线图中显示中文字体不可或缺的一环
    plt.rcParams['font.family'] = ['sans-serif']
    plt.rcParams['font.sans-serif'] = ['SimHei']
    #绘制k线图



    yDatas_df = pd.DataFrame(yDatas)
    yDatas_df.set_index('timestamp', inplace=True)
    yDatas_df.dropna()#过滤掉缺失的日期
    y_Datas1=yDatas_df[['open', 'high', 'low', 'close']]
    y_Datas2=yDatas_df[['volume', 'open', 'close']]
    y_Datas1 = y_Datas1.copy()#避免警告
    y_Datas1.loc[:,'MA5']=y_Datas1['close'].rolling(window=5).mean()
    y_Datas1.loc[:,'MA10']=y_Datas1['close'].rolling(window=10).mean()
    # mpf.plot(y_Datas1,type='candle',style='charles',ylabel='价格')
    # ax.set_xticks(xData)
    # # x_labels=["8月{}日".format(i) for i in range(32)]
    # # ax.set_xticklabels(x_labels,rotation=90)
    # name="塞力斯股票日K图"
    # ax.set_title(name,fontsize=30)
    # ax.legend(loc='upper left')
    # ax.grid(True)
    # #绘制成交量柱状图
    # mpf.plot(y_Datas2,type='candle',style='charles',ylabel='数量')
    # # ax2.set_xticks(xData)
    # # ax2.set_xticklabels(x_labels,rotation=90)
    # ax2.grid(True)
    #plt.show()
     # 使用 mplfinance 绘制 K 线图
     # 将日期转换为 matplotlib 日期格式
    dates = mdates.date2num(yDatas_df.index)
     # 创建画布和子图
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(20, 15), gridspec_kw={'height_ratios': [3, 1]})

    # 绘制 K 线图
    ohlc = list(zip(dates, y_Datas1['open'], y_Datas1['high'], y_Datas1['low'], y_Datas1['close']))
    candlestick_ohlc(ax1, ohlc, width=0.6, colorup='g', colordown='r')
    ax1.plot(dates, y_Datas1['MA5'], color='orange', label='MA5')
    ax1.plot(dates,y_Datas1['MA10'], color='purple',label='MA10')

    #ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    #ax1.xaxis.set_major_locator(mdates.DateLocator())
    ax1.set_xticks(dates)
    ax1.set_xticklabels([mdates.num2date(d).strftime('%Y-%m-%d') for d in dates], rotation=45)
    ax1.set_title("塞力斯股票日K图", fontsize=30)
    ax1.grid(True)

    # 绘制成交量柱状图
    ax2.bar(dates, y_Datas2['volume'], color='blue', alpha=0.5, label='成交量')
    #ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    #ax2.xaxis.set_major_locator(mdates.DateLocator())
    ax2.set_xticks(dates)  # 每隔5个数据点设置一个刻度
    ax2.set_xticklabels([mdates.num2date(d).strftime('%Y-%m-%d') for d in dates], rotation=45)
    ax2.set_ylabel('数量')
    ax2.legend(loc='upper left')
    ax2.grid(True)
    # 创建次轴
    ax2_twin = ax2.twinx()
    ax2_twin.bar(dates, y_Datas2['open'], color='green', alpha=0.5, label='开盘价', width=0.3)
    ax2_twin.bar(dates + 0.3, y_Datas2['close'], color='red', alpha=0.5, label='收盘价', width=0.3)
    ax2_twin.set_ylabel('价格')
    ax2_twin.legend(loc='upper right')

    # 调整 y 轴的范围
    min_volume = min(y_Datas2['volume'])
    max_volume = max(y_Datas2['volume'])
    margin = (max_volume - min_volume) * 0.1  # 增加10%的裕度
    ax2.set_ylim(min_volume - margin, max_volume + margin)

    plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.1, hspace=0.2)

    plt.show()

    # fig, (ax1, ax2) = mpf.plot(y_Datas1, type='candle', style='charles', ylabel='价格',
    #                            volume=ax2, ylabel_lower='成交量', show_nontrading=True,
    #                            figratio=(20, 15), figscale=1.5, returnfig=True)
    #
    # ax1.set_title("塞力斯股票日K图", fontsize=30)
    # ax1.legend(loc='upper left')
    # ax1.grid(True)
    #
    # ax2.set_ylabel('数量')
    # ax2.legend(loc='upper left')
    # ax2.grid(True)
    #
    # # 调整 y 轴的范围
    # min_volume = min(y_Datas2['volume'])
    # max_volume = max(y_Datas2['volume'])
    # margin = (max_volume - min_volume) * 0.1  # 增加10%的裕度
    # ax2.set_ylim(min_volume - margin, max_volume + margin)
    #
    # plt.tight_layout()
    # plt.show()
    # fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(20, 15), gridspec_kw={'height_ratios': [3, 1]})
    #
    # # 绘制 K 线图
    # ax1.plot(y_Datas1.index, y_Datas1['high'], color='red', label='最高价')
    # ax1.plot(y_Datas1.index, y_Datas1['low'], color='green', label='最低价')
    # # ax1.plot(y_Datas1.index, y_Datas1['open'], color='black', label='开盘价')
    # ax1.plot(y_Datas1.index, y_Datas1['close'], color='blue', label='收盘价')
    # ax1_twin = ax1.twinx()
    # ax1_twin.plot(y_Datas1.index, y_Datas1['open'], color='black', label='开盘价')
    # ax1_twin.set_ylabel('开盘价')
    # ax1_twin.legend(loc='upper right')
    #
    # ax1.set_title("塞力斯股票日K图", fontsize=30)
    # ax1.legend(loc='upper left')
    # ax1.grid(True)
    #
    # # 绘制成交量柱状图
    # ax2.bar(y_Datas2.index, y_Datas2['volume'], color='blue', alpha=0.5, label='成交量')
    # # ax2.plot(y_Datas2.index, y_Datas2['open'], color='green', label='开盘价')
    # # ax2.plot(y_Datas2.index, y_Datas2['close'], color='red', label='收盘价')
    # ax2.set_ylabel('数量')
    # ax2.legend(loc='upper left')
    # ax2.grid(True)
    #  # 调整 y 轴的范围
    # min_volume = min(y_Datas2['volume'])
    # max_volume = max(y_Datas2['volume'])
    # margin = (max_volume - min_volume) * 0.1  # 增加10%的裕度
    # ax2.set_ylim(min_volume - margin, max_volume + margin)
    #
    #
    # plt.tight_layout()
    # plt.show()


