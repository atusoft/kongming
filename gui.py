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

def download_img(url):
    from PIL import Image
    import requests
    from io import BytesIO

    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    pic.image=img
    pic.tk.place(x=0,y=0,relwidth=1,relheight=1)

def show_timer():
    from time import localtime, strftime
    text.value=strftime(u"%y年%m月%d日 %H点%M", localtime())
    load_katong_pic()


app = App(width=420,height=340,bg="black")
app.tk.attributes("-fullscreen",True)
pic=Picture(app)
text = Text(app,size=20,color="white",align='bottom')
text.repeat(60000,show_timer)
show_timer()
app.display()
