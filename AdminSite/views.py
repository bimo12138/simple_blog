from django.shortcuts import render
from django.views import View
from django.apps import apps
from django.http import JsonResponse, HttpResponseRedirect
from utils.token import Token


miss_model = ["<class 'django.contrib.admin.models.LogEntry'>", "<class 'django.contrib.auth.models.Permission'>",
              "<class 'django.contrib.auth.models.Group'>", "<class 'django.contrib.contenttypes.models.ContentType'>",
              "<class 'django.contrib.sessions.models.Session'>", ""]

token = Token()


class IndexHandler(View):

    def get(self, request):

        token_value = request.GET.get("token")
        if token:
            value = token.get_available_message(token_value)
            if value[0]:
                return render(request, "admin_index.html")
            else:
                return JsonResponse(status=401, data={"status": False, "message": "请重新登陆"})
        else:
            return HttpResponseRedirect(redirect_to="/")
