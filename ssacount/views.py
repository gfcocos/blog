# from django.shortcuts import render
from django.http import HttpResponse
# from django.core.signing import Signer

from .models import SSAcount
from log.models import Log

import base64
from datetime import datetime
# from django.utils.dateformat import DateFormat
from ipware.ip import get_ip
# from django.utils.formats import get_format
# from time import gmtime, strftime
# Create your views here.
def index(request):
    ip = get_ip(request)
    return HttpResponse(ip)


def detail(request, my_args):
    return HttpResponse("You're looking at my_args %s." % my_args)


def acounts(request):
    ip = get_ip(request)
    acounts = SSAcount.objects.order_by('ping')
    if len(acounts) > 0:
        acount = acounts[0]
        if acount.server_aes == '':
            aes = base64.encodestring(acount.server)
            aes = aes.replace('\n', '').replace(' ', '')
            acount.server_aes = aes
            acount.save()
        t = datetime.now().strftime('%m-%d-%y %H:%M:%S')
        output = ('{ "local_port": %s, "method": "%s", "password": "%s", "server": "%s", "server_aes": "%s", "server_port": "%s" , "time": "%s"}' % (1080, acount.method, acount.password, acount.server, acount.server_aes, acount.server_port,t))

        #log it
        l = Log(retserver=acount.server, clinetip=ip, time=datetime.now())
        l.save()
        return HttpResponse(output)
    else:
        return HttpResponse('Error,No Data')
    # acount = acounts.
