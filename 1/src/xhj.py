#-*-coding:utf-8 -*-
import urllib2
import requests

class XHJ():

    def __init__(self):
        self.baseurl = 'http://www.simsimi.com/requestChat?lc=ch&ft=1.0&req='
        #self.firsturl = self.baseurl +u'您好'
        self.session = requests.Session()
        #self.cookies = requests.get(self.firsturl).cookies

    def resp(self,msg):
        msg = urllib2.quote(msg.encode('UTF-8'))
        url = self.baseurl + msg
        resp = self.session.get(url).json()
        return resp['res']



if __name__ == "__main__":
    xhj = XHJ()
    print xhj.resp(u'你大爷')