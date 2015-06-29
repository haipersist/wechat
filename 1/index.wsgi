#-*-coding:utf-8 -*-
import os
import sys


#install third module
root = os.path.dirname(__file__)
sys.path.insert(0,os.path.join(root,'site-packages'))
from src.WeixinInterface import app
import pylibmc
import sae

sys.modules['memcache'] = pylibmc

 
application = sae.create_wsgi_app(app)

