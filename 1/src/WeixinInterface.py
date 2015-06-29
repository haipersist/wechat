#-*-coding:utf8 -*-
from flask import Flask,request,make_response,render_template
import hashlib
from lxml import etree
import xml.etree.ElementTree as ET
import time
from Wechat import Wechat
import pylibmc as memcache
from  xhj import XHJ
from music import Music,MusicDict

app = Flask(__name__)



@app.route('/')
def hello():
	return render_template('hello.html')


@app.route( '/weixin', methods=['GET','POST'])
def wechat_auth():
    chat = Wechat()
    if request.method == 'GET':
        query = request.args
        signature = query.get('signature')
        timestamp = query.get('timestamp')
        nonce = query.get('nonce')
        echostr = query.get('echostr')
        return chat.auth(timestamp,nonce,signature,echostr)

    mc =  memcache.Client()
    chat.parse_data(request.data)
    if chat.msgtype == 'text':
        content = chat.msg.content
        if content == u'音乐':
            mc.set(chat.msg.user+'_music','music')
            reply = u'开始收听，列表：1.云中的Angle；2.until you；3.终于等到你。请输入序号。若停止收听，请输入停止，可切换到与机器对话'
            return chat.resp_text(reply)
        elif content == u'停止':
             mc.delete(chat.msg.user+'_music')
             reply = u'欢迎下次收听'
             return chat.resp_text(reply)
        elif content == u'帮助':
            reply = u'若想收听音乐，请输入音乐,想停止，即输入停止'
            return chat.resp_text(reply)
        else:
            pass

    music = mc.get(chat.msg.user+'_music')
    if music == 'music':
        song = MusicDict[content]
        title, desc, musicurl, hqurl = song['title'],song['desc'],song['url'],song['url']
        return chat.resp_music(title, desc, musicurl, hqurl)
    else:
        reply = XHJ().resp(content)
        return chat.resp_text(reply)



@app.route('/job')
def Job():
    pass




if __name__ == "__main__":
    chat = Wechat()
    xml = """
    <xml>
    <ToUserName><![CDATA[wechat]]></ToUserName>
    <FromUserName><![CDATA[pycharm]]></FromUserName>
    <CreateTime>13</CreateTime>
    <MsgType><![CDATA[text]]></MsgType>
    <Content><![CDATA[rhh]]></Content>
    </xml>
    """
    Music = {'1':{'title':u'云中的Angle','desc':u'爱你',
              'url':'http://hbnn-hbnnstore.stor.sinaapp.com/%E5%BC%A0%E6%9D%B0%20-%20%E4%BA%91%E4%B8%AD%E7%9A%84Angel.mp3'},
         '2':{'title':'until you','desc':u'爱你,老婆',
              'url':'http://hbnn-hbnnstore.stor.sinaapp.com/Shayne%20Ward-Until%20You.wma'},
         '3':{'title':u'终于等到你','desc':u'永远在一起',
              'url':'http://hbnn-hbnnstore.stor.sinaapp.com/%E5%BC%A0%E9%9D%93%E9%A2%96-%E7%BB%88%E4%BA%8E%E7%AD%89%E5%88%B0%E4%BD%A0(%E7%94%B5%E8%A7%86%E5%89%A7%E3%80%8A%E5%92%B1%E4%BB%AC%E7%BB%93%E5%A9%9A%E5%90%A7%E3%80%8B%E4%B8%BB%E9%A2%98%E6%9B%B2).wma'
         }}

    chat.parse_data(xml)
    song = Music['1']
    title, desc, musicurl, hqurl = song['title'],song['desc'],song['url'],song['url']
    print chat.resp_music(title, desc, musicurl, hqurl)

