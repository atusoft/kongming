#! /usr/bin/python3
from guizero import *

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

def download_img(image_link):
    import shutil
    import requests
    r=requests.get(image_link,stream=True)
    with open('img.png','wb') as out_file:
        shutil.copyfileobj(r.raw,out_file)
    pic.image='img.png'
    pic.tk.place(x=0,y=0,relwidth=1,relheight=1)
    del r

def show_timer():
    from time import gmtime, strftime
    text.value=strftime(u"%y年%m月%d日 %H:%M:%S", gmtime())


app = App(width=420,height=340,bg="black")
app.tk.attributes("-fullscreen",True)
pic=Picture(app)
pic.repeat(30000,load_katong_pic)
text = Text(app,size=20,color="white",align='bottom')
text.repeat(1000,show_timer)
app.display()
