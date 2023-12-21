import requests
import os
import GetList
import Utils
import time

global file_path


def check_and_remove_empty_folder(folder_path):
    # 检查文件夹是否为空
    if not os.listdir(folder_path):
        # 如果为空，删除文件夹
        os.rmdir(folder_path)
        Utils.print_colored(f"删除'{folder_path}'文件夹!!!", "31")
        # 同时检查并递归删除父文件夹
        parent_folder = os.path.dirname(folder_path)
        if not os.listdir(parent_folder):
            os.rmdir(parent_folder)
            Utils.print_colored(f"删除'{parent_folder}'文件夹!!!", "31")


def get_file(songs, root_dir, page_number):
    global file_path
    index = 0
    for song in songs:
        index = index + 1

        name = song['name']
        song_id = song['id']
        ar_name = song['ar'][0]['name']
        # print(f"第{page_number}页-第{index}首: {ar_name} - {name} - {song_id}")

        data_array = GetList.get_song(song_id)
        url = data_array[0]['url']
        br = data_array[0]['br']
        size = data_array[0]['size']
        song_time = data_array[0]['time']
        # print(f"第{page_number}页-第{index}首-下载地址: {url}")

        # 控制请求频率，间隔 1 秒
        # time.sleep(1)

        try:
            file_path = Utils.download_file(url, ar_name, name, root_dir)

            print(f"第{page_number}页-第{index + 1}首-已下载文件: {file_path} "
                  f"码率: {br/1000}K 大小: {round(size/1024/1024, 2)}M 时长: {round(song_time/1000/60, 2)}分钟")
            # 判断文件大小
            file_size = os.path.getsize(file_path)
            if file_size < 3000000:  # 3M
                os.remove(file_path)
                Utils.print_colored(f"但是文件小于3M已经删除!!!", "31")
                # 检查并删除空文件夹
                check_and_remove_empty_folder(os.path.dirname(file_path))
        except requests.exceptions.HTTPError as e:
            Utils.print_colored(f"第{page_number}页-第{index + 1}首-下载文件失败: {e}", "31")
            # 删除下载过程中产生的文件
            if os.path.exists(file_path):
                os.remove(file_path)
                Utils.print_colored(f"第{page_number}页-第{index + 1}首-删除文件: {file_path}", "31")
