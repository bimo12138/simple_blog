from django.shortcuts import render
from django.views import View
from django.apps import apps
from django.http import JsonResponse, HttpResponseRedirect
from utils.token import Token
from IndexSite.models import Auth
import json


miss_model = ["<class 'django.contrib.admin.models.LogEntry'>", "<class 'django.contrib.auth.models.Permission'>",
              "<class 'django.contrib.auth.models.Group'>", "<class 'django.contrib.contenttypes.models.ContentType'>",
              "<class 'django.contrib.sessions.models.Session'>", ""]

token = Token()


class IndexHandler(View):

    def get(self, request):

        return render(request, "admin_index.html")


# 获取数据库的各种操作！ TODO: 权限判断
class ModelHandler(View):

    def get(self, request):
        token = request.GET.get("token")
        model_data = {}
        if token:
            models = apps.get_models()
            lists = {}
            for model in models:
                num = 0
                for name in model._meta.fields:
                    lists["属性-{}".format(str(num))] = name.verbose_name
                    num += 1
                model_data["{}".format(str(model._meta.verbose_name))] = lists
            return JsonResponse(status=200, data={"model_data": model_data})
        else:
            return JsonResponse(status=401, data={"status": False, "message": "token 已过期，请重新登陆"})