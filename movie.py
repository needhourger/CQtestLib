#-*- coding=utf-8 -*-
import requests
import os
import sys
# import chardet
from bs4 import BeautifulSoup

WORKPLACE,FILENAME=os.path.split(os.path.abspath(__file__))
SAVEPATH="./"

URL_BASE="http://www.coupling.pw/"
s="overload"

def Geturl(film_name):
    global SAVEPATH

    if not os.path.exists(SAVEPATH):
        os.mkdir(SAVEPATH)
    
    f=open(SAVEPATH+"/BDPurl.html","w+",encoding="utf-8")
    f.write('''
        <html>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <head>
        ''')

    

    data={"s":film_name}
    r=requests.get(URL_BASE,params=data)
    try:
        html=BeautifulSoup(r.text,"html.parser")
        entry=html.find_all(attrs={"class":"entry-title"})
        a=[]
        for x in entry:
            a=a+x.find_all("a")
        if a!=[]:
            url=a[0]["href"]

        r=requests.get(url)
        html=BeautifulSoup(r.text,"html.parser")            
        p=html.find_all('a',attrs={"target":"_blank"},text="百度云盘")
        for i in p:
            print (i.parent)
            f.write(str(i.parent))
            f.write("\n<br><br>\n")
        if p==[]:
            f.write("<h1>未找到相关电影百度云资源</h1>")
        p=html.find_all('a',attrs={"rel":"noopener","target":"_blank"})
        for i in p:
            if "微信公众号" in i.get_text():
                continue
            print(i)
            f.write(str(i))
            f.write("\n<br><br>\n")
        if p==[]:
            f.write("<h1>未找到相关电影磁力链接资源</h1>")
        
            
    except:
        
        html=BeautifulSoup(r.text,"html.parser")            
        p=html.find_all('a',attrs={"target":"_blank"},text="百度云盘")
        for i in p:
            print (i.parent)
            f.write(str(i.parent))
            f.write("\n<br><br>\n")
        if p==[]:
            f.write("<h1>未找到相关电影百度云资源</h1>")
        p=html.find_all('a',attrs={"rel":"noopener","target":"_blank"})
        for i in p:
            if "微信公众号" in i.get_text():
                continue
            print(i)
            f.write(str(i))
            f.write("\n<br><br>\n")
        if p==[]:
            f.write("<h1>未找到相关电影磁力链接资源</h1>")
        
    finally:
        f.close()
          

# def Save(ret):
#     global SAVEPATH
#     # print(chardet.detect(ret.encode("utf-8")))
#     if not os.path.exists(SAVEPATH):
#         os.mkdir(SAVEPATH)
#     with open(SAVEPATH+"/BDPurl.html","w+",encoding="utf-8") as f:
#         f.write('''
#         <html>
#         <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
#         <head>
#         ''')
#         f.write(ret)
#         f.close()

def main():
    global SAVEPATH
    film_name=""
    try:
        film_name=sys.argv[1]
        SAVEPATH=sys.argv[2]
    except:
        film_name=input()
    Geturl(film_name)
    # Save(ret)

if __name__=="__main__":
    main()