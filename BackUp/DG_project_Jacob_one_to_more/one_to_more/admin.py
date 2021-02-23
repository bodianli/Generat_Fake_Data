from django.contrib import admin
from .models import Account_more
from .models import User_more

# Register your models here.

admin.site.register(User_more)
admin.site.register(Account_more)