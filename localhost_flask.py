from flask import Flask, render_template
from flask import request, redirect
from flask import jsonify
import requests
from bs4 import BeautifulSoup
import urllib2, urllib, json, urlfetch
import cookielib
from getpass import getpass
import sys
import os
from stat import *

app = Flask(__name__)

value1=0
value2=0
value3=0
row=5
flag=0

@app.route('/')
def hello_world():
    return render_template('test.html')


@app.route('/test')
def get_values_from_spreadsheet():
    global value1
    global value2
    global value3
    global row
    global flag
    sheets_id='1gSW_8V4q0FZTnQr_Di5yqy6LNgXgbA7IvoyL8VYgZzU'
    r=requests.get('https://sheets.googleapis.com/v4/spreadsheets/%s/values/A%d:C%d?key=AIzaSyCcnQDCQGsTp4dofDS3fjbgGWM3mhBQw_c'%(sheets_id,row,row))
    response=r.json()
    response1=str(response)
    r=len(str(row))
    response1=response1[28+2*r:34+2*r]

    if response1=='values':
        values=response['values']
        values1=values[0]
        if len(values1)==3:
            if values1[0]!='' and values1[1]!='' and values1[2]!='':
                value1=int(values1[0])                       #here datatypes needed are of int, so typecasting to int
                value2=int(values1[1])
                value3=int(values1[2])
                flag=1
                row=row+1
                string='value1 is %d value2 is %d value3 is %d flag is %d' %(int(value1),int(value2),int(value3),int(flag))
                return jsonify(
                value1=value1,
                value2=value2,
                value3=value3,
                flag=flag
            )

    flag=0
    return jsonify(flag=flag)

@app.route('/values/', methods=['POST', 'GET'])
def hello():
    global value1
    global value2
    global value3
    if request.method=='POST':
        value1=request.form['value1']
        value2=request.form['value2']
        value3=request.form['value3']
        return 'success!'
    else:
        return 'value1 is %d value2 is %d value3 is %d' %(int(value1),int(value2),int(value3))

@app.route('/js/', methods=['POST', 'GET'])
def bolo():
    if request.method=='POST':
        value1=request.form['uname']
        value2=request.form['psw']
        #return redirect("http://www.google.com", code=302)
        #return 'value1 is %s value2 is %s' %(value1,value2)
        return render_template('test.html')
    else:
        return 'Fail'



@app.route('/message/', methods=['POST'])
#@app.route('/message/')

#message = raw_input("Enter text: ")
#number = raw_input("Enter number: ")
def message():

    username = "enter username"
    passwd = "enter password"
    number="7382923814"
    message=request.form['message']

    message = "+".join(message.split(' '))

    #logging into the sms site
    url ='http://site24.way2sms.com/Login1.action?'
    data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'

    #For cookies

    cj= cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

    #Adding header details
    opener.addheaders=[('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120')]
    try:
        usock =opener.open(url, data)
    except IOError:
        return jsonify(
        message='error'
    )
        #return()

    jession_id =str(cj).split('~')[1].split(' ')[0]
    send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
    send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen=136'
    opener.addheaders=[('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
    try:
        sms_sent_page = opener.open(send_sms_url,send_sms_data)
    except IOError:
        return jsonify(
        message='error'
    )
        #return()

    return jsonify(
    message='Success'
)
    #return ()


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=2000,
        debug=True
    )
