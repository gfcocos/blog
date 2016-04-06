# coding=utf-8

import hashlib
# import json
# from lxml import etree
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseBadRequest
# from django.shortcuts import render
from lxml import etree
# import the logging library
import logging
from auto_reply.views import auto_reply_main
import urllib,urllib2,json
# Create your views here.
WEIXIN_TOKEN = 'happyyi'

# Get an instance of a logger
logger = logging.getLogger('django.request')

# 微信SDK

from wechat_sdk import WechatBasic
from wechat_sdk.exceptions import ParseError
from wechat_sdk.messages import TextMessage, VoiceMessage, ImageMessage, VideoMessage, LinkMessage, LocationMessage, EventMessage

wechat_instance = WechatBasic(
    token='happyyi',
    appid='wxfe58b4a595b9206c',
    appsecret='5c425fed5ce41614472ca1263089e4e8'
)

@csrf_exempt
def index(request):
    """所有的消息都会先进入这个函数进行处理，函数包含两个功能，如果请求时get，说明是微信接入验证，如果是post就是微信正常的收发消息。"""

    if request.method == "GET":
        signature = request.GET.get("signature", None)
        timestamp = request.GET.get("timestamp", None)
        nonce = request.GET.get("nonce", None)
        echostr = request.GET.get("echostr", None)
        if not wechat_instance.check_signature(signature=signature, timestamp=timestamp, nonce=nonce):
            return HttpResponseBadRequest('Verify Failed')
        return HttpResponse(echostr)
    else:
        # 解析本次请求的 XML 数据
        try:
            wechat_instance.parse_data(data=request.body.decode('utf-8'))
        except ParseError:
            return HttpResponseBadRequest('Invalid XML Data')
        message = wechat_instance.get_message()

        if isinstance(message, TextMessage):
            content = message.content.strip()
            logger.debug(content)
            if '你的名字'.decode('utf-8') in content or '你叫什么'.decode('utf-8') in content:
                reply_text = (
                    '我就是你心里想的那个人(凉面君)'
                )
                response_xml = wechat_instance.response_text(reply_text)
            elif 'wiki' in content:
                import wikipedia
                wiki_content = content.replace("wiki:", "")
                wiki = wikipedia.page(wiki_content)
                message = [{
                    'title': wiki.title,
                    'picurl': 'https://www.phodal.com/static/phodal/images/bg.jpg',
                    'description': 'what the fuck',
                    'url': 'www.baidu.com'
                }]
                logger.debug(message)
                response_xml = wechat_instance.response_news(message)
            else:
                reply_text = RobotService.auto_reply(content)
                response_xml = wechat_instance.response_text(reply_text)
            return HttpResponse(response_xml)
        # xml_str = smart_str(request.body)
        # logger.debug(xml_str)
        # request_xml = etree.fromstring(xml_str)
        # response_xml = auto_reply_main(request_xml)
        # return HttpResponse(response_xml)
class RobotService(object):
    """Auto reply robot service"""
    KEY = 'd92d20bc1d8bb3cff585bf746603b2a9'
    url = 'http://www.tuling123.com/openapi/api'
    @staticmethod
    def auto_reply(req_info):
        query = {'key': RobotService.KEY, 'info': req_info.encode('utf-8')}
        headers = {'Content-type': 'text/html', 'charset': 'utf-8'}
        data = urllib.urlencode(query)
        req = urllib2.Request(RobotService.url, data)
        f = urllib2.urlopen(req).read()
        return json.loads(f).get('text').replace('<br>', '\n')
        #return json.loads(f).get('text')
