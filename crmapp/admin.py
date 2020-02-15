from django.contrib import admin
from .models import Company, Project, Manager, Message, Keyword
# Register your models here.

admin.site.register(Company)
admin.site.register(Project)
admin.site.register(Manager)
admin.site.register(Message)
admin.site.register(Keyword)