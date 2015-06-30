#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'WHB'


from response import TextReply,WechatReply,MusicReply,ArticleReply
from message import TextMsg,MSG_TYPES,WechatMsg,ImageMsg,LinkMsg,VideoMsg,VoiceMsg,MusicMsg
from utils import parse_xml
import hashlib
import time
from flask import make_response

class Wechat():

    def __init__(self):
        self.token = 'hbnnforever'

    def auth(self,timestamp, nonce, signature,echostr):
        s = [timestamp, nonce, self.token]
        s.sort()
        s = ''.join(s)
        return make_response(echostr) \
                if ( hashlib.sha1(s).hexdigest() == signature ) \
                else 'auth fail,plese retry'

    def parse_data(self,metadata):
        data = parse_xml(metadata)
        self.msgtype = data.get('MsgType').lower()
        self.msg = MSG_TYPES.get(self.msgtype)(data)

    def resp_text(self,content):
        return TextReply(self.msg,content=content).render()

    def resp_voice(self,id):
        pass

    def resp_image(self,mediaid):
        pass

    def resp_music(self, title, desc, musicurl, hqurl):
       return MusicReply(self.msg,title=title,desc=desc,musicurl=musicurl,hqurl=hqurl).render()

    def response_video(self, media_id, title=None, description=None):
        pass

    def resp_article(self,articles):
        return ArticleReply(self.msg,articles).render()




if __name__ == "__main__":
    chat = Wechat()
    xml = """
    <xml>
    <ToUserName><![CDATA[wechat]]></ToUserName>
    <FromUserName><![CDATA[pycharm]]></FromUserName>
    <CreateTime>dd</CreateTime>
    <MsgType><![CDATA[text]]></MsgType>
    <Content><![CDATA[sss]]></Content>
    </xml>
    """
    title = 'dds'
    desc = 'dff'
    musicurl = 'f'
    hqurl = 'fg'
    chat.parse_data(xml)
    articles = [{'title':u'爱你','desc':u'记忆','picurl':'http://hbnn-hbnnstore.stor.sinaapp.com/boat.jpg',
                 'url':'http://finance.ifeng.com/a/20150630/13807969_0.shtml'},
                {'title':u'爱你','desc':u'记忆','picurl':'http://hbnn-hbnnstore.stor.sinaapp.com/europ.jpg',
                 'url':'http://finance.ifeng.com/a/20150630/13808481_0.shtml'}]
    print chat.resp_article(articles)
