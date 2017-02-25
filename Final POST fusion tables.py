#author The Great Jayasimha!

import requests
import urllib2, urllib, json, urlfetch
from bs4 import BeautifulSoup

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
    
#continuosly sends post request to given fusion tables id and automatically updates access token, if expired. 
def post_request_fusion_table(access_token): 
    table_id='19Kr0bBpapTGNrKCUoUHfs3IaKTYIRkVNTVUDospm'
    reading1=230
    reading2=240
    reading3=250
    access_token=access_token
    r=requests.post('https://www.googleapis.com/fusiontables/v2/query?sql=INSERT INTO %s ("Number","Date","Location") "VALUES" (%d,%d,%d)&scope=https://www.googleapis.com/auth/fusiontables&access_token=%s' % (table_id,reading1,reading2,reading3,access_token))
    a=str(r)
    if a[11:14]=='401':
        access_token=gen_acc_token()
        
    post_request_fusion_table(access_token)
        
post_request_fusion_table('ya29.Glv9A7hrhIUxQ5f9k0tovnr5LEFm_p6Reb9ZGAXsGw_ABcyX0pYKwlgvLxNJ77HxokhkvDhbdT_gi0kQaYtxE-6jm3TIEeMzpV8Iq04hP42cNW5ddcEryDGuO2Wp')
    
