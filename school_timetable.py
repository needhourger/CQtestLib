#-*- coding:utf-u8 -*-
import requests
import sys
import sqlite3
import bs4
import logging
logging.basicConfig(format="%(asctime)s-[%(levelname)s]: %(message)s",level=logging.INFO)


url="https://cas.hhit.edu.cn/lyuapServer/login?service=http://58.192.29.7/login_cas.aspx"
