
from django.contrib import admin
from register.models import *

class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User,UserAdmin)



# Register your models here.
