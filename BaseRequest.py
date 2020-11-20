# -*- coding: utf-8 -*-#

# Name:         
# Description:
# Author:       gongzhao
# Date:         2020/9/28
import json

import requests


# 请求参数就是一般形式
def normal_request(url, params):
    print("*******请求数据*****")
    for param in params:
        print(param + " : " + str(params[param]))
    print("*******************")
    response = requests.get(url, params=params)
    content = response.content
    return json.loads(content)


# 请求参数是json形式
def json_request(url, json_param):
    print("*******json请求数据*****")
    for param in json_param:
        print(param + " : " + str(json_param[param]))
    print("***********************")
    response = requests.get(url, json=json_param)
    content = response.content
    print(type(content))
    return json.loads(content)


def user_test_url():
    return "http://user.133ec.com"


def user_prod_url():
    return "http://120.133.0.149:8021"


if __name__ == '__main__':
    data = {
        "system": "widefield",
        "phone": "15872368251"
    }
    result = normal_request(user_test_url() + "/user/baseinfo/queryByPhoneidOrPhone", data)
    print(result)
    print(result['data'])
    print(result['data']['user'])
    print(result['data']['user']['phoneUserId'])
