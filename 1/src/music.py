#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'WHB'
import urllib2
#import requests
import xml.etree.ElementTree as ET
from cStringIO import StringIO


class Music():

    def __init__(self,content):
        self.title,self.artist = content.split(' ')[0],content.split(' ')[1]
        self.baseurl = u'http://box.zhangmen.baidu.com/x?op=12&count=1&title=%s$$%s$$$$'%\
                       (self.title,self.artist)

    def get_url(self):
        """
        :return:musicurl,hqurl in dict type
        """
        resp = requests.get(self.baseurl).content
        resp = resp.decode('gb2312').encode('utf-8')
        resp = resp.replace('gb2312', 'utf-8')
        root = ET.parse(StringIO(resp))
        url = root.find('url')
        for child in url:
            if child.tag == 'encode':
                url1 = child.text
            if child.tag == 'decode':
                url2 = child.text
        musicurl = '/'.join([url1,url2])
        hqurl = root.find('durl')
        for child in hqurl:
            if child.tag == 'encode':
                hqurl1 = child.text
            if child.tag == 'decode':
                hqurl2 = child.text
        hqurl = '/'.join([hqurl1,hqurl2])
        return {'musicurl':musicurl,'hqurl':hqurl}

MusicDict = {'1':{'title':u'云中的Angle','desc':u'爱你',
              'url':'http://hbnn-hbnnstore.stor.sinaapp.com/%E5%BC%A0%E6%9D%B0%20-%20%E4%BA%91%E4%B8%AD%E7%9A%84Angel.mp3'},
         '2':{'title':'until you','desc':u'爱你,老婆',
              'url':'http://hbnn-hbnnstore.stor.sinaapp.com/Shayne%20Ward-Until%20You.wma'},
         '3':{'title':u'终于等到你','desc':u'永远在一起',
              'url':'http://hbnn-hbnnstore.stor.sinaapp.com/%E5%BC%A0%E9%9D%93%E9%A2%96-%E7%BB%88%E4%BA%8E%E7%AD%89%E5%88%B0%E4%BD%A0(%E7%94%B5%E8%A7%86%E5%89%A7%E3%80%8A%E5%92%B1%E4%BB%AC%E7%BB%93%E5%A9%9A%E5%90%A7%E3%80%8B%E4%B8%BB%E9%A2%98%E6%9B%B2).wma'
         }}



if __name__ == "__main__":
   s = Music(u'逆战 张杰').get_url()
   print s['musicurl']
   print s['hqurl']
