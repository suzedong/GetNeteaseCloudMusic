# 以下是一些常用的ANSI转义序列示例：

# 控制文本颜色：

# \033[30m：黑色
# \033[31m：红色
# \033[32m：绿色
# \033[33m：黄色
# \033[34m：蓝色
# \033[35m：洋红色
# \033[36m：青色
# \033[37m：白色
# 控制背景颜色：

# \033[40m：黑色背景
# \033[41m：红色背景
# \033[42m：绿色背景
# \033[43m：黄色背景
# \033[44m：蓝色背景
# \033[45m：洋红色背景
# \033[46m：青色背景
# \033[47m：白色背景
# 控制样式：

# \033[1m：粗体
# \033[4m：下划线
# 重置所有样式：

# \033[0m

import os
import requests


def print_colored(text, color_code):
    """
    打印带有颜色的文本。

    参数：
    text (str): 需要打印的文本。
    color_code (int): 文本的颜色代码。

    返回：
    无返回值。
    """
    print(f"\033[{color_code}m{text}\033[0m")


def input_colored(prompt, color_code):
    """
    根据给定的颜色代码，打印带有颜色的提示，并接收用户的输入。

    参数：
    prompt (str) -- 要显示的提示信息
    color_code (int) -- 颜色代码

    返回：
    str -- 用户输入的字符串
    """
    print(f"\033[{color_code}m{prompt}\033[0m", end='')
    return input()


def download_file(file_url, author, title, root_dir):
    """
    下载文件。

    参数：
    url (str) -- 文件的URL
    file_name (str) -- 文件的名称

    返回：
    无返回值。
    """
    response = requests.get(file_url)
    response.raise_for_status()  # 检查是否下载成功

    # 提取扩展名
    ext = os.path.splitext(file_url)[1]

    author = author.replace("/", "-")
    title = title.replace("/", "-")
    # 构造文件夹名和文件名
    folder_name = author
    file_name = f"{author} - {title}{ext}"

    # 创建文件夹（如果不存在）
    folder_path = os.path.join(root_dir, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # 下载文件并保存到相应的文件夹中
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'wb') as file:
        file.write(response.content)

    return file_path
