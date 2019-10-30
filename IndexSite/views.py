from django.shortcuts import render
from django.views import View
from utils.token import Token
from django.http import JsonResponse
import json
from .models import Auth


token = Token()


class IndexHandler(View):

    def get(self, request):

        return render(request, template_name="index.html")


class LoginView(View):
    # 获取登陆状态
    def get(self, request):
        token_value = request.GET.get("token")
        value = token.get_available_message(token_value)
        if value[0]:
            username = value[1]["name"]
            auth = Auth.objects.get(username=username)
            icon_path = "/static/" + str(auth.auth_icon)
            return JsonResponse(status=200, data={"status": True, "user_icon": icon_path, "username": auth.username,
                                                  "is_admin": auth.is_admin})
        else:
            return JsonResponse(status=401, data={"status": False, "message": "请重新登陆"})

    # 登陆
    def post(self, request):
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        if username and password:
            auth = Auth.objects.get(username=username)
            if auth:
                result = auth.check_password(password)
                if result:
                    available_token = token.get_token(username)
                    if isinstance(available_token, bytes):
                        available_token = available_token.decode()

                    return JsonResponse(status=200, data={"message": "登陆成功！", "token": str(available_token)})
                else:
                    return JsonResponse(status=403, data={"message": "密码错误"})
            else:
                return JsonResponse(status=403, data={"message": "当前用户不存在！"})
        else:
            return JsonResponse(status=406, data={"message": "请输入用户名或密码"})