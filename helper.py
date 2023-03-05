'''
Author: weijay
Date: 2023-03-05 17:00:25
LastEditors: weijay
LastEditTime: 2023-03-05 17:27:35
Description: 額外需要用的東西
'''

import random

def gen_random_file_name():
    """ 產生隨機檔案名稱 """

    file_name = ""

    for _ in range(10):

        ascii_num = random.randint(97, 122)

        file_name += chr(ascii_num)

    suffix_num = random.randint(1, 99)

    return f"{file_name}_{str(suffix_num)}"
