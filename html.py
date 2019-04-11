#-*- coding=utf-8 -*-
import os
import sys

WORK_PATH,FILE_NAME=os.path.split(os.path.abspath(__file__))
target=""

html_part1='''
<!Doctype html>
<html>
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="./default.css">
    <title>机器人的下载站点</title>
</head>
<body>
    <style type='text/css'>
            .link_class {
              width:auto;
              height: 30px;
              color: #fff;
              text-align: center;
              display: block;
              -webkit-border-radius: 3px;
              -moz-border-radius: 3px;
              border-radius: 3px;
              background: #000;
              text-decoration: none;
              line-height: 30px;
            }
    </style>
'''

html_part2='''
</body>
</html>
'''

def Generate(target,username="小机器人的下载站"):
    files=os.listdir(target)
    filename=[]
    for x in files:
        if not os.path.isdir(x):
            filename.append(x)
    with open(target+"/index.html","w+",encoding="utf-8") as f:
        f.write(html_part1)
        f.write("<h1>{}</h1><br>".format(username))
        f.write('<a class="link_class" href="./BDPurl.html">电影百度盘链接</a><br><br>')
        for x in filename:
            if x!="index.html" and x!="BDPurl.html":
                f.write('<a class="link_class" href="./{}" download>{}</a>'.format(x,x))
                f.write('<br>')
        f.write(html_part2)
        f.close()
        print("html done!")


def main():
    try:
        target=sys.argv[1]
    except:
        target=WORK_PATH

    try:
        username=sys.argv[2]
    except:
        username=""
    
    Generate(target,username)

if __name__=="__main__":
    main()