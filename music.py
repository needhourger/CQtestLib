#-*- coding=utf-8 -*-
import requests
import json
import sys
import os
import time

from selenium import webdriver

WORK_PATH,FILENAME=os.path.split(os.path.abspath(__file__))
SAVE_PATH=WORK_PATH
cookies=[]
suffix=""

url_base="http://moresound.tk/music/"
url_search="http://moresound.tk/music/api.php?search=qq"
url_song="http://moresound.tk/music/api.php?get_song=qq"

def new_cookies():
    global cookies,url_base

    opt=webdriver.ChromeOptions()
    opt._binary_location=WORK_PATH+"/Application/chrome.exe"
    opt.add_argument("--disable-extensions")
    opt.add_argument("--disable-gpu")
    opt.add_argument("--headless")

    chrome=webdriver.Chrome(options=opt)
    chrome.get(url_base)
    chrome.find_element_by_id("tipsDayPage").click()
    cookies=chrome.get_cookies()
    chrome.quit()

    with open(WORK_PATH+"/cookies","w+") as f:
        f.write(json.dumps(cookies))
        f.close()

def load_cookies():
    global cookies
    if not os.path.exists(WORK_PATH+"/cookies"):
        new_cookies()
    
    with open(WORK_PATH+"/cookies","r") as f:
        cookies=json.load(f)
        now=int(time.time())
        for x in cookies:
            if x['expiry']<=now:
                new_cookies()
                f.close()
                return

def generate():
    global cookies
    ret={}
    for x in cookies:
        if "name" in x and "value" in x:
            ret[x["name"]]=x["value"]
    return ret

def main():
    
    load_cookies()
    song_name=""
    try:
        song_name=sys.argv[1]
    except:
        song_name=input("Song name:")
        
    
    try:
        SAVE_PATH=sys.argv[2]
        suffix=sys.argv[3]
    except:
        SAVE_PATH=WORK_PATH
        suffix=""

    
    param={"w":song_name,"p":1,"n":1}
    cookie=generate()
    print(cookie)
    r=requests.post(url_search,data=param,cookies=cookie)
    ret=json.loads(r.text)
    print(ret)
    if "song_list" in ret:
        mid=ret['song_list'][0]['songmid']
    else:
        print("no songlist")
        return
    
    param={"mid":mid}
    r=requests.post(url_song,param,cookies=cookie)
    ret=json.loads(r.text)
    filename="default"
    if "url" in ret:
        urls=ret['url']
        if "song" in ret:
            filename=ret['song']
        if "singer" in ret:
            filename=filename+" - "+ret['singer']
    else:
        print("no urls")
        return

    url=""
    if "320MP3" in urls:
        url=urls.get("320MP3")
    elif "128MP3" in urls:
        url=urls.get("128MP3")
    
    if url=="":
        print("No resource")
        return
    
    r=requests.get(url_base+url,cookies=cookie)
    ret=json.loads(r.text)
    if "url" in ret:
        url=ret['url']
        if "suffix" in ret:
            filename=filename+suffix+"."+ret['suffix']
        r=requests.get(url)
        if not os.path.exists(SAVE_PATH):
            os.mkdir(SAVE_PATH)
        with open(SAVE_PATH+"/"+filename,"wb") as f:
            f.write(r.content)
            f.close()
            print("dwonload "+filename)
    else:
        print ("last error no url")

if __name__=="__main__":
    main()
