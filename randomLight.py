import paho.mqtt.client as mqtt
import random
import json
import datetime
import time

# 設置日期時間的格式
ISOTIMEFORMAT = "%m/%d %H:%M:%S"

# 連線設定
# 初始化地端程式
client = mqtt.Client()

# 設定登入帳號密碼
client.username_pw_set("smms", "2ojujiru")

# 設定連線資訊(IP, Port, 連線時間)
client.connect("192.168.50.11", 1883, 60)
times = 0
payloads = [
    {"DO_1-0": True, "DO_1-1": True, "DO_1-2": True},
    {"DO_1-0": True, "DO_1-1": True, "DO_1-2": False},
    {"DO_1-0": True, "DO_1-1": False, "DO_1-2": True},
    {"DO_1-0": False, "DO_1-1": True, "DO_1-2": True},
    {"DO_1-0": True, "DO_1-1": False, "DO_1-2": False},
    {"DO_1-0": False, "DO_1-1": True, "DO_1-2": False},
    {"DO_1-0": False, "DO_1-1": False, "DO_1-2": True},
]
while True:
    for i in payloads:
        times += 1
        payload = i
        print(json.dumps(payload), f"{times=}")
        # 要發布的主題和內容
        client.publish("SMMS/SET", json.dumps(payload))
        # time.sleep(0.1)
