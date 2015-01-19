# -*- coding:utf-8 -*-
__author__ = 'Mouse'
import mysql.connector
import markdown2
from settings import connconf

#将html转化为markdown格式
def html2markdown(content):
    conv_content=markdown2.markdown(content)
    return conv_content

#添加文章到数据库
def addarticle(title,content):
    cnx = mysql.connector.connect(user=connconf[0], password=connconf[1], host=connconf[2],database=connconf[3], charset='utf8')
    cursor = cnx.cursor()
    content=html2markdown(content)
    x="insert into articles (title,content) values('%s','%s')" % (title,content)
    cursor.execute(x)
    cnx.commit()
    cnx.close()

#select文章列表
def listarticles():
    cnx = mysql.connector.connect(user=connconf[0], password=connconf[1], host=connconf[2],database=connconf[3], charset='utf8')
    cursor = cnx.cursor()
    x="select title,content,p_time from articles"
    cursor.execute(x)
    articles=cursor.fetchall()
    cnx.close()
    return articles