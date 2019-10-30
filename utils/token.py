"""
@author:      13716
@date-time:   2019/10/14-22:00
@ide:         PyCharm
@name:        token.py
"""
import time
import jwt

secret = "secret"


class Token(object):

    @classmethod
    def get_token(cls, username):

        header = {
            "alg": "HS256"
        }
        payload = {
            # 没有这个域名哦!
            "iss": "bimo.com",
            "exp": int(time.time()) + 3600 * 3,
            "iat": int(time.time()),
            "name": username,
            "admin": False
        }
        return jwt.encode(payload, secret, algorithm='HS256')

    @classmethod
    def get_available_message(cls, token):
        try:
            message = jwt.decode(token, secret, issuer="bimo.com", algorithms=['HS256'])
            return [True, message]
        except jwt.exceptions.ExpiredSignatureError:
            return [False, "Token 已经过期了，请重新登陆！"]
