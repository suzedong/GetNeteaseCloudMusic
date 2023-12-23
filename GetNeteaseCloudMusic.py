import sys
import os
import pyfiglet

import Config
import Utils
import GetList
import Download

result = pyfiglet.figlet_format("BreakDay")
print(result)
print(f"\033[35;1m接口服务地址：{Config.url} ，接口技术由 https://github.com/Binaryify/NeteaseCloudMusicApi 提供。\033[0m")
Utils.print_colored("本程序由SZD提供支持。献给茜茜", "34;1")

# 检查命令行参数数量
if len(sys.argv) >= 4:
    input_value = sys.argv[1]
    page_value = sys.argv[2]
    index_value = sys.argv[3]
    root_dir = sys.argv[4]
else:
    # 默认值
    input_value = None  # '汽车音乐'
    page_value = None  # '1‘ 多少页
    index_value = None  # '10' 每页多少条
    root_dir = None  # os.path.expanduser('~/Downloads/GetMusic')  # 默认为用户的下载文件夹

    # 提示用户输入参数并使用默认值
    if not input_value:
        input_value = Utils.input_colored("请输入搜索关键词（默认为'汽车音乐'）：", "32;4") or '汽车音乐'
        print(f"您输入的文本是：{input_value}")
    if not page_value:
        page_value = Utils.input_colored("请输入要下载的页数（指定页数，如：'10'，默认为'1'）：", "32;4") or '1'
        print(f"您输入的文本是：{page_value}")
    if not index_value:
        index_value = Utils.input_colored("请输入要下载每页数量（如：'30'，默认为 '10'）：", "32;4") or '10'
        print(f"您输入的文本是：{index_value}")
    if not root_dir:
        root_dir = Utils.input_colored("请输入下载文件的根目录（默认为'~/Downloads/GetMusic'）：",
                                       "32;4") or os.path.expanduser('~/Downloads/GetMusic')
        print(f"您输入的文本是：{root_dir}")


for page_number in range(int(page_value)):
    # 获取搜索结果
    data_array = GetList.get_list(input_value, page_number, int(index_value))
    # print(data_array)
    Download.get_file(data_array, root_dir, page_number + 1)
