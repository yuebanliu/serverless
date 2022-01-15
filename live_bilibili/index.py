# -*- coding: utf8 -*-
import json
import time
import requests
from random import randint


# server酱 自己去申请，推送用
sc_url = 'https://sctapi.ftqq.com/'
sckey = '' # 自己注册

def main_handler(event, context):

    time.sleep(randint(0, 10))

    sessdata = "" # 需要自己去获取之后填上

    userinfo = json.loads(requests.get("https://api.bilibili.com/x/web-interface/nav", cookies={"SESSDATA":sessdata}).text)
    if userinfo["data"]["isLogin"] == False:
        msg = '登录失败'
    else:
        print("用户名: " + userinfo["data"]["uname"])
        print("UID: " + str(userinfo["data"]["mid"]))
        #https://api.live.bilibili.com/xlive/web-ucenter/v1/sign/DoSign
        sign = requests.get("https://api.live.bilibili.com/sign/doSign", cookies={"SESSDATA":sessdata})
        sign_info = json.loads(sign.text)
        if sign_info["code"] == 0:
            msg = "签到成功:" + sign_info["data"]["text"] + "\n" +sign_info["data"]["specialText"]
        else:
            msg = "签到失败:"+sign_info["message"]

    print(msg)
    requests.get( sc_url + sckey + '.send?title=B站直播签到通知: '+msg)
    return("Finish")

