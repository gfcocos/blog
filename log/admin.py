from django.contrib import admin
from .models import Log

# Register your models here.
class LogAdmin(admin.ModelAdmin):
    """docstring for LogAdmin"""
    list_display = ('time_seconds', 'clinetip', 'retserver')

    def time_seconds(self, obj):
        return obj.time.strftime('%y-%m-%d %H:%M:%S')

    def __str__(self):              # __unicode__ on Python 2
        if self.time:
            t = self.time.strftime('%m-%d-%y %H:%M:%S')
        else:
            t = 'None'

admin.site.register(Log, LogAdmin)
