#-*- coding:utf-8 -*-
import sys
import os
import time
import sqlite3
import logging
from selenium import webdriver
logging.basicConfig(format="%(asctime)s-[%(levelname)s]: %(message)s",level=logging.INFO)

DATABASE="CQtest.db"
ROOT,FILENAME=os.path.split(os.path.abspath(__file__))

url=r"https://cas.hhit.edu.cn/lyuapServer/login?service=http://58.192.29.7/login_cas.aspx"


def GetTable(username,password,savePath):
    global url

    options=webdriver.ChromeOptions()
    options._binary_location=ROOT+"/Application/chrome.exe"
    options.add_argument("--disable_gpu")
    options.add_argument("--allow_running-inecure-content")
    options.add_argument("--disable-extensions")
    options.add_argument("--headless")

    chrome=webdriver.Chrome(chrome_options=options,executable_path=ROOT+"/chromedriver.exe")
    chrome.get(url)
    chrome.find_element_by_id("username").send_keys(username)
    chrome.find_element_by_id("password").send_keys(password)
    chrome.find_element_by_class_name("btn-submit").click()
    # time.sleep(5)
    URL=r"http://58.192.29.7/xskbcx.aspx?xh="+username+r"&xm=%BD%F0%C8%CA%BD%DC&gnmkdm=N121603"
    chrome.get(URL)
    body=chrome.find_element_by_xpath("/html/body")
    width=body.size['width']
    height=body.size['height']
    chrome.set_window_size(width,height)
    chrome.save_screenshot(savePath+"/school_timetable.jpg")
    # time.sleep(5)
    chrome.quit()


def GetUserPass(qq):
    conn=sqlite3.connect(DATABASE)
    c=conn.cursor()
    c.execute("select Stu_ID,Password from users where QQ_ID={}".format(qq))
    row=c.fetchone()
    return row
    
# username="2017120097"
# password="07025210"
# GetTable(login(username,password),username,"./")
if __name__ == "__main__":
    username=sys.argv[1]
    password=sys.argv[2]
    savePath=sys.argv[3]
    # username,password=GetUserPass(qq)
    # username="2017120097"
    # password="07025210"
    # savePath="./"
    GetTable(str(username),str(password),savePath)
