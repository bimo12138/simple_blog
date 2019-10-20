"""
@author:      13716
@date-time:   2019/10/20-11:26
@ide:         PyCharm
@name:        get_uuid.py
"""
import uuid


class UUID(object):

    @staticmethod
    def uuid_1():
        return str(uuid.uuid1())
