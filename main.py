from PIL import ImageGrab,Image
from datetime import datetime
import numpy as np
import os
import time

global slideCount,directoryName
slideCount = 1
baseDir = os.path.dirname(os.path.realpath(__file__))
directoryName = f"{baseDir}\\bunk-inator-slides_{datetime.today().strftime('%d-%m-%y')}_{datetime.now().strftime('%H.%M.%S')}"

# tunable vars
waitBeforeCaptureStart = 6      # will wait x-1 secs before starting script
frequency = 1                   # will capture every x secs
atol = 40                       # absolute tolerance for comparing new capture with last capture
rtol = 43                       # relative tolerance for comparing new capture with last capture
captureAreaX = 0                # capture area's starting x position on screen
captureAreaY = 0                # capture area's starting y position on screen
captureAreaWidth = 1920         # width of capture area in pixels
captureAreaHeight = 1080        # height of capture area in pixels

# uncomment anyone of the following slideArea to fit your capture area
#slideArea = (captureAreaX,captureAreaY,captureAreaWidth,captureAreaHeight)        # area of capture for fullscreen 1920 x 1080 screen
#slideArea = (0,130,1920,1020)                                                     # screen coordinates for chrome 1920 x 1080 screen
slideArea = (0,90,1920,1020)                                                       # screen coordinates for firefox 1920 x 1080 screen

def main():
    global slideCount,directoryName
    
    if slideCount > 1:
        newSlide = ImageGrab.grab(bbox=slideArea)

    if slideCount == 1:
        putBanner()
        newDirectoryName = input("Enter directory name[optional] : ")
        if newDirectoryName.strip() != "":
            directoryName = f"{baseDir}\\{newDirectoryName}"
        os.system(f"mkdir {directoryName}")
        
        for i in range(1,waitBeforeCaptureStart):
            print(f"\rSlide capture will start in {waitBeforeCaptureStart-i}sec ...",end="")
            time.sleep(1)
        
        newSlide = ImageGrab.grab(bbox=slideArea)
        newSlide.save(f"{directoryName}\{slideCount}.png")
        statusMsg = f"\r\b[+] {slideCount} slides Captured ..."
        print(statusMsg + (38-len(statusMsg))*" ",end="")
        slideCount += 1 
    
    elif slideIsChanged(newSlide):
        newSlide.save(f"{directoryName}\{slideCount}.png")
        statusMsg = f"\r\b[+] {slideCount} slides Captured ..."
        print(statusMsg + (38-len(statusMsg))*" ",end="")
        slideCount += 1


def slideIsChanged(newSlide):
    global slideCount,directoryName
    oldSlide = Image.open(f"{directoryName}\{slideCount-1}.png")
    oldSlideArray = np.array(oldSlide)
    newSlideArray = np.array(newSlide)
    if np.allclose(newSlideArray,oldSlideArray,rtol,atol):
        return False
    else:
        return True


def putBanner():
    os.system("cls") if os.name == "nt" else os.system("clear")

    banner = '''
        ██████╗ ██╗   ██╗███╗   ██╗██╗  ██╗              ██╗███╗   ██╗ █████╗ ████████╗ ██████╗ ██████╗ 
        ██╔══██╗██║   ██║████╗  ██║██║ ██╔╝              ██║████╗  ██║██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
        ██████╔╝██║   ██║██╔██╗ ██║█████╔╝     █████╗    ██║██╔██╗ ██║███████║   ██║   ██║   ██║██████╔╝
        ██╔══██╗██║   ██║██║╚██╗██║██╔═██╗     ╚════╝    ██║██║╚██╗██║██╔══██║   ██║   ██║   ██║██╔══██╗
        ██████╔╝╚██████╔╝██║ ╚████║██║  ██╗              ██║██║ ╚████║██║  ██║   ██║   ╚██████╔╝██║  ██║
        ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝              ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝

        Bunk-inator - A notes taking app for lazy smart people like you
    '''
    print(banner)
                                                                                                

while True:
    try:
        main()
        time.sleep(frequency)
    except:
        print(f"\n[*] Total {slideCount-1} slides Saved [*]")
        exit(1)
