# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 01:31:14 2020

"""

import json
import re

from CMS import Format
import io
def getfromjson():
    with open('./devopediaArticles.json') as f:
        fulljson_dct= json.load(f)
    url_dct_r={}
    text_dct_r={}
    url_dct_f={}
    text_dct_f={}
    for x,jsonitemnos_dct in fulljson_dct.items():
        list1=[]
        list2=[]
        list3=[]
        list4=[]
        if('References' in jsonitemnos_dct['secs'].keys()):
            
            for w in jsonitemnos_dct['secs']['References']:
                
                try:
                    list1.append(w['url'])
                    
                except:
                    print('')
                try:
                    list2.append(w['text'])
                   
                except:
                    continue
        
        url_dct_r[x]= list1
        text_dct_r[x]= list2
        if('Further Reading' in jsonitemnos_dct['secs'].keys()):
                    for w in jsonitemnos_dct['secs']['Further Reading']:
                        try:
                            list3.append(w['url'])
                        except:
                            print('')
                        try:
                            list4.append(w['text'])
                        except:
                            continue 
        
        url_dct_f[x]= list3
        text_dct_f[x]= list4        
     
    return [text_dct_r,text_dct_f]
   # return [url_dct_r,url_dct_f]
#import pdb;pdb.set_trace()   
text_dct= getfromjson() 
#url_dct=getfromjson()
#print(url_dct)



def extract_details(text_dct):
    ref = Format.AuthorDateFormat();
    #variable={}
    pattern1=re.compile(r'(?P<authors>.*?)\.\W*(?P<year>[0-9]{4}[a-z]?)\.\W*(?P<title>\".*\")\.?.*' )
    pattern2 = re.compile(r'\s*([\S]+)$')
    pattern3 = re.compile(r"\"\W.*?(?P<details>.*?)?(\.)?\W*?(?P<publisher>.*?)\,.*?")
    pattern4=re.compile(r",?(?P<date>[A-Za-z]+\W([0-2][0-9]|[3][01]))?(\.\W*)?(\,\W*)?(?P<date_updated>(Updated?\W[a-zA-Z]+\W+([0-9]{1,2}|([0-2]?[0-9]|[3]?[01])-([0-2]?[0-9]|[3]?[01]))|[0-9]{4}-[0-9]{2}-[0-9]{2})?)(\.\W*)?(?P<access_date>(Accessed|Retrieved)\W*[0-9]{4}-[0-9]{2}-[0-9]{2})(\.\W*)")
  
    
    for key,lines in text_dct[0].items():
        #import pdb;pdb.set_trace()
        for k,line in enumerate(lines):
            ref.author_name.append([i.group('authors') for i in pattern1.finditer(str(line))])
            ref.year_of_publication.append([i.group('year') for i in pattern1.finditer(str(line))])
            ref.title.append([i.group('title') for i in pattern1.finditer(line)])
            ref.access_date.append([pattern2.findall(line)])
            ref.publisher_name.append([i.group('publisher') for i in pattern3.finditer(str(line))])
            ref.date_of_publication.append([i.group('date') for i in pattern4.finditer(str(line))] )
            ref.date_updated.append([i.group('date_updated') for i in pattern4.finditer(str(line))] )
            ref.access_date.append([i.group('access_date') for i in pattern4.finditer(str(line))] )
     
    for key,line in text_dct[0].items():
         for k,line in enumerate(lines):
             ref.author_name.append([i.group('authors') for i in pattern1.finditer(str(line))])
             ref.publisher_name.append([i.group('publisher') for i in pattern3.finditer(str(line))])
             ref.year_of_publication.append([i.group('year') for i in pattern1.finditer(str(line))])
             ref.title.append([i.group('title') for i in pattern1.finditer(line)])
             ref.access_date.append([pattern2.findall(line)])
             ref.date_of_publication.append([i.group('date') for i in pattern4.finditer(str(line))] )
             ref.date_of_publication.append([i.group('date') for i in pattern4.finditer(str(line))] )
             ref.date_updated.append([i.group('date_updated') for i in pattern4.finditer(str(line))] )
             ref.access_date.append([i.group('access_date') for i in pattern4.finditer(str(line))] )
        
    return [ref.date_updated]
matches= extract_details(text_dct)
print(matches)
f1= io.open("resources.txt","w+",encoding="utf-8")
f1.write("%s\n" % matches)
f1.close()  

