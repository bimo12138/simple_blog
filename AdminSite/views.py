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
        login_status = token.get_available_message(request.COOKIES.get("token"))
        model_data = {}
        if login_status:
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


class ModelProcessHandler(View):

    def get(self, request, model_name):
        login_status = token.get_available_message(request.COOKIES.get("token"))
        if login_status:
            models = apps.get_models()
            for model in models:
                columns = {}
                if model._meta.verbose_name == model_name:
                    num = 0
                    for column in model._meta.fields:
                        columns[num] = column.verbose_name
                        num += 1
                    result = model.objects.all()

                    if result.exists():
                        database = []
                        for i in result:
                            di = i.__getstate__()
                            database.append(di)

                        print(type(columns), type(database))
                        return JsonResponse(status=200, data={"columns": columns, "result": database})
                    else:
                        return JsonResponse(status=404, data={"columns": columns, "result": False})
        return JsonResponse(status=401, data={"status": False, "message": "token 已过期，请重新登陆"})