import pymysql
import datetime
from tkinter import Tk, ttk
from tkinter import messagebox
def gui_mysql():

    def fetch_data():
        try:
            # 连接到mysql数据库（假设你有一个名为'stock'的数据库和一个名为'sailisi'的表）
            conn = pymysql.connect(
                    host='localhost',
                    user='root',
                    password='Wqz20050213',
                    database='stock',
             )
            cursor = conn.cursor()

            # 执行查询
            cursor.execute('SELECT * FROM sailisi')
            rows = cursor.fetchall()

            # 清除Treeview中的旧数据（如果有的话）
            for i in treeview.get_children():
                treeview.delete(i)

            # 在Treeview中显示新数据
            # 将timestamp转换为日期格式并显示
            # 将timestamp转换为日期格式并显示
            for row in rows:
                # 假设 timestamp 是第一列
                timestamp = row[0]
                #print(f"Timestamp: {timestamp}, Type: {type(timestamp)}")  # 打印 timestamp 和其类型

                try:
                    # 尝试将 timestamp 转换为日期格式
                    if isinstance(timestamp, (int, float)):
                        # 如果是毫秒级时间戳，先转换为秒级时间戳
                        if timestamp > 1e10:  # 毫秒级时间戳通常大于10位数
                            timestamp /= 1000
                        date_str = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
                    elif timestamp is None:
                        date_str = "None"  # 如果 timestamp 是 None，显示 "None"
                    else:
                        date_str = str(timestamp)  # 如果不是有效的时间戳，直接显示原值
                except (ValueError, OverflowError) as e:
                    date_str = f"Invalid Timestamp: {timestamp}"  # 处理无效的时间戳

                # 将转换后的日期字符串插入到 Treeview 中
                treeview.insert('', 'end', values=(date_str, *row[1:]))

            # 关闭数据库连接
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # 创建主窗口
    root = Tk()
    root.title("Database Query Result")

    # 创建一个Treeview组件来显示数据
    treeview = ttk.Treeview(root, columns=("timestamp", "volume", "open", "high", "low", "close"), show="headings")  # 假设你的表有n列
    for col in treeview["columns"]:
        treeview.heading(col, text=col)
    for col in treeview["columns"]:#设置为居中对齐
        treeview.column(col, anchor='center')
    treeview.pack(expand=True, fill="both")

    # 创建一个按钮来触发数据获取和显示
    btn_fetch = ttk.Button(root, text="Fetch Data", command=fetch_data)
    btn_fetch.pack(pady=10)

    # 运行主循环
    root.mainloop()
