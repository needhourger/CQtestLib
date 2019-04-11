#-*- coding=utf-8 -*-
import sys
import os
import qrcode

WORKPATH,FILENAME=os.path.split(os.path.abspath(__file__))
SAVE_PATH="./"
url=""

def main():
    global SAVE_PATH,url
    try:
        url=sys.argv[1]
        SAVE_PATH=sys.argv[2]
    except:
        url=input()
    
    qr=qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img=qr.make_image(fill_color="black",back_color="white")
    if (not os.path.exists(SAVE_PATH)):
        os.mkdir(SAVE_PATH)
    
    img.save(SAVE_PATH+"/QRcode.png")
    

if __name__=="__main__":
    main()