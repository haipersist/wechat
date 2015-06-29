#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'WHB'

from flask import make_response
from message import WechatMsg
import time

class WechatReply(object):

    """
    :parameter:msg,Wechatmsg
    """
    def __init__(self,metaMsg,**kwargs):
        if 'toUser' not in kwargs :
            kwargs['toUser'] = metaMsg.user
        if 'fromUser' not in kwargs :
            kwargs['fromUser'] = metaMsg.server
        if 'msgtype' not in kwargs :
            kwargs['msgtype'] = metaMsg.msgtype

        kwargs['time'] = int(time.time())
        self.reply = {}
        self.reply.update(kwargs)

    def render(self):
        pass

class TextReply(WechatReply):
    """
    TExtXml
    """
    reply_xml = """
    <xml>
    <ToUserName><![CDATA[%s]]></ToUserName>
    <FromUserName><![CDATA[%s]]></FromUserName>
    <CreateTime>%s</CreateTime>
    <MsgType><![CDATA[text]]></MsgType>
    <Content><![CDATA[%s]]></Content>
    <FuncFlag>0</FuncFlag>
    </xml>
    """

    def __init__(self,metaMsg,content):
        super(TextReply,self).__init__(metaMsg,content=content)

    def render(self):
        #must keep the right order
        para = (self.reply['toUser'],self.reply['fromUser'],
                self.reply['time'],self.reply['content'])
        response = make_response(self.reply_xml % para)
        #response =self.reply_xml % para
        return response


class MusicReply(WechatReply):
    """
    Music Template
    """
    reply_xml = """<xml><ToUserName><![CDATA[%s]]></ToUserName>
     <FromUserName><![CDATA[%s]]></FromUserName>
     <CreateTime>%s</CreateTime>
     <MsgType><![CDATA[music]]></MsgType>
     <Music>
     <Title><![CDATA[%s]]></Title>
     <Description><![CDATA[%s]]></Description>
     <MusicUrl><![CDATA[%s]]></MusicUrl>
     <HQMusicUrl><![CDATA[%s]]></HQMusicUrl>
     </Music>
     <FuncFlag>0</FuncFlag></xml>"""

    def __init__(self,metaMsg,title,desc,musicurl,hqurl):
        super(MusicReply,self).__init__(metaMsg,title=title,desc=desc,musicurl=musicurl,hqurl=hqurl)

    def render(self):
        print self.reply
        #must keep the right order
        para = (self.reply['toUser'],self.reply['fromUser'],
                self.reply['time'],self.reply['title'],self.reply['desc'],self.reply['musicurl'],self.reply['hqurl'])
        #response = make_response(self.reply_xml % para)
        response =self.reply_xml % para
        return response



if __name__ == "__main__":
    pass