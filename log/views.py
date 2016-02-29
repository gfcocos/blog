from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from ipware.ip import get_ip
# from django.utils.formats import get_format
# from time import gmtime, strftime
# Create your views here.
def index(request):
    ip = get_ip(request)
    return HttpResponse(ip)
