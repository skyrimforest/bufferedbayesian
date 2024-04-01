import json
from SkyLogger import get_logger
import requests
import numpy as np
import time
logger = get_logger("test")

# 0,1时有极大值
def black_box_function(x,y):
    return -x ** 2 - (y - 1) ** 2 + 1

# 5,7时有极大值
def white_box_function(x,y):
    return -(x-5) ** 2 - (y - 7)**2 -3

def target_function(x,y,a,b):
    # 逐渐从black变成white
    print(f"这是计算内部:{a,b,x,y}")
    return a*black_box_function(x,y) + b*white_box_function(x,y)

idx=0
dire=1
a = [100] * 100
a += [0] * 100
b = [0] * 100
b += [100] * 100
print(a)
print(b)
def function_2b_optimized(x,y):
    global a
    global b
    global idx
    global dire
    # 0-199
    if idx>=199:
        dire=0
    idx+=dire
    return target_function(x,y,a[idx],b[idx])


if __name__ == '__main__':
    next_point = {
        "x": 2.0,
        "y": 3.0,
    }
    new_target = {
        "target": function_2b_optimized(**next_point)
    }
    while True:
        time.sleep(0.5)
        logger.info(f"next_point: {next_point},new_target: {new_target}")
        res = requests.post('http://127.0.0.1:8080/getnewconfig',
                            json={"new_config":next_point, "new_target": new_target})
        next_point=json.loads(res.text)
        new_target = {
            "target": function_2b_optimized(**next_point)
        }
