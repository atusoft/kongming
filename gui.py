#! /usr/bin/python3
from guizero import *

import threading

class MyThread(threading.Thread):
    def __init__(self, func, *args):
        super().__init__()

        self.func = func
        self.args = args

        self.setDaemon(True)
        self.start()    # 在这里开始

    def run(self):
        self.func(*self.args)

def load_katong_pic():
    import feedparser
    import re
    import random
    d=feedparser.parse('https://rsshub.app/pigtails')
    l=len(d.entries)
    i=random.randrange(l)

    img=d.entries[i].description
    s=re.search('src="([^"]*)"',img)
    download_img(s.group(1))

def download_img(url):
    from PIL import Image
    import requests
    from io import BytesIO

    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.thumbnail((480,320),Image.ANTIALIAS) 
    pic.image=img
    pic.tk.place(x=0,y=0,relwidth=1,relheight=1)

def show_timer():
    from time import localtime, strftime
    text.value=strftime(u"%y-%m-%d %H:%M", localtime())
    import subprocess
    subprocess.call(['xdotool','keydown','Shift_L','keyup','Shift_L'])

app = App(width=480,height=320,bg="black")
app.tk.attributes("-fullscreen",True)
pic=Picture(app)
pic.repeat(60000,lambda :MyThread(load_katong_pic))
text = Text(app,size=20,color="grey",align='bottom',font='Spaceport One')
text.repeat(60000,show_timer)
show_timer()
app.display()
