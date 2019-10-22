"""
@author:      13716
@date-time:   2019/10/13-22:51
@ide:         PyCharm
@name:        urls.py
"""
from . import views
from django.urls import path

app_name = "index"

urlpatterns = [
    path("", views.IndexHandler.as_view(), name="index"),
    path("login/", views.LoginView.as_view(), name="login")
]