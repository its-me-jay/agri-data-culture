#author - The Great Jayasimha!

import requests
import urllib2, urllib, json, urlfetch
from pprint import pprint
from bs4 import BeautifulSoup

access_token='ya29.Glv9A7hrhIUxQ5f9k0tovnr5LEFm_p6Reb9ZGAXsGw_ABcyX0pYKwlgvLxNJ77HxokhkvDhbdT_gi0kQaYtxE-6jm3TIEeMzpV8Iq04hP42cNW5ddcEryDGuO2Wp'

def get_values_from_spreadsheet(row):
    row=row
    r=requests.get('https://sheets.googleapis.com/v4/spreadsheets/1gSW_8V4q0FZTnQr_Di5yqy6LNgXgbA7IvoyL8VYgZzU/values/A%d:C%d?key=AIzaSyCcnQDCQGsTp4dofDS3fjbgGWM3mhBQw_c'%(row,row))
    response=r.json()
    print(response)
    response1=str(response)
    r=len(str(row))
    response1=response1[28+2*r:34+2*r]
    
    if response1=='values':
        values=response['values']
        values1=values[0]
        if len(values1)==3:
            if values1[0]!='' and values1[1]!='' and values1[2]!='':
                val1=int(values1[0])
                val2=int(values1[1])
                val3=int(values1[2])
                row=row+1
                post_request_fusion_table(access_token,val1,val2,val3)
                print('success!')
    
    get_values_from_spreadsheet(row)
    


#generates new access token when called

def gen_acc_token():
    client_id = '80194741481-ged71cdpdptf8j6u3522hnihp9e6bd4g.apps.googleusercontent.com'
    client_secret = 'i69xo7rR0tVYENPvIBlR0Odj'
    redirect_uri = 'http://www.example.com/oauth2callback'
    refresh_token='1/uwhh9bfdi9QcDw4PAYfueXjjCouz_VQTmTn68cAPkEs'
    data = urllib.urlencode({
      'client_id': client_id,
      'client_secret': client_secret,
      'refresh_token': refresh_token,
      'grant_type': 'refresh_token'})
    request = urllib2.Request(
      url='https://accounts.google.com/o/oauth2/token',
      data=data)
    request_open = urllib2.urlopen(request)
    response = request_open.read()
    request_open.close()
    tokens = json.loads(response)
    access_token = tokens['access_token']
    return access_token
    
#sends post request to given fusion tables id and automatically updates access token, if expired. 

def post_request_fusion_table(acs_token,val1,val2,val3): 
    table_id='19Kr0bBpapTGNrKCUoUHfs3IaKTYIRkVNTVUDospm'
    reading1=val1
    reading2=val2
    reading3=val3
    access_token=acs_token
    r=requests.post('https://www.googleapis.com/fusiontables/v2/query?sql=INSERT INTO %s ("Number","Date","Location") "VALUES" (%d,%d,%d)&scope=https://www.googleapis.com/auth/fusiontables&access_token=%s' % (table_id,reading1,reading2,reading3,access_token))
    a=str(r)
    if a[11:14]=='401':
        access_token=gen_acc_token()
        post_request_fusion_table(access_token,val1,val2,val3)
      


get_values_from_spreadsheet(9)       

    
