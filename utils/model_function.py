"""
@author:      13716
@date-time:   2019/11/2-16:40
@ide:         PyCharm
@name:        model_function.py
"""
from django.apps import apps


class MyModelUtils(object):
    # 只用于查找用户创建的 model，django 自带的没有 # NOQ/A
    def __init__(self):
        self.installed_app = ["AdminSite", "IndexSite"]
        self.models = self.initial_model()

    def refresh(self):
        self.__init__()

    def initial_model(self):
        model_list = []
        for app in self.installed_app:
            app_label = apps.get_app_config(app)
            models = app_label.models.values()
            if models.__len__() == 0:
                continue
            for item in models:
                model_list.append(item)
        return model_list

    def get_model(self, name):
        return [(item._meta.verbose_name, item._meta.db_table) for item in self.models if item._meta.app_label == name]

    def get_items(self, name, model_name):
        for model in self.models:
            if model._meta.app_label == name and model._meta.verbose_name == model_name:
                return [(field.column, field.verbose_name) for field in model._meta.fields]

    def get_message(self, name, model_name):
        for model in self.models:
            if model._meta.app_label == name and model._meta.verbose_name == model_name:
                return model.objects.all()
