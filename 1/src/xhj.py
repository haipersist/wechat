#-*-coding:utf-8 -*-
import urllib2
import requests

class XHJ():

    def __init__(self):
        self.baseurl = 'http://www.simsimi.com/requestChat?lc=ch&ft=1.0&req='
        self.firsturl = self.baseurl +u'您好'
        self.cookies = requests.get(self.firsturl).cookies

    def resp(self,msg):
        msg = urllib2.quote(msg.encode('UTF-8'))
        url = self.baseurl + msg
        resp = requests.get(url,cookies=self.cookies).json()
        return resp['res']



