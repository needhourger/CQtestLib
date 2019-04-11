#-*- coding=utf-8 -*-
import os
import json
import sys
import shutil
import html


from selenium import webdriver

ROOT,FILENAME=os.path.split(os.path.abspath(__file__))
JavaScript=""
SAVEPATH="./"
USERNAME=os.getenv("username")

def LoadJs():
    global JavaScript
    if (not os.path.exists(ROOT+"/JavaScript.js")):
        print("JavaScript.js not found")
        exit(1)
    try:
        f=open(ROOT+"/JavaScript.js","r")
        JavaScript=f.read()
    except:
        print("Unknown error")
        exit(1)


def checking(f):
    global USERNAME,SAVEPATH
    path=os.path.join(os.path.expanduser("~"),"Downloads")
    if os.path.exists(path+"/"+f):
        print("download confirm")
        print(f)
        if not os.path.exists(SAVEPATH):
            os.mkdir(SAVEPATH)
        # shutil.move(path+"/"+f,SAVEPATH+"/"+f)
        shutil.copyfile(path+"/"+f,SAVEPATH+"/"+f)
        os.remove(path+"/"+f)
        
def download(url,timeout=30):
    global JavaScript
    
    appState = { 
        "recentDestinations": [ 
        { 
        "id": "Save as PDF", 
        "origin": "local" 
        } 
        ], 
        "selectedDestinationId": "Save as PDF", 
        "version": 2
    } 
    profile = {
        'printing.print_preview_sticky_settings.appState': json.dumps(appState)
    } 
    options=webdriver.ChromeOptions()
    options._binary_location=ROOT+"/Application/chrome.exe"
    options.add_experimental_option("prefs",profile)
    options.add_argument("--disable-gpu")
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--kiosk-printing')
    options.add_argument('--disable-extensions')
    #options.add_argument('--headless')
    
    chrome=webdriver.Chrome(chrome_options=options,executable_path=ROOT+"/chromedriver.exe")
    chrome.set_script_timeout(timeout)
    print("Geting url...")
    try:
        chrome.get(url)
        filename=chrome.title
    except:
        print("Error on get url")
    try:
        print("Execute JavaScript...")
        chrome.execute_async_script(JavaScript)
    except:
        print("Error on execute JavaScript")
    finally:    
        chrome.quit()
        checking(filename+".pdf")



        
    
def main():
    global JavaScript,SAVEPATH
    
    LoadJs()
    try:
        # print(JavaScript)
        url=sys.argv[1]
        SAVEPATH=sys.argv[2]
        try:
            timeout=sys.argv[3]
        except:
            timeout=30
        # url="https://wenku.baidu.com/view/8952e6fb0c22590102029d8f.html?from=search"
        # SAVEPATH="E:/workplace"
        download(url,timeout)
    except:
        # print("usage: python "+FILENAME+" <url> <SAVE_PATH> <TIMEOUT=30>")
        url=input("url:")
        timeout=input("timeout:")
        download(url,timeout)
    
    
        

if __name__=="__main__":
    main()

