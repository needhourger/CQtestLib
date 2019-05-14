# CQtest Lib

>### cc.yuukisama.CQtest 项目的相关依赖代码

* Github: [https://github.com/needhourger/CQtestLib](https://github.com/needhourger/CQtestLib)

>### 环境
* python 3.5+
* pyinstaller

>### 包含
1. BDWKdonwload.py  百度文库下载部分

1. html.py 生成下载页面

1. music.py 音乐下载部分

1. QR.py 将链接转换为二维码

1. movie.py 电影链接爬取

1. register.py 校园信息门户爬取认证

1. manager.py 简易数据库链接管理工具

>2019.5.14更新
1. 修复部分程序bug

1. new_music.py正在开发的独立音乐下载功能

>2019.4.24更新

1. register.py 校园信息门户爬取认证

1. manager.py 简易数据库链接管理工具

>### 使用方法
1. 使用对应版本的pyinstaller将上述py文件打包生成exe

1. 在酷Q安装目录下新建download文件夹，将如下文件放入其中
    * 上述所有打包生成的exe
    * javaScript.js文件
    * chromedriver.exe
    * Application/ 文件夹

1. 受限于github只可以上传小于50m的文件，将
    ```Application/71.0.3578.98/chrome_child.rar```
    解压到当前文件夹后再使用