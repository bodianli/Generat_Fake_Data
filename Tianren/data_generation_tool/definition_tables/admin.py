from django.contrib import admin
from .models import TableConfig
from .models import ColumnConfig


# Register your models here.
class ColumnConfigAdmin(admin.ModelAdmin):
    list_display = ('name', 'table_config')


admin.site.register(TableConfig)
admin.site.register(ColumnConfig, ColumnConfigAdmin)
