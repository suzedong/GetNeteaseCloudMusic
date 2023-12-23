import os
import pyfiglet
import tkinter as tk
import threading
from tkinter import filedialog

import DownloadGUI
import GetList

# 创建一个布尔变量来控制下载线程
stop_download = False
stop_select = False
# 创建一个 Event 对象用于控制下载线程
stop_event = threading.Event()


def select_directory():
    initial_dir = os.path.expanduser("~/Downloads")  # 初始路径
    directory = filedialog.askdirectory(initialdir=initial_dir)  # 选择文件夹
    root_dir_entry.delete(0, tk.END)  # 清空输入框
    root_dir_entry.insert(0, directory)  # 输入文件夹路径


def stop_download_music():
    global stop_download
    stop_download = True
    stop_event.set()  # 设置 Event 对象，通知下载线程停止下载
    state_change(tk.NORMAL)


def stop_select_pages():
    global stop_select
    stop_select = True
    select_state_change(tk.NORMAL)


def state_change(state):
    input_entry.config(state=state)
    page_entry.config(state=state)
    index_entry.config(state=state)
    root_dir_entry.config(state=state)
    select_button.config(state=state)
    start_button.config(state=state)
    select_pages_button.config(state=state)
    stop_select_button.config(state=state)


def select_state_change(state):
    select_pages_button.config(state=state)


def select_pages():
    global stop_select
    select_state_change(tk.DISABLED)
    pages_text.delete(1.0, tk.END)
    stop_select = False
    # 创建一个新线程用于下载
    download_thread = threading.Thread(target=select_pages_thread)
    download_thread.start()


def select_pages_thread():
    input_value = input_entry.get()
    page_numbers = page_entry.get()
    index_value = index_entry.get()
    for page_number in range(int(page_numbers)):
        if stop_select:
            pages_text.insert(tk.END, f"在第{page_number + 1}页-停止查询!!!\n", "red")
            pages_text.see(tk.END)
            # 如果停止按钮被点击，终止下载
            break
        pages_text.insert(tk.END, f"开始请求第{page_number + 1}页数据", "bold")
        pages_text.see(tk.END)
        data_array = GetList.get_list(input_value, page_number, index_value)  # 获取搜索结果
        pages_text.insert(tk.END, f"->获取到{len(data_array)}条数据\n", "green")
        pages_text.see(tk.END)

        if len(data_array) > 0:
            # 显示查询结果
            index_int = 1
            for item in data_array:
                names = [i.get('name', '') for i in item.get('ar', [])]
                result = ','.join(names)
                pages_text.insert(tk.END, f"{index_int}.{result} - {item['name']} "
                                          f"时长:{round(item['dt']/1000/60, 2)}分钟\n")
                index_int += 1

            pages_text.see(tk.END)

    if not stop_select:
        pages_text.insert(tk.END, f"{page_numbers}页-查询完成!!!\n", "green")
        pages_text.see(tk.END)

    select_state_change(tk.NORMAL)


def download_music():
    # ...
    global stop_download
    state_change(tk.DISABLED)
    result_text.delete(1.0, tk.END)
    pages_text.delete(1.0, tk.END)
    stop_download = False
    stop_event.clear()
    # 创建一个新线程用于下载
    download_thread = threading.Thread(target=download_music_thread)
    download_thread.start()


def download_music_thread():
    input_value = input_entry.get()
    page_numbers = page_entry.get()
    index_value = index_entry.get()
    root_dir = root_dir_entry.get()

    # 下载完成后的回调函数，重新启用状态为 DISABLED 的组件
    def download_complete_callback():
        print(f"{page_number + 1} >= {int(page_numbers)}")
        if page_number + 1 >= int(page_numbers):
            # 如果是最后一个页面，重新启用组件
            state_change(tk.NORMAL)

    for page_number in range(int(page_numbers)):
        if stop_download:
            # 如果停止按钮被点击，终止下载
            break
        result_text.insert(tk.END, f"开始请求第{page_number + 1}页数据", "bold")
        result_text.see(tk.END)
        data_array = GetList.get_list(input_value, page_number, index_value)  # 获取搜索结果
        result_text.insert(tk.END, f"->获取到{len(data_array)}条数据\n", "green")
        result_text.see(tk.END)

        pages_text.insert(tk.END, f"第{page_number + 1}页\n", "green")
        if len(data_array) > 0:
            # 显示查询结果
            index_int = 1
            for item in data_array:
                names = [i.get('name', '') for i in item.get('ar', [])]
                result = ','.join(names)
                pages_text.insert(tk.END, f"{index_int}.{result} - {item['name']} "
                                          f"时长:{round(item['dt']/1000/60, 2)}分钟\n")
                index_int += 1

            pages_text.see(tk.END)

            result_text.insert(tk.END, f"开始下载第{page_number + 1}页数据\n", "bold")
            result_text.see(tk.END)

            DownloadGUI.download_gui(data_array, root_dir, page_number + 1, result_text, stop_event,
                                     download_complete_callback)
        else:
            result_text.insert(tk.END, f"没有找到第{page_number + 1}页数据\n", "red")


# 创建主窗口
window = tk.Tk()
window.title("音乐下载器")

# title_frame--------
title_frame = tk.Frame(window)
title_frame.pack(anchor="nw")
# 创建标题
tk.Label(title_frame, text=pyfiglet.figlet_format("BreakDay"), font=("Courier", 20)).pack(side="left")
tk.Label(title_frame, text=pyfiglet.figlet_format(" - GetMusic v0.8.0"), font=("Courier", 12)).pack(side="left",
                                                                                                    anchor="s")

# left_frame--------
left_frame = tk.Frame(window)
left_frame.pack(side="left", fill="y")
# grid_frame--------
grid_frame = tk.Frame(left_frame)
grid_frame.pack()

# 创建输入框和标签
tk.Label(grid_frame, text="搜索关键词：").grid(row=0, column=0, sticky="e")
input_entry = tk.Entry(grid_frame)
input_entry.insert(0, "汽车音乐")
input_entry.grid(row=0, column=1)

select_pages_button = tk.Button(grid_frame, text="查询", command=select_pages)
select_pages_button.grid(row=0, column=2, sticky="w")
stop_select_button = tk.Button(grid_frame, text="停止", command=stop_select_pages)
stop_select_button.grid(row=1, column=2, sticky="w")

pages_label = tk.Label(grid_frame, text="数量：")
pages_label.grid(row=1, column=0, sticky="e")
number_frame = tk.Frame(grid_frame)
number_frame.grid(row=1, column=1, sticky="w")
page_var = tk.StringVar()
page_var.set("1")
page_entry = tk.Spinbox(number_frame, from_=1, to=10, width=2, textvariable=page_var)
page_entry.pack(side="left")
p_label = tk.Label(number_frame, text="页 每页")
p_label.pack(side="left")
index_var = tk.StringVar()
index_var.set("10")
index_entry = tk.Spinbox(number_frame, from_=10, to=100, increment=10, width=3, textvariable=index_var)
index_entry.pack(side="left")
i_label = tk.Label(number_frame, text="条")
i_label.pack(side="left")

tk.Label(grid_frame, text="下载文件的根目录：").grid(row=3, column=0, sticky="e")
root_dir_entry = tk.Entry(grid_frame)
default_dir = os.path.expanduser("~/Downloads/GetMusic")
root_dir_entry.insert(0, default_dir)
root_dir_entry.grid(row=3, column=1)

# 添加文件夹选择按钮
select_button = tk.Button(grid_frame, text="选择文件夹", command=select_directory)
select_button.grid(row=3, column=2, sticky="w")

# 创建一个框架来容纳按钮
button_frame = tk.Frame(left_frame)
button_frame.pack(pady=10)

# 创建开始下载按钮
start_button = tk.Button(button_frame, text="开始下载", command=download_music)
start_button.pack(side=tk.LEFT, padx=10)

# 创建停止下载按钮
stop_button = tk.Button(button_frame, text="停止下载", command=stop_download_music)
stop_button.pack(side=tk.LEFT, padx=10)

# 创建结果标签
result_frame = tk.Frame(left_frame, padx=5, pady=5)
result_frame.pack(fill="both", expand=True)
result_text = tk.Text(result_frame)
result_text.tag_config("bold", font=("Arial", 12, "bold"))
result_text.tag_config("red", foreground="red")
result_text.tag_config("green", foreground="green")
result_text.insert(tk.END, "Hello, World!")
result_text.pack(fill="both", expand=True)

# right_frame--------
right_frame = tk.Frame(window)
right_frame.pack(fill="both", expand=True)

tk.Label(right_frame, text="查询结果:-----------------------").pack(side="top", anchor="w", padx=5, pady=5)
pages_text = tk.Text(right_frame)
pages_text.tag_config("bold", font=("Arial", 12, "bold"))
pages_text.tag_config("red", foreground="red")
pages_text.tag_config("green", foreground="green")
pages_text.pack(side="top", fill="both", expand=True, anchor="w", padx=5, pady=5)
tk.Button(right_frame, text="退出", command=window.destroy).pack(side="bottom", anchor="e", padx=5, pady=5)

# 运行主循环
window.mainloop()
