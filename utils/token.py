"""
@author:      13716
@date-time:   2019/10/14-22:00
@ide:         PyCharm
@name:        token.py
"""
import time
import jwt
import base64
secret = "gvfsdhgdsgdfsfgfrghfgsgdfa"


class Token(object):

    @classmethod
    def get_token(cls, username):

        header = {
            "alg": "HS256"
        }
        payload = {
            # 没有这个域名哦!
            "iss": "bimo.com",
            "exp": int(time.time()),
            "name": username,
            "admin": False
        }
        return jwt.encode(payload=payload, key="secret", alg="HS256", al=header)
