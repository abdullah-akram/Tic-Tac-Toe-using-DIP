import cv2
from handcapture import *
from board import *
import sys
from PIL import Image
import winsound
from computerAi import *

box1 = cv2.imread('box1.png')
box5 = cv2.imread('box2.png')
box9 = cv2.imread('wait.png')
bg = cv2.imread('BG.png')
bg4 = cv2.imread('BG2.png')

cv2.namedWindow("Tic_Tac_Toe", cv2.WND_PROP_FULLSCREEN)
# cv2.putText(bg, str(int(2)), (605, 435), cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 4)

startGame = False
computerai = False
cv2.setWindowProperty("Tic_Tac_Toe",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)


cv2.namedWindow("Result", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Result",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

cv2.imshow('Result',bg)

imS = cv2.resize(box1, (560, 450)) 
cv2.namedWindow('Board', cv2.WINDOW_NORMAL)
cv2.setWindowProperty("Board",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
cv2.resizeWindow('Board', 530, 460)
cv2.moveWindow("Board", 775,130) 

bol = True 

cv2.imshow('Board', imS)




imS4 = cv2.resize(box9, (560, 450)) 
cv2.namedWindow('Board5', cv2.WINDOW_NORMAL)
cv2.setWindowProperty("Board5",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
cv2.resizeWindow('Board5', 525, 456)
cv2.moveWindow("Board5",21,128) 

cv2.imshow('Board5', imS4)

detector = HandDetector(maxHands=2, detectionCon=0.8)
video = cv2.VideoCapture(0)
ress = ''
kk = True    

cv2.destroyWindow('Board5')



while True:
    key = cv2.waitKey(1)
    # To start
    if key==ord('a'):
        computerai = True
        cv2.destroyWindow('Result')

    if key == ord('s'):
        print("value of key in s: "+str(key))
        startGame = True
        cv2.destroyWindow('Result')
        # To See instructions
    if key == ord('i'):
        bg2 = cv2.imread('instruction.png')
        cv2.destroyWindow('Result')

        cv2.namedWindow("Result", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("Result",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

        cv2.imshow('Result',bg2)
# To quit
    if key == ord('q'):
        print("q observed")
        exit()

    if computerai:
        if kk:
            imS = cv2.resize(box5, (560, 450)) 
            cv2.namedWindow('Board2', cv2.WINDOW_NORMAL)
            cv2.setWindowProperty("Board2",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
            cv2.resizeWindow('Board2', 530, 460)
            cv2.moveWindow("Board2", 775,130) 

            cv2.imshow('Board2', imS)
            kk  =False
        if ress=='d' or ress=='x' or ress == 'o':
            img_box = Image.open("box2o.png")
            img_box1 = Image.open("box2.png")
            # Copy the content of img_box to img_box1
            img_box1.paste(img_box, (0, 0))
            # Save the modified image
            img_box1.save("box2.png")
            winsound.Beep(240, 1000)
            while True:
                key3 = cv2.waitKey(1)
                if key3 == ord('q'):
                    sys.exit()
                    
        if key == ord('q'):
            print("q observed in s")
            sys.exit()
        ccc = handsTimer(video, detector,bg4,key=key)
        bol,ress = callboxai(ccc,key,bol)    
        # One turn of user
        # One turn of computer
        # Check if user has a valid input if not then check again 


    if startGame:   
        
        if ress=='d' or ress=='x' or ress == 'o':
            img_box = Image.open("box.png")
            img_box1 = Image.open("box1.png")
            # Copy the content of img_box to img_box1
            img_box1.paste(img_box, (0, 0))
            # Save the modified image
            img_box1.save("box1.png")
            winsound.Beep(240, 1000)

            while True:
                key3 = cv2.waitKey(1)
                if key3 == ord('q'):
                    sys.exit()
                    
        if key == ord('q'):
            print("q observed in s")
            sys.exit()
        ccc = handsTimer(video, detector,bg4,key=key)
        bol,ress = callbox(ccc,key,bol)
        
    


   