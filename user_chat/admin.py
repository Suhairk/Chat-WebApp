from django.contrib import admin
from .models import Group, Message,privateMessage
# Register your models here.
admin.site.register(Group)
admin.site.register(Message)
admin.site.register(privateMessage)
