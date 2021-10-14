import os
import datetime

tokenVK = 'vk_token.txt'
tokenYa = 'ya_token.txt'


def get_token_id(file_name):
    with open(os.path.join(os.getcwd(), file_name), 'r') as token_file:
        token = token_file.readline().strip()
        id = token_file.readline().strip()
    return [token, id]


def get_max_dpi(dict_in_search):
    max_dpi = 0
    for a in range(len(dict_in_search)):
        file_dpi = dict_in_search[a].get('width') * dict_in_search[a].get('height')
        if file_dpi > max_dpi:
            max_dpi = file_dpi
            need_elem = a
            return dict_in_search[need_elem].get('url'), dict_in_search[need_elem].get('type')


def get_time(time_un):
    time_bc = datetime.datetime.fromtimestamp(time_un)
    str_time = time_bc.strftime('%Y-%m-%d time %H-%M-%S')
    return str_time
