"""
@author:      13716
@date-time:   2019/10/13-22:51
@ide:         PyCharm
@name:        urls.py
"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexHandler.as_view(), name="index"),
    path("model/", views.ModelHandler.as_view(), name="model"),
    path("model/<str:model_name>/", views.ModelProcessHandler.as_view(), name="model_process")
]