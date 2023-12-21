import requests
import Config
import time


def get_list(input_value, page_number, index_value):
    # 构造请求数据
    data = {
        'keywords': input_value,
        'limit': index_value,
        'offset': page_number * index_value,
    }
    # cloudsearch?keywords = 海阔天空 & limit = 10 & offset = 0
    # 发送POST请求
    response = requests.get(Config.url + 'cloudsearch', headers=Config.headers, data=data)

    # 将响应数据解析为JSON格式
    json_data = response.json()

    # print(json_data)

    if json_data["code"] == 200:
        data_array = json_data['result']["songs"]
    else:
        data_array = []

    # 返回数据数组
    return data_array


def get_song(song_id):
    # print(int(time.time_ns()))
    # 构造请求数据
    data = {
        'id': song_id,
        'level': 'exhigh',
        'timestamp': int(time.time_ns())
    }
    # song/url/v1?id = 2102012051 & level = exhigh
    # 发送POST请求
    # headers = Config.headers
    # headers.update({'cookie': 'GetNeteaseCloudMusic=breakday-zh-cn-' + str(song_id) + '-' + str(time.time_ns())})

    response = requests.get(Config.url + f'song/url/v1?id={song_id}&level=exhigh&timestamp={int(time.time_ns())}')

    # 将响应数据解析为JSON格式
    json_data = response.json()

    # print(json_data)

    if json_data["code"] == 200:
        data_array = json_data['data']
    else:
        data_array = []

    # 返回数据数组
    return data_array
