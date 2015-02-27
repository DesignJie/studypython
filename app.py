#!/usr/bin/env python
# -*- coding: utf-8 -*-
__auther = 'linjie'

from flask import Flask, render_template, url_for, request, redirect, g
import umysql 

app = Flask(__name__)

@app.route('/')
def index():
	g.url_path = request.path
	print request.url
	print request.method == 'GET'

	data = {'name':'linjie','age':'26','info':['linhui','linjie','chenqun']}
	return render_template('index.html',data=data)

# conn = MySQLdb.connect(host='localhost',user='root',passwd='',db='python')
# t = conn.cursor()
# t.execute('select * from user')
# print t.fetchall()


app.debug = True

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
