import cv2
import sys
import winsound
from board import drawX, drawO
import random
    
#detects empty square and fills a value accordingly X
def detectEmptySquareai(img,img_rgb,cnt,j,cc,bol):
    x, y, w, h = cv2.boundingRect(cnt)
    sub_img = img[y:y+h, x:x+w]
    _, sub_thresh = cv2.threshold(sub_img, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    if cv2.sumElems(sub_thresh)[0] > 180000: # adjust threshold as needed
        print("")
    else:
        # print("jX = "+str(j))
        if j==(9-cc):
            winsound.Beep(1240, 400)
            drawX(img_rgb,x,w,y,h)
            bol = False
      
    j+=1
    return bol,j


def moveai(img,img_rgb,cntours,bol,j):
    cntx = 0
    cnto=0
    xlist = []
    olist = []
    i=1
    for cnt in cntours:
        x, y, w, h = cv2.boundingRect(cnt)
        sub_img = img[y:y+h, x:x+w]
        _, sub_thresh = cv2.threshold(sub_img, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
        # print("sum: "+str(cv2.sumElems(sub_thresh)[0]))
        j = 10-i
        if cv2.sumElems(sub_thresh)[0] > 183500 and cv2.sumElems(sub_thresh)[0] < 183700: # adjust threshold as needed
            # print("X detected on"+str(j))
            # cntx+=1
            xlist.append(j)

        elif cv2.sumElems(sub_thresh)[0] > 220800 and cv2.sumElems(sub_thresh)[0] < 220900: # adjust threshold as needed
            # print("0 detected on"+str(j))
            cnto+=1
            olist.append(j)
        i+=1    
            # moveAI(img,img_rgb,cnt,j,cc)
    chk = False
    checklist = [[1,2,3],
                 [1,4,7],
                 [7,8,9],
                 [3,6,9],
                ]
    xset = set(xlist)
    oset = set(olist)
    if(len(oset)==2):
        chk = True
    if chk:

        for lst in checklist:
            check =  all(item in lst for item in xset)
            sub_list = list(set(lst) - set(xset))
            if sub_list[0] not in oset:
                print("")
            else:
                check = False
                chk = False    
            if check:

                print("list main agya")
                print(lst)
                print(xset)
                print(oset)
                # find missing number an fill that
                sub_list = list(set(lst) - set(xset))
                # put O on sub_list[0]
                print("sublist")
                print(sub_list)
                kl = 0
                for cnt in cntours:
                    area = cv2.contourArea(cnt)
                    if area > 300: # Filter out small contours
                        if(kl==(10-sub_list[0]-1)):
                            x, y, w, h = cv2.boundingRect(cnt)
                            sub_img = img[y:y+h, x:x+w]
                            _, sub_thresh = cv2.threshold(sub_img, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
                            drawO(img_rgb,x,w,y,h)
                            bol = True
                            print("horaha 2 wala")
                            print(kl)
                            print(sub_list[0])
                    kl+=1

    if not chk:
        # genrate random number other than oset and xset
        combined = oset.union(xset)
        random_number = random.randint(1, 9)
        kl2=0

# keep generating a new random number until it is not in the combined set
        while random_number in combined:
            random_number = random.randint(1, 9)
        for cnt in cntours:
            area = cv2.contourArea(cnt)
            if area > 300: # Filter out small contours
                if(kl2==(10-random_number-1)):
                    x, y, w, h = cv2.boundingRect(cnt)
                    sub_img = img[y:y+h, x:x+w]
                    _, sub_thresh = cv2.threshold(sub_img, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
                    drawO(img_rgb,x,w,y,h)
                    bol = True
                    print("horaha 1 wala") 
                    print(kl2)
                    
                    print(random_number)
            kl2+=1       

        print("")


    j+=1
    bol = True
    print(oset)
    print(xset)
    chk = False
    return bol,j

#detects empty square and fills a value accordingly O
# bol,j = detectOSquareai(img,img_rgb,cnt,j,cc,bol)
# cnt = contour 
# j = to count the contour
# cc = fingercount



def checkresultai(img,cntours):

    cntx = 0
    cnto=0
    xlist = []
    olist = []
    i=1
    for cnt in cntours:
        x, y, w, h = cv2.boundingRect(cnt)
        sub_img = img[y:y+h, x:x+w]
        _, sub_thresh = cv2.threshold(sub_img, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
        # print("sum: "+str(cv2.sumElems(sub_thresh)[0]))
        j = 10-i
        if cv2.sumElems(sub_thresh)[0] > 183500 and cv2.sumElems(sub_thresh)[0] < 183700: # adjust threshold as needed
            # print("X detected on"+str(j))
            # cntx+=1
            xlist.append(j)

        elif cv2.sumElems(sub_thresh)[0] > 220800 and cv2.sumElems(sub_thresh)[0] < 220900: # adjust threshold as needed
            # print("0 detected on"+str(j))
            cnto+=1
            olist.append(j)
        i+=1    
            # moveAI(img,img_rgb,cnt,j,cc)
 
    checklist = [[1,2,3],
                 [4,5,6],
                 [7,8,9],
                 [1,5,9],
                 [3,5,7],
                 [2,5,8],
                 [1,4,7],
                 [3,6,9]]
    
    xset = set(xlist)
    for lst in checklist:
        if set(lst).issubset(xset):
            xshow = cv2.imread('xwon.png')
            cv2.namedWindow('Xwon', cv2.WINDOW_NORMAL)
            cv2.setWindowProperty("Xwon",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
            cv2.resizeWindow("Xwon", 525, 456)
            cv2.imshow("Xwon", xshow)
            cv2.moveWindow("Xwon", 21,128) 
            print(f"{lst} is a subset of {xlist}")
            return "x"

    oset = set(olist)
    for lst in checklist:
        if set(lst).issubset(oset):
            print(f"{lst} is a subset of {olist}")
            oshow = cv2.imread('owon.png')
            cv2.namedWindow('Owon', cv2.WINDOW_NORMAL)
            cv2.setWindowProperty("Owon",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
            cv2.resizeWindow("Owon", 525, 456)
            cv2.imshow("Owon", oshow)
            cv2.moveWindow("Owon", 21,128) 
            return "o"


    if len(xlist)+len(olist)>=9:
        draw = cv2.imread('draw.png')
        cv2.namedWindow('Draw', cv2.WINDOW_NORMAL)
        cv2.setWindowProperty("Draw",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        cv2.resizeWindow("Draw", 525, 456)
        cv2.imshow("Draw", draw)
        cv2.moveWindow("Draw", 21,128) 
        return "d"
        # print(f"{lst} is a subset of {xlist}")


    # print("cntx:"+str(xlist)+"\n cnto:"+str(olist))
    return "n"






#Takes in input as the count of fingers and fills the box accordingly
def callboxai(cc,key,bol):
   


    if key == ord('q'):
        sys.exit()
    j=0
    k=0
    img = cv2.imread('box2.png', cv2.IMREAD_GRAYSCALE)
    _, thresh = cv2.threshold(img, 170, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    img_rgb = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

    # Draw bounding box around each contour and check for text
 
#  Check to maintain alternating turns
    if bol:
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 300: # Filter out small contours
                bol,j = detectEmptySquareai(img,img_rgb,cnt,j,cc,bol)
        # bol = False   
    else:
        # for cnt in contours:
        #     area = cv2.contourArea(cnt)
        #     if area > 300: # Filter out small contours
            bol,j = moveai(img,img_rgb,contours,bol,j)
        # bol = True   
    
    re = checkresultai(img,contours)
    


  
    cv2.destroyWindow('Board2')
#  Update the board
    cv2.imwrite('box2.png',img_rgb)
    # imgg= cv2.imread('box1.png')
    # cv2.imshow('Result', img_rgb)
    imS = cv2.resize(img_rgb, (530, 460)) 

    # cv2.imshow('Board', imS)

    # cv2.resizeWindow("Result", 520, 520)
    cv2.namedWindow('Board2', cv2.WINDOW_NORMAL)
    cv2.moveWindow("Board2", 775,130) 
    cv2.setWindowProperty("Board2",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    cv2.resizeWindow('Board2', 530, 460)
    cv2.moveWindow("Board2", 775,130) 
    cv2.imshow('Board2', imS)
    return bol,re