from django.shortcuts import render
from django.views import View
from utils.token import Token
from django.http import JsonResponse


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
            print(value[1])
            return JsonResponse(status=200, data={"status": True})
        else:
            return JsonResponse(status=401, data={"status": False, "message": "请重新登陆"})
