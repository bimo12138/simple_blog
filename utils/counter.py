"""
@author:      13716
@date-time:   2019/10/29-13:41
@ide:         PyCharm
@name:        counter.py
"""
import json


class Count(object):

    def __init__(self):
        self.message = {}

    def save(self):
        import time
        current_time = time.localtime()
        time_stamp = "{}-{}-{}".format(current_time.tm_year, current_time.tm_mon, current_time.tm_mday)
        with open(r"logger/{}".format(time_stamp), "a") as f:
            f.write(json.dumps(self.message))
        self.message.clear()

    def add(self, key, item):
        value = self.message[key]
        if value:
            if isinstance(value, list):
                value.append(item)
            else:
                list(value).append(item)
        else:
            self.message[key] = item

    # TODO 实现存储到数据库，等待model实现
    def save_to_database(self):
        pass