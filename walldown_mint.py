#!/usr/bin/env python3

import time
import sys
import os
sys.path.append(os.path.abspath("SO_site-packages"))

import pyperclip
import http.client
from os.path import expanduser
import datetime

now = datetime.datetime.now()

dir_path = expanduser("~")+'/Pictures/Wallpapers/' + now.strftime("%y.%m.%d")+'/'

if os.name == 'nt':
    dir_path = dir_path.replace('/', '\\')

if not os.path.exists(dir_path):
    os.makedirs(dir_path)

print('Ready to work, wait for urls!', flush = True)

recent_value = ""

while True:
    tmp_value = pyperclip.paste()
    if tmp_value != recent_value:
        recent_value = tmp_value
        if 'https://alpha.wallhaven.cc/wallpaper/' in recent_value:
            conn = http.client.HTTPSConnection('alpha.wallhaven.cc')
            conn.request('GET', recent_value)
            res = conn.getresponse()
            page = res.read().decode('utf-8')
            find = '<img id="wallpaper" src="//'
            pos = page.find(find)
            img = page[pos + len(find):pos + 300]
            pos = img.find('" alt="')
            img = img[:pos]
            print('URL captured: ' + img, flush = True)
            file_name = img.split('/');
            conn = http.client.HTTPSConnection('wallpapers.wallhaven.cc')
            conn.request('GET', 'https://' + img)
            res = conn.getresponse()
            img = res.read()
            home = expanduser("~")
            file_path = dir_path + file_name[-1]
            if os.path.exists(file_path):
                print('File exist! ' + file_path, flush = True)
                continue
            file = open(file_path, 'wb')
            file.write(img)
            file.close()
            print('Download finished! To: ' + file_path, flush = True)
    time.sleep(0.5)