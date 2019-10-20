from django.db import models
from utils.get_uuid import UUID
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


uuid = UUID()


class AuthManger(BaseUserManager):

    def base_function(self, username, password, email):
        if not username or not password or not email:
            raise ValueError("请把数据输入完整！")
        user = self.model(username=username, email=email)
        user.set_password(password)
        return user

    def create_user(self, username, password, email):
        user = self.base_function(username=username, password=password, email=email)
        user.is_admin = False
        user.save()

    def create_super_user(self, username, password, email):
        user = self.base_function(username=username, password=password, email=email)
        user.is_admin = True
        user.save()


class Auth(AbstractBaseUser):

    identify = models.CharField(primary_key=True, verbose_name="身份ID", max_length=40, default=uuid.uuid_1())
    username = models.CharField(max_length=20, verbose_name="姓名")
    password = models.CharField(max_length=20, verbose_name="密码")
    register_time = models.DateField(verbose_name="注册时间", auto_now_add=True)
    last_login = models.DateField(verbose_name="最后一次登陆时间", auto_now=True)
    email = models.EmailField(verbose_name="登陆邮箱", unique=True)
    auth_icon = models.ImageField(verbose_name="用户头像", upload_to="img/", default="img/user.png")
    is_active = models.BooleanField(verbose_name="激活状态", default=False)
    is_admin = models.BooleanField(verbose_name="是否是管理员用户")
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "email"]
    EMAIL_FIELD = "email"

    objects = AuthManger()

    def get_full_name(self):
        return {
            "id": self.identify,
            "email": self.email
        }

    def get_short_name(self):
        return {
            "email": self.email
        }

    def __str__(self):
        return self.email
