#! /usr/bin/python3
from guizero import *

import threading
import yaml

class MyThread(threading.Thread):
    def __init__(self, func, *args):
        super().__init__()

        self.func = func
        self.args = args

        self.setDaemon(True)
        self.start()    # 在这里开始

    def run(self):
        self.func(*self.args)

def load_pic(urls):
    import feedparser
    import re
    import random
    if(len(pics)==0):
        for url in urls:
            d=feedparser.parse(url)
            for n in d.entries:
                img=n.description
                s=re.search('src="([^"]*)"',img)
                pics.append(s.group(1))

    l=len(pics)
    i=random.randrange(l)

    download_img(pics[i])

def download_img(url):
    from PIL import Image
    import requests
    from io import BytesIO

    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.thumbnail((480,320),Image.ANTIALIAS) 
    pic.value=img
    pic.tk.place(x=0,y=0,relwidth=1,relheight=1)
    pic.resize(480,320)
    app.update()

def show_timer():
    from time import localtime, strftime
    text.value=strftime(u"%y-%m-%d %H:%M", localtime())
    import subprocess
    subprocess.call(['xdotool','keydown','Shift_L','keyup','Shift_L'])

if __name__=='__main__':
    app = App(width=480,height=320,bg="black")
    app.tk.attributes("-fullscreen",True)
    pic=Picture(app)
    f=open('config.yml')
    url=yaml.load(f)['url']
    pics=[]
    pic.repeat(60000,lambda :MyThread(load_pic,url))
    text = Text(app,size=20,color="grey",align='bottom',font='Spaceport One')
    text.repeat(60000,show_timer)
    show_timer()
    app.display()
