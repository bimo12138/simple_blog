from django.db import models
from utils.get_uuid import UUID
uuid = UUID()

#
# class UserLogging(models.Model):
#     identify = models.CharField(primary_key=True, verbose_name="记录的用户ID", max_length=40, default=uuid.uuid_1())
#
