import hashlib
import time
import logging
logger = logging.getLogger("django")
from .wechat_config import WX_TOKEN

def wx_utilsMakeSha1(params):
    """Generate sha1 hash value with params sorted by dictionary order,
    the params param is a list"""
    param_list = []
    param_list.extend(params)
    param_list.sort()
    #print("MakeSha1 - params: %s" % param_list)
    tmpstr = ''
    for i in range(len(param_list)):
        tmpstr += param_list[i]
    
    h = hashlib.sha1(tmpstr.encode('utf8'))
    h_value = '%s' % (h.hexdigest(),)
    return h_value

def wx_utilsCheckSignature(signature, timestamp, nonce):
    token = WX_TOKEN
    params_list = []
    params_list.append(timestamp)
    params_list.append(nonce)
    params_list.append(token)
    
    h_value = wx_utilsMakeSha1(params_list)
    logger.info("Signature Received: {}".format(signature))
    logger.info("Signature Expected: {}".format(h_value))
    if signature == h_value:
        return True
    else:
        return False

# def wx_getTimestamp():
#     return int(time.time())

def check_signature(signature, timestamp, nonce):
    token = WX_TOKEN
    L = [timestamp, nonce, token]
    logger.info("Before sort String_list: {}".format(L))
    L.sort()
    s = L[0] + L[1] + L[2]
    logger.info("After sort String_list: {}".format(s))
    h_value = hashlib.sha1(s.encode('utf8')).hexdigest()
    logger.info("Signature Received: {}".format(signature))
    logger.info("Signature Expected: {}".format(h_value))
    return h_value == signature