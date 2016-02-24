from django.shortcuts import render
from django.http import HttpResponse
from django.core.signing import Signer
from .models import SSAcount
import base64
from time import gmtime, strftime
# Create your views here.
def index(request):
    return HttpResponse("Hello World, Django")


def detail(request, my_args):
    return HttpResponse("You're looking at my_args %s." % my_args)


def acounts(request):
    acounts = SSAcount.objects.order_by('ping')
    if len(acounts) > 0:
        acount = acounts[0]
        if acount.server_aes == '':
            aes = base64.encodestring(acount.server).replace('\n','');
            aes = aes.replace(' ','')
            acount.server_aes = aes
            acount.save()
        t = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        output = ('{ "local_port": %s, "method": "%s", "password": "%s", "server": "%s", "server_aes": "%s", "server_port": "%s" , "time": "%s"}' % (1080, acount.method, acount.password, acount.server, acount.server_aes, acount.server_port,t))
        return HttpResponse(output)
    else:
        return HttpResponse('Error,No Data')
    # acount = acounts.
