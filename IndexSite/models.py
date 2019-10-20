from django.db import models
from utils.get_uuid import UUID
from django.contrib.auth.models import AbstractBaseUser


uuid = UUID()


class Auth(AbstractBaseUser):

    identify = models.CharField(primary_key=True, verbose_name="身份ID", max_length=40, default=uuid.uuid_1())
    username = models.CharField(max_length=20, verbose_name="姓名")
    password = models.CharField(max_length=20, verbose_name="密码")
    register_time = models.DateField(verbose_name="注册时间", auto_now_add=True)
    last_login = models.DateField(verbose_name="最后一次登陆时间", auto_now=True)
    email = models.EmailField(verbose_name="登陆邮箱", unique=True)

    USERNAME_FIELD = "email"
    def get_full_name(self):
        return {
            "id": self.identify,
            "email": self.email
        }

    def get_short_name(self):
        return {
            "email": self.email
        }
