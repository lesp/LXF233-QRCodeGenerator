import easygui as eg
#import os  
from MyQR import myqr

def QRCreator(URL, image, save):
    version, level, qr_name = myqr.run(  
    URL,
    version=1,
    level='H',
    picture=image,
    colorized=True,
    contrast=1.0,
    brightness=1.0,
    save_name=save,
    save_dir="/home/pi/"
    )
    eg.msgbox(msg="Your QR code has been saved to /home/pi/"+save, title="Save Complete")

URL = eg.enterbox(msg="Please provide the URL for the QR code", title="Specify URL for QR code")
print(URL)
image = eg.fileopenbox(msg="What image shall I use with the QR code?", title="Open Image", default="/home/pi/")
print(image)
save = eg.filesavebox(msg="Save QR Code as ?", default="/home/pi/")
print(save)


QRCreator(URL, image, save)
