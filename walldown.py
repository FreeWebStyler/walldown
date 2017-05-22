import time
import sys
import os
sys.path.append(os.path.abspath("SO_site-packages"))

import pyperclip
import http.client
#import http
from os.path import expanduser
import datetime

now = datetime.datetime.now()

dir = expanduser("~")+'/Pictures/Wallpapers/' + now.strftime("%y.%m.%d")+'/'
#now = datetime.datetime.now() print(now.year)

recent_value = ""
while True:
    tmp_value = pyperclip.paste()
    if tmp_value != recent_value:
        recent_value = tmp_value
        #if 'zhttps://alpha.wallhaven.cc/wallpaper/' not in recent_value:
        if 'https://alpha.wallhaven.cc/wallpaper/' in recent_value:
            #print ("Value changed: %s" % str(recent_value)[:20])
            #print ("Value changed: " + str(recent_value))
            conn = http.client.HTTPSConnection('alpha.wallhaven.cc')
            #conn.request('GET', 'https://alpha.wallhaven.cc/wallpaper/6492')
            conn.request('GET', recent_value)
            res = conn.getresponse()
            page = res.read().decode('utf-8')
            #print(page)
            #print(type(page))
            find = '<img id="wallpaper" src="//'
            pos = page.find(find)
            #print(type(pos))
            #print(pos)
            #pos = page.find('6492.jpg')
            #print('pos:' + str(pos))
            img = page[pos + len(find):pos + 300]
            pos = img.find('" alt="')
            img = img[:pos]
            print(img) #'https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-294165.jpg'
            file_name = img.split('/');
            conn = http.client.HTTPSConnection('wallpapers.wallhaven.cc')
            conn.request('GET', 'https://' + img)
            res = conn.getresponse()

            img = res.read()#.decode('utf-8').strip()
            #img = res.read().decode('utf16')
            #print(type(img))
            home = expanduser("~")
            file = open(dir+file_name[-1], 'wb')
            file.write(img)
            file.close()
            print('Download finished!')
    time.sleep(0.1)