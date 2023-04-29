import cv2
import numpy as np
from handcapture import *
from board import *
import sys
import random

box1 = cv2.imread('box1.png')
bg = cv2.imread('BG.png')

cv2.namedWindow("Tic_Tac_Toe", cv2.WND_PROP_FULLSCREEN)
# cv2.putText(bg, str(int(2)), (605, 435), cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 4)

startGame = False
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
# cv2.imshow('Result',box1)
# box2 = cv2.imread('box.png')
detector = HandDetector(maxHands=2, detectionCon=0.8)
video = cv2.VideoCapture(0)

      
while True:
    key = cv2.waitKey(1)
    # To start
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

    if startGame:   
        # key = cv2.waitKey(1)
        if key == ord('q'):
            print("q observed in s")
            sys.exit()
        cnt = handsTimer(video, detector,bg,key=key)
        bol = callbox(cnt,key,bol)
        # cnt2 = random.randint(1,10)

        # moveAI(cnt)
        print("value of key in start: "+str(key))
        
       
       
    print("value of key out start: "+str(key))

    print("end loop")


   