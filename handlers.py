# -*- coding:utf-8 -*-
__author__ = 'Mouse'

from settings import connconf
import tornado.web
import utils


# 网站主页
class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        print('hello,IP: ',self.request.remote_ip)
        articles=utils.listarticles()
        self.render('index.html',articles=articles)

#后台管理界面
class ManageHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        print('hello,IP: ',self.request.remote_ip)
        self.render('manage.html')

class PostarticleHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        article_title=self.get_argument('article_title')
        article_content=self.get_argument('article_content')
        print(article_content,article_title)
        utils.addarticle(article_title,article_content)
        #self.redirect（'index.html'）
        self.write('''{"resultcode":"success"}''')