from PIL import ImageGrab,Image
from datetime import datetime
from areaselector import areaSelector
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
useAreaSelector = True          # flag for whether to use gui for capture area selection

captureAreaX = 0                # capture area's starting x position on screen
captureAreaY = 0                # capture area's starting y position on screen
captureAreaWidth = 1920         # width of capture area in pixels
captureAreaHeight = 1080        # height of capture area in pixels

# uncomment anyone of the following slideArea to fit your capture area if useAreaSelector is false
#slideArea = (captureAreaX,captureAreaY,captureAreaWidth,captureAreaHeight)        # area of capture for fullscreen 1920 x 1080 screen
#slideArea = (0,130,1920,1020)                                                     # screen coordinates for chrome 1920 x 1080 screen
slideArea = (0,90,1920,1020)                                                       # screen coordinates for firefox 1920 x 1080 screen

def main():
    global slideCount,directoryName
    
    if slideCount > 1:
        newSlide = ImageGrab.grab(bbox=slideArea,all_screens=True)
    
    # session and 1st iteration setup
    if slideCount == 1:
        # display app banner
        putBanner()

        # use area selection gui according to flag
        if useAreaSelector:
            print("\rWaiting for Capture area selection ...",end="")
            areaSelectorGui = areaSelector()
            setCaptureArea(areaSelectorGui.getCaptureArea())

        # create new directory for storing screenshots
        newDirectoryName = input("\r\bEnter directory name[optional]  :     ")
        if newDirectoryName.strip() != "":
            directoryName = f"{baseDir}\\{newDirectoryName}"
        os.system(f"mkdir {directoryName}")
        
        # create a delay in capture launch for user to get ready
        for i in range(1,waitBeforeCaptureStart):
            print(f"\rSlide capture will start in {waitBeforeCaptureStart-i}sec ...",end="")
            time.sleep(1)
        print("\n[!] press ctrl + c to stop ")

        # capture and store initial slide/frame/screenshot
        newSlide = ImageGrab.grab(bbox=slideArea,all_screens=True)
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
    '''for checking if the new capture is different than the last one'''
    global slideCount,directoryName
    oldSlide = Image.open(f"{directoryName}\{slideCount-1}.png")
    oldSlideArray = np.array(oldSlide)
    newSlideArray = np.array(newSlide)
    if np.allclose(newSlideArray,oldSlideArray,rtol,atol):
        return False
    else:
        return True

def setCaptureArea(newSlideArea):
    '''for setting new capture area cordinates if area selection gui is used'''
    global slideArea
    slideArea = (
        newSlideArea['x'],
        newSlideArea['y'],
        newSlideArea['width'],
        newSlideArea['height'],
    )

def putBanner():
    '''for displaying app banner'''
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
                                                                                                

'''main loop'''
while True:
    try:
        main()
        time.sleep(frequency)
    except:
        print(f"\n[*] Total {slideCount-1} slides Saved [*]")
        exit(1)
