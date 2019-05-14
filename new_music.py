#-*- coding:utf-8 -*-
import requests
import json
import logging
logging.basicConfig(format="%(asctime)s-[%(levelname)s]:%(message)s",level=logging.INFO)

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.3"
}

tencentUrlSearch="https://c.y.qq.com/soso/fcgi-bin/client_search_cp"
tencentUrlSong="https://c.y.qq.com/v8/fcg-bin/fcg_play_single_song.fcg"
searchParams={
    "format":"json",
    "p":"1",
    "n":"1",
    "w":"千与千寻",
    "aggr":"1",
    "lossless":"1",
    "cr":"1",
    "new_json":"1"
}

session=requests.Session()
logging.info("Searching ...")
r=session.get(tencentUrlSearch,params=searchParams,headers=headers)
result=json.loads(r.text)
logging.info(result.get("message"))

songParams={
    "songmid":result.get('data').get
}
r=session.get(tencentUrlSong,)





