import pyautogui
import time

#TODO: Add album link input
#This scraper supports:
#https://brielarson.org/gallery
#2020-12-29

#Enter number of images in album to be downloaded
number = input("Enter the number of images in album \n")

#Enter the y-value of nextbutton
ynextbutton = input("Enter the y-value of nextbutton \n")

def openpopup():
    filCords = pyautogui.locateCenterOnScreen("fil.png", grayscale = True)
    time.sleep(1)
    pyautogui.moveTo(filCords)
    pyautogui.move(0, 200, 1)
    #time.sleep(1)
    #pyautogui.moveTo(500, 300, 1)
    #pyautogui.click()

def openrightmenu():
    time.sleep(10)
    brielarsonfan = pyautogui.locateCenterOnScreen("brielarsonfan")
    pyautogui.moveTo(brielarsonfan)
    #pyautogui.moveTo(200, 200, 0.5)
    pyautogui.click(button='right')

def nextbutton():
    time.sleep(1)
    #nextbutton = pyautogui.locateCenterOnScreen("nextbutton.png", grayscale = True, region=(0,0, 1000, 400))
    #pyautogui.click(nextbutton)
    pyautogui.click(800, int(ynextbutton))

def firstscrape():
    #Open popup image
    openpopup()

    #Open right-click menu
    openrightmenu()

    #Click save button
    time.sleep(1)
    savebuttonCords = pyautogui.locateCenterOnScreen("savebutton.png", grayscale = True)
    pyautogui.click(savebuttonCords)

    #Explorer save window action, creates new folder
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'l')
    time.sleep(0.5)
    pyautogui.write('Hämtade filer', interval=0.2)
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'shift', 'n')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    sparabutton = pyautogui.locateCenterOnScreen('sparabutton.png', grayscale = True)
    pyautogui.click(sparabutton)

    #Close picture popup
    time.sleep(1)
    pyautogui.move(-200, -200)
    pyautogui.click()

    #Go to next image
    nextbutton()

def scrape():

    #Open popup image
    openpopup()

    #Open right-click menu
    openrightmenu()

    #Click save button
    time.sleep(1)
    savebuttonCords = pyautogui.locateCenterOnScreen("savebutton.png", grayscale = True)
    pyautogui.click(savebuttonCords)

    #Explorer save window action
    time.sleep(1)
    pyautogui.press('enter')

    #Close picture popup
    time.sleep(1)
    pyautogui.click()

    #Go to next image
    nextbutton()

#Start of program__________________________________________________________________________________

#Open browser-CHANGE TO locateCenterOnScreen
pyautogui.moveTo(160, 760, 0.5)
pyautogui.click()

#Actual download___________________________________________________________________________________

#1st picture in new folder
firstscrape()

#Rest of the pictures
for x in range(int(number)-1):
    scrape()
