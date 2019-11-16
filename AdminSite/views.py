from django.shortcuts import render
from django.views import View
from django.apps import apps
from django.http import JsonResponse, HttpResponseRedirect
from utils.token import Token
from IndexSite.models import Auth
import json
from utils.model_function import MyModelUtils


token = Token()


class IndexHandler(View):

    def get(self, request):

        return render(request, "admin_index.html")


# 获取数据库的各种操作！ TODO: 权限判断
class ModelHandler(View):

    def get(self, request):
        login_status = token.get_available_message(request.COOKIES.get("token"))

        if login_status:
            model_app = MyModelUtils()
            model_banner = model_app.get_banner()
            return JsonResponse(status=200, data={"model_banner": model_banner})
        else:
            return JsonResponse(status=401, data={"status": False, "message": "token 已过期，请重新登陆"})


class ModelProcessHandler(View):

    def get(self, request, model_name):
        login_status = token.get_available_message(request.COOKIES.get("token"))
        if login_status:
            pass
            # model_app = MyModelUtils()
            # columns = MyModelUtils.get
            # return JsonResponse(status=200, data={"columns": columns, "result": database})
            # else:
            #     return JsonResponse(status=404, data={"columns": columns, "result": False})
        return JsonResponse(status=401, data={"status": False, "message": "token 已过期，请重新登陆"})