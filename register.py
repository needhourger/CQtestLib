#-*- coding:utf-8 -*-
import requests
import sys
import sqlite3
import bs4
import logging
logging.basicConfig(format="%(asctime)s-[%(levelname)s]: %(message)s",level=logging.INFO)

users_sql="""
CREATE TABLE IF NOT EXISTS Users(
QQ_ID INTEGER PRIMARY KEY NOT NULL,
Stu_ID INTEGER,
Password TEXT,
Name TEXT DEFAULT NULL,
Gender TEXT DEFAULT NULL,
Department TEXT DEFAULT NULL,
Notice_uptime TEXT DEFAULT NULL,
isVIP INTEGER DEFAULT 0,
isBanned INTEGER DEFAULT 0,
isRegistered INTEGER DEFAULT 0
);
"""


def login(username,password):
    """
    登陆信息门户
    username: 用户名
    password: 密码
    返回值
    session: 信息门户session requests.session
    soup: 信息门户bs4 bs4.beautifulsoup
    """
    URL=r"https://cas.hhit.edu.cn/lyuapServer/login?service=http%3A%2F%2Fportal.hhit.edu.cn%2Fc%2Fportal%2Flogin%3Fredirect%3D%252F%26p_l_id%3D70131"
    
    session=requests.Session()
    logging.info("Connect to {}".format(URL))
    r=session.get(URL)
    html=bs4.BeautifulSoup(r.text,"html.parser")

    lt=html.find('input',attrs={"type":"hidden","name":"lt"})["value"]
    logging.info("Get lt: {}".format(lt))
    execution=html.find('input',attrs={"type":"hidden","name":"execution"})['value']
    logging.info("Get execution: {}".format(execution))
    eventId=html.find('input',attrs={"type":"hidden","name":"_eventId"})['value']
    logging.info("Get eventId: {}".format(eventId))
    captcha=html.find('input',attrs={"type":"hidden","name":"captcha"})['value']
    logging.info("Get captch: {}".format(captcha))
    
    param={
        "username":username,
        "password":password,
        "lt":lt,
        "execution":execution,
        "_eventId":eventId,
        "login":r"%E7%99%BB%E5%BD%95",
        "captcha":captcha
    }

    logging.info("Try logging...")
    r=session.post(URL,data=param)
    soup=bs4.BeautifulSoup(r.text,"html.parser")
    if "学生首页" in soup.find('title').get_text():
        return session,soup
    return None

def register(username,password,qq):
    session,soup=login(username,password)
    if session!=None:
        logging.info("login success")
    else:
        logging.error("login failed")
        return
    class_userinfo=soup.find('div',attrs={"class":"_hhitwin8userinfo_WAR_hhitwin8userinfoportlet_imgBox"})
    tds=class_userinfo.findChildren('td')
    if tds==None:
        logging.error("missing td")
        return

    info={}
    for td in tds:
        text=td.get_text().split('：')
        try:
            info[text[0]]=text[1]
        except:
            info[text[0]]=""
        
    db=sqlite3.connect("./CQtest.db")
    if db==None:
        logging.error("failed to connect ro database")
        return
    logging.info("connect to databases success")
    logging.info("Users table init")
    cursor=db.cursor()
    cursor.execute(users_sql)
    db.commit()
    logging.info("check is Banned")
    cursor.execute("select isBanned,isRegistered from users where Stu_id={} limit 1;".format(username))
    # print(cursor.rowcount)
    row=cursor.fetchone()
    # print(row)
    if row==None or row==(0,0):
        cursor.execute(
        "insert or replace into users (QQ_ID,Stu_ID,Password,Name,Gender,Department,Notice_uptime,isvip,isbanned,isregistered) values({},{},'{}','{}','{}','{}',NULL,0,0,1);".format(qq,username,password,info.get('姓名'),info.get('性别'),info.get('部门'))
        )
        logging.info("update user")
    else:
        logging.warning("this user has been banned or has registered")
    db.commit()
    db.close()
    return
        

if __name__=="__main__":
    try:
        args=sys.argv[1]
        username,password=args.split(" ")
        qq=sys.argv[2]
    except:
        username=input("Username: ")
        password=input("Password: ")
        qq=input("QQ: ")
        
    logging.info("Username: {}".format(username))
    logging.info("password: {}".format(password))
    logging.info("QQ: {}".format(qq))
    register(username,password,qq)