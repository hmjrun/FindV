from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseBadRequest
from wechat.wechat_utils import wx_utilsCheckSignature
import logging
logger = logging.getLogger("django")


def wx_checkSignature(request):
    logger.info("Begin Wechat Check Signature...")
    signature = request.GET.get('signature')
    timestamp = request.GET.get('timestamp')
    nonce = request.GET.get('nonce')
    if wx_utilsCheckSignature(signature=signature, timestamp=timestamp, nonce=nonce):
        return HttpResponse(request.GET['echostr'])
    else:
        return HttpResponseBadRequest()