#author - The Great Jayasimha!

#In this example my sheets have only 3 columns, if it has more or less than 3, change C in 'A%d:C%d' to corresponding alphabet, for example 'A%d:E%d', if 5 columns. 

import requests
import urllib2, urllib, json, urlfetch
from pprint import pprint
from bs4 import BeautifulSoup

def get_values_from_spreadsheet(row): 
    row=row
    sheets_id='1gSW_8V4q0FZTnQr_Di5yqy6LNgXgbA7IvoyL8VYgZzU'
    r=requests.get('https://sheets.googleapis.com/v4/spreadsheets/%s/values/A%d:C%d?key=AIzaSyCcnQDCQGsTp4dofDS3fjbgGWM3mhBQw_c'%(sheets_id,row,row))
    response=r.json()
    print(response)
    response1=str(response)
    r=len(str(row))
    response1=response1[28+2*r:34+2*r]
    print(response1)
    
    if response1=='values':
        values=response['values']
        values1=values[0]
        if len(values1)==3:
            if values1[0]!='' and values1[1]!='' and values1[2]!='':
                val1=int(values1[0])                       #here datatypes needed are of int, so typecasting to int
                val2=int(values1[1])
                val3=int(values1[2])
                row=row+1
                print('%d %d %d' %(val1,val2,val3))
                print('success!')
                
        get_values_from_spreadsheet(row)
    
    
get_values_from_spreadsheet(5)

