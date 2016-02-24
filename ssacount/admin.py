from django.contrib import admin
# Register your models here.
from .models import SSAcount


class SSAcountAdmin(admin.ModelAdmin):
    """docstring for SSAcountAdmin"""
    # action display
    # fields = ['server', 'server_port', 'method', 'password']

    # list dispaly
    list_display = ('server', 'server_aes', 'server_port', 'method', 'password', 'ping')

# admin.site.register(SSAcount, SSAcountAdmin)
admin.site.register(SSAcount, SSAcountAdmin)
