#!/usr/bin/python

#Web Search Specific Arguments
#http://code.google.com/apis/ajaxsearch/documentation/reference.html#_fonje_web

#Standard URL Arguments
#http://code.google.com/apis/ajaxsearch/documentation/reference.html#_fonje_args

#Google AJAX Search Module
#http://code.google.com/apis/ajaxsearch/documentation/reference.html

try:
    import simplejson as json
except:
    import json
import urllib

URL = 'http://ajax.googleapis.com/ajax/services/search/web?'

#import sys
#query = ' '.join(sys.argv[1:])

def search(query):
    flter = 1          #Controls turning on or off the duplicate content filter. On = 1.
    rsz = 3            #Results per page. small = 4 /large = 8
    safe = "off"       #SafeBrowsing -  active/moderate/off
    hl = "en"          #language; defaults to English (en)
    titles = []
    urls = []

    args = {'q' : query, 'v' : '1.0', 'start' : 0, 'rsz': rsz, 'safe' : safe, 'filter' : flter, 'hl' : hl}
    q = urllib.urlencode(args)
    search_results = urllib.urlopen(URL+q)
    data = json.loads(search_results.read())
    if data['responseStatus'] == 200:
        for result in data['responseData']['results']:
            if result:
                titles.append(urllib.unquote(result['titleNoFormatting']))
                urls.append(urllib.unquote(result['visibleUrl']))
    return titles,urls

q1= raw_input('Enter Company name ')
t1,u1 = search(q1)
u1.append(q1)

q= raw_input('Enter email ')
q2= q.split("@",1)[1]
t2,u2 = search(q2)
t2.append(q)

from ctypes import *
lib = cdll.LoadLibrary('./company_v1.so')
arr = (c_char_p * len(u1))()
arr[:] = u1
arr1 = (c_char_p * len(t2))()
arr1[:] = t2
lib.start_here(len(u1), arr, len(t2), arr1)

